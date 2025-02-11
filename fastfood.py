import pandas as pd
import statsmodels.api as sm

def main(data):
    predictors = ['total_fat', 'sat_fat', 'cholesterol', 'sodium']
    X = sm.add_constant(data[predictors])

    y = data['calories']
    model = sm.OLS(y, X).fit()

    print(model.mse_total.round(2))
    print(model.rsquared.round(2))
    print(model.params.round(2))
    print(model.pvalues.round(2))

data = pd.read_csv('fastfood.csv')
main(data)

