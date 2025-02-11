import pandas as pd
import statsmodels.api as sm

def main(data):
    data.rename(columns = {'Credit amount' : 'Credit_amount'}, inplace = True)

    predictors = ['Age', 'Duration']

    X = sm.add_constant(data[predictors])

    y = data['Credit_amount']
    model = sm.OLS(y, X).fit()

    print(model.params.round(2))
    print(model.rsquared.round(2))
    

data = pd.read_csv('german_credit_data.csv')
main(data)

