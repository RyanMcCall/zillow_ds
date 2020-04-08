import env
import pandas as pd

def get_url(database):
    '''
    database: string; name of database that the url is being created for
    '''
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

def get_data():
    zillow = pd.read_csv('zillow.csv')
    FIPS = pd.read_csv('fips.csv')
    zillow = zillow.merge(FIPS, left_on='fips', right_on='FIPS')
    return zillow