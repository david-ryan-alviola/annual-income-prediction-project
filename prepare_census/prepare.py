import env
import pandas as pd

_column_name_dictionary = {0 : 'age', 1 : 'worker_class', 2 : 'drop', 3 : 'drop', 4 : 'education',\
                         5 : 'hourly_wage', 6 : 'drop', 7 : 'marital_status', 8 : 'major_industry_code',\
                         9 : 'major_occupation_code', 10 : 'race', 11 : 'of_hispanic_origin', 12 : 'sex', 13 : 'is_union_member',\
                         14 : 'drop', 15 : 'drop', 16 : 'capital_gains', 17 : 'capital_losses',\
                         18 : 'total_dividends', 19 : 'drop', 20 : 'drop', 21 : 'drop', 22 : 'drop',\
                         23 : 'household_summary', 24 : 'drop', 25 : 'drop', 26 : 'drop', 27 : 'drop',\
                         28 : 'drop', 29 : 'drop', 30 : 'company_size', 31 : 'drop',\
                         32 : 'country_of_father', 33 : 'country_of_mother', 34 : 'birth_country', 35 : 'citizenship',\
                         36 : 'is_self_employed', 37 : 'drop', 38 : 'drop', 39 : 'weeks_worked', 40 : 'year', 41 : 'drop'}

_string_cols = ['worker_class', 'education', 'marital_status', 'major_industry_code', 'major_occupation_code',\
              'race', 'of_hispanic_origin', 'sex', 'is_union_member', 'household_summary', 'country_of_father', 'country_of_mother',\
                'birth_country', 'citizenship']

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
    census_df = _engineer_features(census_df)
    
    return _encode_categorical_variables(census_df)

def _engineer_features(df):
    census_df = df.copy()
    
    # Standard 40 hour work week for 52 weeks
    census_df['total_annual_income'] = (census_df.hourly_wage * 40 * 52) + census_df.total_dividends \
    + census_df.capital_gains - census_df.capital_losses
    
    census_df['is_married'] = census_df.marital_status.apply\
    (lambda status : 1 if "spouse_present" in status else 0)
    
    census_df['has_investments'] = census_df[['capital_gains', 'capital_losses', 'total_dividends']]\
    .sum(axis=1)
    census_df['has_investments'] = census_df.has_investments.apply(lambda net : 1 if net != 0 else 0)
    
    census_df.education = census_df.education.apply(_simplify_education)
    census_df.worker_class = census_df.worker_class.apply(_simplify_class)
    
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
        df[col] = df[col].str.strip().str.replace(" ", "_")
        
    return df

def _drop_duplicate_rows(df):
    census_df = df.copy()
    
    dupes = census_df[census_df.index.value_counts() > 1]
    census_df.drop(index=dupes.index, inplace=True)
    
    return census_df

def _simplify_education(education_level):
    if "High_school_graduate" in education_level or "Some_college_but_no_degree" in education_level:
        return "is_high_school_grad"
    elif "Bachelors" in education_level or "Associates" in education_level:
        return "is_college_grad"
    elif "Masters" in education_level or "Prof" in education_level or "Doctorate" in education_level:
        return "is_post_grad"
    else:
        return "not_high_school_grad"
    
def _simplify_class(worker_class):
    if "government" in worker_class:
        return "is_public"
    else:
        return "is_private"
    
def _encode_categorical_variables(df):
    df = df.copy()
    
    class_dummies = pd.get_dummies(df.worker_class, drop_first=True)
    sex_dummies = pd.get_dummies(df.sex, drop_first=True)
    
    race_dummies = pd.get_dummies(df.race, drop_first=False)
    race_dummies.drop(columns=['Amer_Indian_Aleut_or_Eskimo', 'Asian_or_Pacific_Islander', 'Black', 'Other'], inplace=True)
    
    union_dummies = pd.get_dummies(df.is_union_member, drop_first=True)
    union_dummies.rename(columns={'Yes' : 'belongs_to_union'}, inplace=True)
    
    education_dummies = pd.get_dummies(df.education, drop_first=False)
    
    return pd.concat([df, class_dummies, sex_dummies, race_dummies, union_dummies, education_dummies], axis=1)

