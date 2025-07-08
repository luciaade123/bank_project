"""
Lucia Adeola
project 2
step 3
get_my_monthly_transactions.py
"""
import pandas as pd


def get_month_transactions(conn, year, month):
    """
    Pulls bank transactions for a specified month and year from bank database.
    Drops 'account_id' and returns a dataframe.
    If input is invalid(year and month), return warning and correct columns with all -1 values.

    Parameters
    ----------
    conn : PostgreSQL database connection
    year : int
        target year
    month : int
        target month

    Returns
    -------
    pandas.DataFrame
      transaction records or dummy data.
   """
    # query table transactions for given year and month
    try:
        query = """
            SELECT * FROM transaction
            WHERE EXTRACT(YEAR FROM txn_date) = %s
              AND EXTRACT(MONTH FROM txn_date) = %s;
        """
        transactions_df = pd.read_sql(query, conn, params=(year, month))

        # if not valid/no data, return correct columns with dummy row all -1 values
        if transactions_df.empty:
            columns = ['txn_id', 'txn_date', 'amount']
            dummy = pd.DataFrame([[-1] * len(columns)], columns=columns)
            print("no data found for specified date, returning dummy row.")
            return dummy

        # drop account_id column
        if 'account_id' in transactions_df.columns:
            transactions_df = transactions_df.drop(columns=['account_id'])

        return transactions_df

    # print incase of error
    except Exception as error:
        print("error in get_monthly_transactions:", error)
        return pd.DataFrame()
