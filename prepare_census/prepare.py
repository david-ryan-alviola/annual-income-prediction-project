import env

_column_name_dictionary = {0 : 'age', 1 : 'worker_class', 2 : 'drop_1', 3 : 'drop_2', 4 : 'education',\
                         5 : 'hourly_wage', 6 : 'highest_education', 7 : 'marital_status', 8 : 'major_industry_code',\
                         9 : 'major_occupation_code', 10 : 'race', 11 : 'of_hispanic_origin', 12 : 'sex', 13 : 'is_union_member',\
                         14 : 'unemployed_reason', 15 : 'employment_status', 16 : 'capital_gains', 17 : 'capital_losses',\
                         18 : 'total_dividends', 19 : 'tax_filer_status', 20 : 'region', 21 : 'state', 22 : 'family_status',\
                         23 : 'household_summary', 24 : 'drop_3', 25 : 'drop_4', 26 : 'drop_5', 27 : 'drop_6',\
                         28 : 'lived_in_house_last_year', 29 : 'drop_7', 30 : 'company_size', 31 : 'family_members_under_18',\
                         32 : 'country_of_father', 33 : 'country_of_mother', 34 : 'birth_country', 35 : 'citizenship',\
                         36 : 'is_self_employed', 37 : 'drop_8', 38 : 'drop_9', 39 : 'weeks_worked', 40 : 'year', 41 : 'drop_10'}

_string_cols = ['worker_class', 'education', 'highest_education', 'marital_status', 'major_industry_code', 'major_occupation_code',\
              'race', 'of_hispanic_origin', 'sex', 'is_union_member', 'unemployed_reason', 'employment_status', 'tax_filer_status',\
              'region', 'state', 'family_status', 'household_summary', 'lived_in_house_last_year', 'family_members_under_18',\
              'country_of_father', 'country_of_mother', 'birth_country', 'citizenship']

def prepare_census_df(df):
    census_df = df.copy()
    
    census_df.rename(columns=_column_name_dictionary, inplace=True)
    census_df.drop(columns=_generate_drop_column_list(census_df.columns), inplace=True)
    census_df = census_df[census_df.age >= 18]
    census_df = census_df[census_df.weeks_worked == 52]
    census_df.hourly_wage = census_df.hourly_wage / 100
    census_df = census_df[census_df.hourly_wage > 0]
    census_df = _strip_whitespace_from_values(census_df)
    census_df = _drop_duplicate_rows(census_df)
    
    # Standard 40 hour work week for 52 weeks
    census_df['total_annual_income'] = (census_df.hourly_wage * 40 * 52) + census_df.total_dividends \
    + census_df.capital_gains - census_df.capital_losses
    
    return census_df
    
def _generate_drop_column_list(columns):
    drop_cols = []
    
    for col in columns:
        if "drop" in col:
            drop_cols.append(col)
        
    return drop_cols

def _strip_whitespace_from_values(df):
    df = df.copy()
    
    for col in _string_cols:
        df[col] = df[col].str.strip()
        
    return df

def _drop_duplicate_rows(df):
    census_df = df.copy()
    
    dupes = census_df[census_df.index.value_counts() > 1]
    census_df.drop(index=dupes.index, inplace=True)
    
    return census_df

