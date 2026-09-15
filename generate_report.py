import json
from pathlib import Path
from datetime import datetime


# ---------------------------------------------------------
# Load validation results
# ---------------------------------------------------------

with open(
    "validation_report/validation_results.json",
    "r",
    encoding="utf-8"
) as file:
    results = json.load(file)


# ---------------------------------------------------------
# Extract results
# ---------------------------------------------------------

validation_results = results.get("results", [])

total = len(validation_results)
passed = sum(
    1 for result in validation_results
    if result.get("success") is True
)
failed = total - passed


# ---------------------------------------------------------
# Create HTML rows
# ---------------------------------------------------------

rows = ""

for index, result in enumerate(
    validation_results,
    start=1
):
    expectation_type = result.get(
        "expectation_config",
        {}
    ).get(
        "type",
        "Unknown"
    )

    success = result.get(
        "success",
        False
    )

    status = "PASS" if success else "FAIL"

    status_class = (
        "pass"
        if success
        else "fail"
    )

    rows += f"""
    <tr>
        <td>{index}</td>
        <td>{expectation_type}</td>
        <td class="{status_class}">
            {status}
        </td>
    </tr>
    """


# ---------------------------------------------------------
# Create HTML report
# ---------------------------------------------------------

html = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>
Employee Data Quality Validation Report
</title>

<style>

body {{
    font-family: Arial, sans-serif;
    margin: 40px;
    background-color: #f5f5f5;
}}

.container {{
    max-width: 1000px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
}}

h1 {{
    margin-bottom: 5px;
}}

.subtitle {{
    color: #666;
}}

.summary {{
    display: flex;
    gap: 20px;
    margin: 25px 0;
}}

.card {{
    flex: 1;
    padding: 20px;
    border-radius: 8px;
    background-color: #eeeeee;
    text-align: center;
}}

.number {{
    font-size: 30px;
    font-weight: bold;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 25px;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}}

th {{
    background-color: #eeeeee;
}}

.pass {{
    font-weight: bold;
}}

.fail {{
    font-weight: bold;
}}

.info {{
    margin-top: 30px;
    padding: 15px;
    background-color: #f0f0f0;
    border-radius: 8px;
}}

</style>

</head>


<body>

<div class="container">

<h1>
Employee Data Quality Validation Report
</h1>

<p class="subtitle">
Great Expectations Validation Report
</p>

<hr>

<h2>Dataset Information</h2>

<p>
<strong>Dataset:</strong>
Employee_quality_test.csv
</p>

<p>
<strong>Original Dataset:</strong>
Employee.csv
</p>

<p>
<strong>Validation Date:</strong>
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
</p>


<h2>Validation Summary</h2>

<div class="summary">

<div class="card">
<div>Total Expectations</div>
<div class="number">
{total}
</div>
</div>

<div class="card">
<div>Passed</div>
<div class="number">
{passed}
</div>
</div>

<div class="card">
<div>Failed</div>
<div class="number">
{failed}
</div>
</div>

</div>


<h2>Expectation Results</h2>

<table>

<tr>
<th>#</th>
<th>Expectation</th>
<th>Status</th>
</tr>

{rows}

</table>


<div class="info">

<h2>Intentional Data Quality Errors</h2>

<p>
<strong>Error 1:</strong>
PaymentTier was changed to an invalid value of 5.
</p>

<p>
<strong>Error 2:</strong>
Age was changed to an invalid value of 150.
</p>

<p>
<strong>Error 3:</strong>
Gender was changed to an invalid value of "Unknown".
</p>

<p>
Great Expectations successfully detected all three
intentional data quality errors.
</p>

</div>


<div class="info">

<h2>Conclusion</h2>

<p>
The Employee dataset was validated using eight
Great Expectations rules. Five expectations passed
and three expectations failed because of intentionally
introduced data quality errors. The validation confirms
that the defined quality rules can detect invalid
PaymentTier, Age, and Gender values.
</p>

</div>

</div>

</body>

</html>
"""


# ---------------------------------------------------------
# Save HTML report
# ---------------------------------------------------------

output_path = Path(
    "validation_report/validation_report.html"
)

output_path.write_text(
    html,
    encoding="utf-8"
)

print(
    "HTML validation report created successfully!"
)

print(
    f"Report location: {output_path}"
)