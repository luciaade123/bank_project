# Project : Bank Database Secure Connection & Transaction Retrieval using Python & PostgreSQL

## Professional Summary
This project showcases my ability to securely connect to a PostgreSQL database using Python and SQLAlchemy, retrieve transaction data based on user inputs, and structure logic using object-oriented programming.
It highlights my understanding of:
- Secure credential handling (via external vault file)
- SQL querying using Python
- Building and testing Python functions
- Error handling and clean output formatting
- Notebook-based walkthroughs for reproducibility
The use case simulates a real-world scenario where a financial analyst or banking system retrieves and analyzes transaction data by date. This project demonstrates my ability to work independently, write clean and maintainable code, and present technical work in a clear, step-by-step format for future stakeholders.



## Project Overview
This project details how to securely connect to a PostgresSQL bank database using using SQLAlchemy, execute python functions to retrieve transactions based on user input, demonstrates basic python classes and error handling.
The Jupyter Notebook (`Python_project_2.ipynb`) provides a step-by-step walkthrough of each component — including database connection, transaction retrieval, and class-based implementation — making the logic easy to follow and test.


## Technologies Used
- Python 3
- PostgreSQL
- SQLALCHEMY
- Pandas
- Jupyter Notebook
- Spyder


# Project Features
- Connect to PostgresSQL via secure credentials from a 'vault.txt' file
- Retrieve monthly transactions using SQL 'EXTRACT()'
- Encapsulates logic in a Python class
- Handle errors and invalid outputs in a clean output
-  Test the functions via jupyter Notebook


## Files
- 'vault.txt': Contains Postgresql username and password (not uploaded for security)
- 'my_db_connection.py': secure connection python function
- 'get_monthly_transactions.py': transactions retrieval python function
- 'my_bank_db.py': python class to retrieve transactions for a given date and plot the results
- 'Python_project_2.ipynb': Jupyter note book to run and test the logic.
- 'README.md': project overview
