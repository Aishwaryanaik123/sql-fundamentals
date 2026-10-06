\# Vanna AI - SQLite SQL Analyst



\## Project Overview



This project demonstrates a simple SQL analyst application using Vanna AI, SQLite, and FastAPI.



\## Database



Database: `sales.db`



Table: `sales`



The table contains 8 sales records with information about:



\- Customer name

\- Product

\- Category

\- Quantity

\- Price

\- Region



\## Training Examples



Five natural-language questions and their SQL queries were prepared:



1\. How many sales records are there?

2\. What is the total sales amount?

3\. What is the average product price?

4\. Which region has the most sales records?

5\. What is the total quantity sold?



\## Testing



Ten natural-language SQL questions were prepared and verified against the SQLite database.



\## FastAPI CIA Endpoint



Endpoint:



`POST /cia/sql-analyst`



Example questions tested:



\- How many sales records are there?

\- What is the total sales amount?



Both requests returned HTTP `200 OK`.



\## Technologies Used



Python, Vanna AI, SQLite, FastAPI, Uvicorn, OpenAI API

