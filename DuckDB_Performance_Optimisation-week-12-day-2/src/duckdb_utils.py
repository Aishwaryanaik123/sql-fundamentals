"""Reusable DuckDB-to-Pandas query helper with an in-memory result cache."""
from functools import lru_cache
from pathlib import Path
import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "sales_analytics.duckdb"
CSV_PATH = ROOT / "data" / "sales_100k.csv"

_connection = duckdb.connect(str(DB_PATH))

# Create the table once when the database is first initialized.
_table_exists = _connection.execute(
    "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'sales'"
).fetchone()[0] > 0
if not _table_exists:
    _connection.execute(
        "CREATE TABLE sales AS SELECT * FROM read_csv_auto(?)", [str(CSV_PATH)]
    )

@lru_cache(maxsize=128)
def _cached_query(sql: str) -> pd.DataFrame:
    """Run SQL once per distinct SQL string and cache its DataFrame result."""
    return _connection.execute(sql).fetchdf()

def query_to_df(sql: str) -> pd.DataFrame:
    """Take a SQL string and return the DuckDB result as a Pandas DataFrame."""
    if not isinstance(sql, str) or not sql.strip():
        raise ValueError("sql must be a non-empty string")
    return _cached_query(sql).copy(deep=True)

def clear_query_cache() -> None:
    """Clear cached query results after the underlying data changes."""
    _cached_query.cache_clear()

def close_connection() -> None:
    _connection.close()
