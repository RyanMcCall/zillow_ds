import env
import pandas as pd
from os import path

def get_url(database):
    '''
    database: string; name of database that the url is being created for
    '''
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

def label_county(row):
    if row['fips'] == 6037:
        return 'Los Angeles'
    elif row['fips'] == 6059:
        return 'Orange'
    elif row['fips'] == 6111:
        return 'Ventura'

def get_data():
    if not path.isfile("zillow.csv"):
        query = '''
        SELECT p.id, p.bathroomcnt, p.bedroomcnt, p.calculatedfinishedsquarefeet, p.fips, p.fullbathcnt, p.latitude, p.longitude, p.roomcnt, p.yearbuilt, p.taxvaluedollarcnt, ROUND((p.taxamount / p.taxvaluedollarcnt) * 100, 2) AS taxrate
        FROM properties_2017 AS p
        JOIN predictions_2017 AS pr USING (parcelid)
        WHERE p.propertylandusetypeid IN (261, 262, 263, 264, 266, 268, 273, 276, 279)
        AND pr.transactiondate BETWEEN "2017-05-01" AND '2017-06-30';
        '''

        url = get_url('zillow')

        zillow = pd.read_sql(query, url, index_col='id')

        zillow.to_csv('zillow.csv')
        
    zillow = pd.read_csv('zillow.csv')

    zillow['County'] = zillow.apply(lambda row: label_county(row), axis=1)

    zillow['State'] = 'CA'

    return zillow