import pandas as pd
import great_expectations as gx
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.expectations import (
    ExpectColumnValuesToNotBeNull,
    ExpectColumnValuesToBeBetween,
    ExpectColumnValuesToBeInSet,
)


# ---------------------------------------------------------
# 1. Load original dataset
# ---------------------------------------------------------

df = pd.read_csv("Employee.csv")

print("Original dataset shape:", df.shape)


# ---------------------------------------------------------
# 2. Create a test copy
# ---------------------------------------------------------

test_df = df.copy()


# ---------------------------------------------------------
# 3. Inject 3 intentional data-quality errors
# ---------------------------------------------------------

# Error 1: Invalid PaymentTier
test_df.loc[0, "PaymentTier"] = 5

# Error 2: Invalid Age
test_df.loc[1, "Age"] = 150

# Error 3: Invalid Gender
test_df.loc[2, "Gender"] = "Unknown"


# Save the intentionally corrupted dataset
test_df.to_csv("Employee_quality_test.csv", index=False)

print("\nThree intentional errors were added:")
print("1. PaymentTier = 5")
print("2. Age = 150")
print("3. Gender = Unknown")


# ---------------------------------------------------------
# 4. Create Great Expectations context
# ---------------------------------------------------------

context = gx.get_context(mode="file")


# ---------------------------------------------------------
# 5. Create expectation suite
# ---------------------------------------------------------

suite = ExpectationSuite(
    name="employee_data_quality_suite"
)


# ---------------------------------------------------------
# 6. Add 8 expectations
# ---------------------------------------------------------

# Expectation 1
suite.add_expectation(
    ExpectColumnValuesToNotBeNull(
        column="Education"
    )
)

# Expectation 2
suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="JoiningYear",
        min_value=2000,
        max_value=2020
    )
)

# Expectation 3
suite.add_expectation(
    ExpectColumnValuesToBeInSet(
        column="City",
        value_set=[
            "Bangalore",
            "Pune",
            "New Delhi"
        ]
    )
)

# Expectation 4
suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="PaymentTier",
        min_value=1,
        max_value=3
    )
)

# Expectation 5
suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="Age",
        min_value=18,
        max_value=60
    )
)

# Expectation 6
suite.add_expectation(
    ExpectColumnValuesToBeInSet(
        column="Gender",
        value_set=[
            "Male",
            "Female"
        ]
    )
)

# Expectation 7
suite.add_expectation(
    ExpectColumnValuesToBeBetween(
        column="ExperienceInCurrentDomain",
        min_value=0,
        max_value=20
    )
)

# Expectation 8
suite.add_expectation(
    ExpectColumnValuesToBeInSet(
        column="LeaveOrNot",
        value_set=[
            0,
            1
        ]
    )
)


# ---------------------------------------------------------
# 7. Save the expectation suite
# ---------------------------------------------------------

context.suites.add_or_update(suite)

print("\nExpectation suite created successfully.")
print("Number of expectations:", len(suite.expectations))


# ---------------------------------------------------------
# 8. Create Pandas data source
# ---------------------------------------------------------

data_source = context.data_sources.add_pandas(
    name="employee_pandas_source"
)


# ---------------------------------------------------------
# 9. Create data asset
# ---------------------------------------------------------

data_asset = data_source.add_dataframe_asset(
    name="employee_quality_test"
)


# ---------------------------------------------------------
# 10. Create batch definition
# ---------------------------------------------------------

batch_definition = data_asset.add_batch_definition_whole_dataframe(
    "employee_batch"
)


# ---------------------------------------------------------
# 11. Create batch from corrupted DataFrame
# ---------------------------------------------------------

batch = batch_definition.get_batch(
    batch_parameters={
        "dataframe": test_df
    }
)


# ---------------------------------------------------------
# 12. Validate the data
# ---------------------------------------------------------

validation_results = batch.validate(suite)


# ---------------------------------------------------------
# 13. Display validation results
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("GREAT EXPECTATIONS VALIDATION RESULTS")
print("=" * 60)

print(
    "\nOverall validation result:",
    validation_results.success
)

print(
    "Successful expectations:",
    sum(
        result.success
        for result in validation_results.results
    )
)

print(
    "Total expectations:",
    len(validation_results.results)
)


# ---------------------------------------------------------
# 14. Display individual results
# ---------------------------------------------------------

print("\nIndividual expectation results:")

for i, result in enumerate(
    validation_results.results,
    start=1
):
    print(
        f"{i}. {result.expectation_config.type} "
        f"-> {'PASS' if result.success else 'FAIL'}"
    )


# ---------------------------------------------------------
# 15. Save validation results
# ---------------------------------------------------------

import json
from pathlib import Path

Path("validation_report").mkdir(
    exist_ok=True
)

with open(
    "validation_report/validation_results.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        validation_results.to_json_dict(),
        file,
        indent=4
    )


print(
    "\nValidation results saved to:"
    " validation_report/validation_results.json"
)

print("\nValidation completed.")