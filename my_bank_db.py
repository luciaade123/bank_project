"""
Lucia Adeola
project 2
step 2
my_bank_db.py
"""

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


class BankDB:
    def __init__(self, vault_file):
        with open(vault_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # username and password for user
        username = lines[0].strip()
        password = lines[1].strip()

        # connect to the bank database and return connection
        try:
            self.conn = psycopg2.connect(
                dbname="bank",
                user=username,
                password=password,
                host="localhost",
                port="5432"
            )
            print("successfully connected to database")
        except Exception as error:
            print("connection failed", error)

    def get_monthly_transactions(self, year, month):
        """
        Retrieve transactions for given year and month.
        """
        try:
            query = """
                SELECT * FROM transaction
                WHERE EXTRACT(YEAR FROM txn_date) = %s
                  AND EXTRACT(MONTH FROM txn_date) = %s;
            """
            transactions_df = pd.read_sql(query, self.conn, params=(year, month))

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

        except Exception as error:
            print("error in get_monthly_transactions:", error)
            return pd.DataFrame()

    def transactions_barplot(self, year, month):
        """
        Plots bar plot of the transactions per day for provided month and year.
        """
        # get data for given month and year
        transactions_df = self.get_monthly_transactions(year, month)

        # if dummy, do not plot
        if transactions_df['txn_id'].iloc[0] == -1:
            print("no transactions to plot")
            return

        # Convert 'txn_date' to datetime object if needed
        transactions_df['txn_date'] = pd.to_datetime(transactions_df['txn_date'])

        # pull the day from the date
        transactions_df['day'] = transactions_df['txn_date'].dt.day

        # Sum/total transactions per day
        daily_total = transactions_df.groupby('day')['amount'].sum()

        # Plot the bar plot
        plt.figure(figsize=(10, 5))
        daily_total.plot(kind='bar', color='red')
        plt.title(f'Total Transactions per Day for {month}/{year}')
        plt.xlabel('Day of Month')
        plt.ylabel('Total Amount')
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()