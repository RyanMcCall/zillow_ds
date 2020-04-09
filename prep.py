import pandas as pd

import acquire

def acquire_and_prep_data():
    zillow = acquire.get_data()

    zillow = zillow.drop_duplicates()
    zillow = zillow.dropna()
    zillow = zillow.drop(columns=['fips', 'roomcnt'])

    zillow.bedroomcnt = zillow.bedroomcnt.astype('int')
    zillow.calculatedfinishedsquarefeet = zillow.calculatedfinishedsquarefeet.astype('int')
    zillow.fullbathcnt = zillow.fullbathcnt.astype('int')
    zillow.yearbuilt = zillow.yearbuilt.astype('int')
    zillow.taxvaluedollarcnt = zillow.taxvaluedollarcnt.astype('int')

    zillow = zillow.rename(columns={'calculatedfinishedsquarefeet': 'squarefeet', 'Name': 'County'})
    
    zillow.latitude = zillow.latitude / 1000000
    zillow.longitude = zillow.longitude / 1000000

    return zillow