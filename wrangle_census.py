import env

from acquire_census.acquire import acquire_census_df
from prepare_census.prepare import prepare_census_df

def wrangle_census_df():
    census_df = acquire_census_df()
    
    return prepare_census_df(census_df)