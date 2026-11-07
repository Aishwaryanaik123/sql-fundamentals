"""
A/B Test Analysis
Runs with Python's standard library only. Produces analysis_results.csv and
experiment_summary.txt. The sample dataset is synthetic and for practice.
"""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "ab_test_data.csv"

def normal_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def analyze():
    groups = {"A": [], "B": []}
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            groups[row["variant"]].append({
                "converted": int(row["converted"]),
                "revenue": float(row["revenue"])
            })

    n_a, n_b = len(groups["A"]), len(groups["B"])
    x_a = sum(r["converted"] for r in groups["A"])
    x_b = sum(r["converted"] for r in groups["B"])
    p_a, p_b = x_a / n_a, x_b / n_b
    pooled = (x_a + x_b) / (n_a + n_b)
    se = math.sqrt(pooled * (1-pooled) * (1/n_a + 1/n_b))
    z = (p_b - p_a) / se
    p_value = 2 * (1 - normal_cdf(abs(z)))
    lift = ((p_b - p_a) / p_a) * 100 if p_a else 0
    revenue_a = sum(r["revenue"] for r in groups["A"]) / n_a
    revenue_b = sum(r["revenue"] for r in groups["B"]) / n_b

    results = [
        ("users_A", n_a), ("users_B", n_b),
        ("conversions_A", x_a), ("conversions_B", x_b),
        ("conversion_rate_A", p_a), ("conversion_rate_B", p_b),
        ("absolute_lift", p_b-p_a), ("relative_lift_percent", lift),
        ("z_statistic", z), ("p_value_two_sided", p_value),
        ("average_revenue_per_user_A", revenue_a),
        ("average_revenue_per_user_B", revenue_b),
        ("statistically_significant_at_5_percent", p_value < 0.05)
    ]
    with (ROOT/"analysis_results.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        writer.writerows(results)

    conclusion = ("Variant B shows a statistically significant improvement at the 5% level."
                  if p_value < 0.05 else
                  "The observed difference is not statistically significant at the 5% level.")
    summary = f"""A/B TEST SUMMARY
================
Experiment: Landing page conversion test
Control: Variant A | Treatment: Variant B
Users: A={n_a}, B={n_b}
Conversions: A={x_a}, B={x_b}
Conversion rate: A={p_a:.2%}, B={p_b:.2%}
Absolute lift: {p_b-p_a:.2%}
Relative lift: {lift:.2f}%
Two-proportion z statistic: {z:.4f}
Two-sided p-value: {p_value:.6f}
Decision (alpha=0.05): {conclusion}

Average revenue per user:
A=${revenue_a:.2f} | B=${revenue_b:.2f}

Caution: This is synthetic practice data. Statistical significance does not
prove causality if randomization, instrumentation, or experiment design is flawed.
"""
    (ROOT/"experiment_summary.txt").write_text(summary, encoding="utf-8")
    print(summary)

if __name__ == "__main__":
    analyze()
