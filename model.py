import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.formula.api import ols

import math

import prep

def get_model():
    zillow = prep.acquire_and_prep_data()
    zillow = zillow.drop(columns=['id', 'calculatedbathnbr', 'taxrate', 'County', 'State'])

    zillow['sqft_per_bed_and_bath'] = zillow.squarefeet / (zillow.bathroomcnt + zillow.bedroomcnt)

    train, test = train_test_split(zillow, train_size=.7, random_state=13)
    Xtrain = train.drop(columns='taxvaluedollarcnt')
    ytrain = train.taxvaluedollarcnt

    X = train[['squarefeet', 'bedroomcnt', 'sqft_per_bed_and_bath']]
    y = ytrain

    lm = LinearRegression()
    return lm.fit(X, y)

def make_predictions(linear_model, target, features):
    predictions = pd.DataFrame(target)
    predictions['baseline'] = target.mean()
    predictions['model_predictions'] = linear_model.predict(features)

    return predictions

def evaluate_model(prediction_df):
    baseline_RMSE = math.sqrt(mean_squared_error(prediction_df.taxvaluedollarcnt, prediction_df.baseline))
    model_RMSE = math.sqrt(mean_squared_error(prediction_df.taxvaluedollarcnt, prediction_df.model_predictions))

    print(f'Baseline RMSE: {baseline_RMSE}')
    print(f'Baseline RMSE: {model_RMSE}')

    if baseline_RMSE > model_RMSE:
        print('Model is better than baseline')
    else:
        print('Baseline is better than model')


    
