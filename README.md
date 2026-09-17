\# Week 3 Day 2 – DAX Basics



\## Project Overview



This task focuses on learning and applying basic DAX concepts in Power BI. The practical work includes creating measures, calculated columns, time-based calculations, running totals, and understanding context transition.



\## Tasks Completed



\* Created a `Total Sales` measure using `SUM()`

\* Used `CALCULATE()` to apply filters to measures

\* Created a Year-to-Date Sales measure using `DATESYTD()`

\* Created a Running Total using `EARLIER()`

\* Created a Profit Margin % calculated column

\* Explained row context and filter context

\* Explained context transition using `CALCULATE()`



\## DAX Concepts Used



\### CALCULATE()



Used to evaluate an expression in a modified filter context.



\### DATESYTD()



Used to calculate values from the beginning of the year up to the current date.



\### EARLIER()



Used to access an earlier row context, particularly in calculated column calculations.



\### Profit Margin %



Calculated using:



`Profit Margin % = (Profit / Sales) × 100`



\### Context Transition



Context transition occurs when `CALCULATE()` converts row context into filter context.



\## Files



\* `dax\_measures.md` – Contains the five DAX expressions and their explanations.

\* `sales\_data.csv` – Dataset used for the Power BI DAX practical tasks.

\* `README.md` – Project documentation.



\## Tools Used



Power BI Desktop and DAX.



\## Git Branch



`feature/week-3-day-2`



\## Commit



`feat: dax-basics week-3-day-2 complete`



