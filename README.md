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
This is the structure of the data after preparation:
#### Target
Name | Description | Type
:---: | :---: | :---:

#### Features
Name | Description | Type
:---: | :---: | :---:

#### Other data
Name | Description | Type
:---: | :---: | :---:


## Results
I applied the gradient boosting regressor model to the test data and got an explained variance score of 18%. This amount is the same as the model got on the training sample!

## Recommendations
1. Bin the different incomes into ranges and use a classification model to predict which range
    * This is still an improvement over the original research model that only predicted under 50_000 or not
2. Incorporate industry and occupation data into clusters
3. Most of the incomes seem to be under 75_000, so try to create a model for only those incomes
