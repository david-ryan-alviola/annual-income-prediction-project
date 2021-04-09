import env
import pandas as pd

def acquire_census_df():
    census_df = pd.read_csv(env.data_path + '/census/census-income.data', delimiter=',', header=None)
    census_test_df = pd.read_csv(env.data_path + '/census/census-income.test', delimiter=',', header=None)
    
    return pd.concat([census_df, census_test_df])