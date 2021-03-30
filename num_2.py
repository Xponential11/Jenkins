import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit


xf = pd.ExcelFile("coronacases.xlsx")
df = xf.parse("Sheet1",skiprow = 2,index_col = 0,names= ['dates','cases','active','deaths'])
df[['cases','active','deaths']].plot()



discharged = df["cases"] - df["active"]

if "healed" in df.columns:
    df.drop("healed", axis=1, inplace=True)
if "healed" not in df.columns:
    df.insert(loc=len(df.columns),
              column="healed",
              value=(discharged -df["deaths"]))

healed_ratio = df["healed"] * 100 / discharged
print(healed_ratio)
death_ratio = df["deaths"] * 100 / discharged
print(death_ratio)

outcome = {"death_ratio": death_ratio, "healed_ratio": healed_ratio}
outcome_df = pd.DataFrame(outcome)
print(outcome_df)
outcome_df.plot()
# plt.show()

######################################################################
def growth_func(x, a, b, c):
  return a * np.exp(b * x) + c

Y = df.cases.values
X = np.arange(0, len(Y))
popt, pcov = curve_fit(growth_func, X, Y)

def growth(x):
    return growth_func(x, *popt)

plt.figure()
plt.plot(X, Y, 'ko', label="Original Data")
plt.plot(X, growth(X), 'r-', label="Fitted Curve")
plt.legend()

days_infected_before_outcome = 14
assumed_real_death_rate = 2.9

def create_inverse_growth_func(a, b, c):
    def inverse(x):
        return np.log((x - c) / a) / b
    return inverse

inverse_growth = create_inverse_growth_func(*popt)

# number of cases 'days_infected_before_outcome':
cases_days_infection_before = df["deaths"][-1] * 100 / assumed_real_death_rate 
shift_days = inverse_growth(cases_days_infection_before)
shift_days -= (len(df) - days_infected_before_outcome)
print(shift_days)

plt.figure()
X = np.arange(0, 65)
plt.plot(X, 
         growth_func(X + days_infected_before_outcome, *popt), 
         'r-', 
         label="Fitted Curve")
plt.legend()

print(len(df["cases"]))
x = np.arange(0, len(df["cases"]))
print(len(x))
if "real" in df.columns:
    df.drop("real", axis=1, inplace=True)
df.insert(loc=len(df.columns),
          column="real",
          value=growth(x+shift_days).astype(np.int))

df[["cases", "real"]].plot()
plt.show()

##########################################################################