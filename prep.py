import pandas as pd

import acquire

def acquire_and_prep_data():
    zillow = acquire.get_data()

    zillow = zillow.drop_duplicates()
    zillow = zillow.dropna()
    zillow = zillow.drop(columns='fips')
    zillow.bedroomcnt = zillow.bedroomcnt.astype('int')
    zillow = zillow.rename(columns={'calculatedfinishedsquarefeet': 'squarefeet', 'Name': 'County'})

    return zillow