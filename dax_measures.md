# DAX Basics – Week 3 Day 2

## 1. CALCULATE() – Apply Filters on Measures

```DAX
Total Sales = SUM(Sales_Data[Sales])

Filtered Sales =
CALCULATE(
    [Total Sales],
    Sales_Data[Category] = "Electronics"
)
```

**Explanation:**
`CALCULATE()` evaluates an expression in a modified filter context. Here, `Total Sales` is calculated only for the Electronics category.

---

## 2. YTD Sales using DATESYTD()

```DAX
YTD Sales =
CALCULATE(
    [Total Sales],
    DATESYTD(Sales_Data[OrderDate])
)
```

**Explanation:**
`DATESYTD()` returns the dates from the beginning of the year up to the current date. `CALCULATE()` then calculates total sales for that period.

---

## 3. Running Total using EARLIER()

```DAX
Running Total =
CALCULATE(
    SUM(Sales_Data[Sales]),
    FILTER(
        ALL(Sales_Data[OrderDate]),
        Sales_Data[OrderDate] <= EARLIER(Sales_Data[OrderDate])
    )
)
```

**Explanation:**
This calculated column calculates cumulative sales up to the current row's date. `EARLIER()` allows the current row's date to be compared with other rows while evaluating the expression.

---

## 4. Calculated Column – Profit Margin %

```DAX
Profit Margin % =
DIVIDE(
    Sales_Data[Profit],
    Sales_Data[Sales],
    0
) * 100
```

**Explanation:**
This calculated column calculates profit margin for each row by dividing Profit by Sales and multiplying the result by 100. `DIVIDE()` safely handles cases where Sales is zero.

---

## 5. Context Transition – Row Context to Filter Context

```DAX
Profit by Row =
CALCULATE(
    SUM(Sales_Data[Profit])
)
```

**Explanation:**
Context transition occurs when `CALCULATE()` converts the current row context into filter context. This is especially important when `CALCULATE()` is used inside a calculated column or iterator.

### Summary

* `CALCULATE()` modifies filter context.
* `DATESYTD()` is used for Year-to-Date calculations.
* `EARLIER()` can access an earlier row context in nested row-context calculations.
* Calculated columns calculate values row by row and are stored in the model.
* Measures are calculated dynamically based on the current filter context.
* Context transition converts row context into filter context through `CALCULATE()`.
