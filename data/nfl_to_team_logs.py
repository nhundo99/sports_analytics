"""
in this file i want to extract the data from the nfl_gamelogs_2010_2023.csv file for each team
and make it's own .csv file
"""

import numpy as np
import pandas as pd


# first we have to convert the csv file to a DataFrame
nfl_df = pd.read_csv('nfl_gamelogs_2010_2023.csv')
print(nfl_df)

# find out what types are used in the dataframe 
print(nfl_df.dtypes)

# list of team abbreviations
team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']

# iterate through all the teams
for team in team_abbrs:
    # make team dataframe
    team_df = nfl_df[nfl_df['Team'] == team.upper()]

    # save the team dataframe as a csv file in the given folder
    team_df.to_csv('teams/' + team + '/' + team + '_2010_2023_gamelogs.csv')


