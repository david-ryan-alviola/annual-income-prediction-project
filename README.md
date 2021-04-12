# Predicting total income with mostly categorical data proves to be a lofty goal
I created a regression model to predict total annual income for hourly workers based on census data and features engineered from clustering. This is an expansion of the original research that was used to create a classification model that predicted whether or not an individual made over 50_000 dollars a year.

## Goals

## Setup this project
* Dependencies
    1. [utilities.py](https://github.com/david-ryan-alviola/utilities/releases)
        * Use release 2.5.1 or greater
    2. python
    3. pandas
    4. scipy
    5. sklearn
    6. numpy
    7. matplotlib.pyplot
    8. seaborn
    9. [census data set](https://archive.ics.uci.edu/ml/machine-learning-databases/census-income-mld/census.tar.gz)
* Steps to recreate
    1. Clone this repository
    2. Install `utilities.py` according to the instructions
    3. Setup env.py
        * Remove the .dist extension (should result in `env.py`)
        * Fill in your user_name, password, and host
        * If you did not install `utilities.py` in your cloned repository, replace the "/path/to/utilities" string with the path to where `utilities.py` is installed
    4. Download the data set and unzip
        * Add a `data_path` variable to your `env.py` and set it to the directory where you unzipped the data
    5. Open `predicting_income.ipynb` and run the cells

## Key Findings
1. I was able to increase the explained variance score from 0% to 18%
    * Explained variance increased from 12% to 18% between iterations
2. Age had a .14 correlation with total annual income
    * Clusters also appeared to be along divisions in age
3. The data and my modeling method may not best suited for the problem I wanted to tackle

## The plan
The Kanban board used for planning is [here](https://github.com/david-ryan-alviola/individual-project/projects/1).

The original research that this data was used for was to create a classification model that predicted whether or not an individual made less than 50_000 USD or not. I wanted to expand on this and set the lofty goal of using the data to create a regression model that would use features made from clusters to predict total annual income.

After scanning the data, I wanted to explore these hypotheses:
1. Does private or public affect income?
2. Does sex affect income?
3. Does race affect income?
4. Which occupation makes the most on average?
5. Does belonging to a union affect income?
6. Does having investments affect income?
    * I needed to make new feature since I could not factor in the figures directly
7. Does being married affect total annual income?
8. Does age correlate with total annual income?
9. Does education affect total income?
    * This was done on the second iteration
    
I planned to only use features that were already in the data set and not scale for the first iteration of the model. The second iteration would have engineered features, be scaled, and utilize clusters. I would then select the best perfoming regression model to apply to the test data and evaluate its performance.


## Data Dictionary
This is the structure of the data for the second model:
#### Target
Name | Description | Type
:---: | :---: | :---:
total_annual_income | Calculated by multiplying the hourly wage by 40 hrs and by 52 weeks | float
#### Features
Name | Description | Type
:---: | :---: | :---:
is_married | Indicates if worker is married or not | int
age | Age in years | float
30_40_yr_post_grad | Indicates if a 30-40 yr old post graduate | int
30_50_yr_high_school_grad | Indicates if 30-50 yr high school graduate | int
50_plus_high_school_grad | Indicates if 50 yr plus high school graduate | int
20_30_yr_high_school_grad | Indicates if 20-30 yr high school graduate | int
college_grad | Indicates if a college graduate | int
40_plus_post_grad | Indicates if a 40 yr plus post graduate | int
30_40_yr_no_investments | Indicates if 30-40 yr with no investments | int
40_plus_has_investments | Indicates if 40 plus yr with investments | int
50_plus_no_investments | Indicates if 50 yr plus with no investments | int
40_50_yr_no_investments | Indicates if 40-50 yr with no investments | int
20_30_yr_no_investments | Indicates if 20-30 yr with no investments | int
20_40_yr_has_investments | Indicates if 20-40 yr with investments | int
30_40_yr_private | Indicates if 30-40 yr private worker | int
40_plus_public | Indicates if 40 yr plus public worker | int
50_plus_private | Indicates if 50 yr plus private worker | int
20_40_yr_public | Indicates if 20-40 yr public worker | int
20_30_yr_private | Indicates if 20-30 yr private worker | int
40_50_yr_private | Indicates if 40-50 yr private worker | int
20_30_yr_white | Indicates if 20-30 yr caucasian | int
40_55_yr_white | Indicates if 40-55 yr caucasian | int
20_40_yr_not_white | Indicates if 20-40 yr non-caucasian | int
40_plus_not_white | Indicates if 40 yr plus non-caucasian | int
55_plus_white | Indicates if 55 yr plus caucasian | int
30_40_yr_white | Indicates if 30-40 yr caucasian | int
30_40_yr_non_union | Indicates if 30-40 yr non-union worker | int
20_40_yr_union | Indicates if 20-40 yr union worker | int
50_plus_non_union | Indicates if 50 yr plus non-union worker | int
20_30_yr_non_union | Indicates if 20-30 yr non-union worker | int
40_50_yr_non_union | Indicates if 40-50 yr non-union worker | int
40_plus_union | Indicates if 40 yr plus union worker | int
#### Other data
Name | Description | Type
:---: | :---: | :---:
worker_class | Describes if worker is in private or some level of govt work | string
education | Describes level of education | string
hourly_wage | Amount made per hour in US dollars | float
marital_status | Describes if worker is married or single, etc | string
major_industry_code | Describes the industry of the worker | string
major_occupation_code | Describes the job of the worker| string
race | Describes the race of the worker | string
of_hispanic_origin | Describes worker's Hispanic origins, if any | string
sex | Male or Female | string
is_union_member | Indicates if worker belongs to a union | int
capital_gains | Amount of gains from investments | float
capital_losses | Amount of losses from investments | float
total_dividends | Amount of dividends from investments | float
household_summary | Describes workers home situation | string
company_size | Size of company | int
country_of_father | Home country of birth father | string
country_of_mother | Home country of birth mother | string
birth_country | Worker's birth country | string
citizenship | Citizenship of worker | string
is_self_employed | Indicates if worker is self-employed | int
weeks_worked | Number of weeks worked in a year | int
year | Indicates if year data was recorded was 94 or 95 | int
has_investments | Indicates if worker has investments by summing gains, losses, and dividends. 1 if sum is non-zero; 0 otherwise | int
is_public | Indicates if worker is in government work | int
Male | Indicates if worker is male | int
White | Indicates if worker is white | int
belongs_to_union | Indicates if worker belongs to a union | int
is_college_grad | Indicates if worker is a college graduate | int
is_high_school_grad | Indicates if worker is a high school graduate | int
is_post_grad | Indicates if worker is a post graduates | int
not_high_school_grad | Indicates if worker did not graduate high school | int

## Results
I applied the gradient boosting regressor model to the test data and got an explained variance score of 18%. This amount is the same as the model got on the training sample!

## Recommendations
1. Bin the different incomes into ranges and use a classification model to predict which range
    * This is still an improvement over the original research model that only predicted under 50_000 or not
2. Incorporate industry and occupation data into clusters
3. Most of the incomes seem to be under 75_000, so try to create a model for only those incomes
