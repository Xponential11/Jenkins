import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def tax_sums(journal_df, months=None):
    """ Returns a DataFrame with sales and tax rates -
         If a number or list is passed to 'months', only the sales
         of the corresponding months will be used.
         Example: tax_sums(df, months=[3, 6]) will only use the months
         3 (March) and 6 (June)"""
    if months:
        if isinstance(months, int):
            month_cond = journal_df.index.month == months
        elif isinstance(months, (list, tuple)):
            month_cond = journal_df.index.month.isin(months)
        positive = journal_df["gross amount"] > 0
        # sales_taxes eq. umsatzsteuer
        sales_taxes = journal_df[positive & month_cond]
        negative = journal_df["gross amount"] < 0
        # input_taxes equivalent to German Vorsteuer
        input_taxes = journal_df[negative & month_cond]   
    else:
        sales_taxes = journal_df[journal_df["gross amount"] > 0]
        input_taxes = journal_df[journal_df["gross amount"] < 0]
    
    sales_taxes = sales_taxes[["tax rate", "gross amount"]].groupby("tax rate").sum()
    sales_taxes.rename(columns={"gross amount": "Sales Gross"},
                       inplace=True)
    sales_taxes.index.name = 'Tax Rate'
    
    input_taxes = input_taxes[["tax rate", "gross amount"]].groupby("tax rate").sum()
    input_taxes.rename(columns={"gross amount": "Expenses Gross"},
                      inplace=True)
    input_taxes.index.name = 'Tax Rate'
    
    taxes = pd.concat([input_taxes, sales_taxes], axis=1)
    taxes.insert(1, 
                 column="Input Taxes", 
                 value=(taxes["Sales Gross"] * taxes.index / 100).round(2))
    taxes.insert(3, 
                 column="Sales Taxes", 
                 value=(taxes["Expenses Gross"] * taxes.index / 100).round(2))

    return taxes.fillna(0)



with pd.ExcelFile("net_income_method_2020.xlsx") as xl:
    accounts2descr = xl.parse("account numbers", 
                              index_col=0)
    journal = xl.parse("journal", 
                       index_col=0,
                      )
    
journal.index = pd.to_datetime(journal.index)
# print(journal.index)

account_sums = journal[["account number", "gross amount"]].groupby("account number").sum()
# print(account_sums)

income_accounts = account_sums[account_sums["gross amount"] > 0] 
# print(income_accounts)
plot = income_accounts.plot(y='gross amount', figsize=(5, 5), kind="pie")


expenses_accounts = account_sums[account_sums["gross amount"] < 0]
# print(expenses_accounts)

acc2descr_expenses = accounts2descr["description"].loc[expenses_accounts.index]
# print(acc2descr_expenses)


expenses_accounts.set_index(acc2descr_expenses.values, inplace=True)
expenses_accounts *= -1

labels = [''] * len(expenses_accounts)
plot = expenses_accounts.plot(kind="pie",
                            y='gross amount', 
                            figsize=(5, 5),
                            labels=labels)
plot.legend(bbox_to_anchor=(0.5, 0.5), 
            labels=expenses_accounts.index)

plt.show()

journal.drop(columns=["account number"])


print(tax_sums(journal, months=[5, 6]))



