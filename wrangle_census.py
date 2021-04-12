import env

from acquire_census.acquire import acquire_census_df
from prepare_census.prepare import prepare_census_df
from utilities import split_dataframe_continuous_target

def wrangle_census_df():
    census_df = acquire_census_df()
    census_df = prepare_census_df(census_df)
    
    return split_dataframe_continuous_target(census_df, 'total_annual_income')