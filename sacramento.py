import pandas as pd
import statsmodels.api as sm

def main(data):
    data['bath_binary'] = (data['baths'] > 1).astype(int)
    predictors = ['beds', 'sqft', 'price']

    X = sm.add_constant(data[predictors])

    y = data['bath_binary']
    model = sm.Logit(y, X).fit()

    print(model.params.round(2))
    print(model.pvalues.round(2))
    print('The smallest p-value is for sqft')
    

data = pd.read_csv('sacramento.csv')
main(data)

