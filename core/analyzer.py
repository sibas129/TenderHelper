import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

global reg

df = pd.read_csv('data.csv')
reg = LinearRegression()

reg.fit(df[['trading_volume', 'mean_trading_volume', 'terminated_contract', 'winner_dicline_more_25']].values, df.winrate)

X_incl_const = sm.add_constant(df[['trading_volume', 'mean_trading_volume', 'terminated_contract', 'winner_dicline_more_25']])
model = sm.OLS(df.winrate, X_incl_const)
results = model.fit()

print(reg.coef_)
print(reg.intercept_)
print(results.pvalues)


def result(int):
    return reg.predict([[200, 10, 8, 8]])
