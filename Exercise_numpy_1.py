import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


############################# Sub_ex-1###########################
exp_inc = pd.read_csv("expenses_and_income.csv", sep=";")
# print(exp_inc)
sums = exp_inc[['Out','In']].sum()
# print(sums)

category_sum = exp_inc.groupby('Category').sum()
# print(category_sum)


# ax = category_sum["Out"].plot.pie()
# ax.legend(loc="upper left", bbox_to_anchor=(1.5, 1))
# plt.show()
##################################################################

###########################Sub_ex-2###############################


category2account = {'monthly redemption payment': '200',
                    'insurances and taxes': '201',
                    'food and beverages': '202',
                    'education and culture': '203',
                    'transport': '204',
                    'health and sports': '205',
                    'household goods and services': '206',
                    'clothing': '207',
                    'communications': '208',
                    'restaurants and hotels': '209',
                    'utility': '210',
                    'other expenses': '211',
                    'Income': '400'}

exp_inc.replace(category2account,inplace=True)
exp_inc.rename(columns={'Category':'Accounts'},inplace=True)
print(exp_inc)

account_num = pd.Series(list(category2account.keys()),index = category2account.values())
account_num.name = "Description"
account_num.rename("Accounts")

exp_inc.insert(1,"accounts",account_num)

with pd.ExcelWriter("Expenses & Income.xlsx") as w:
    account_num.to_excel(w,"Account Numbers")
    exp_inc.to_excel(w,"Journal")
    w.save()