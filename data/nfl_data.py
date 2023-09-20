"""
In this python file I want to get Data from the Pro-Football-Reference site and export it into a CSV
file.
The CSV file will be used to analyze the data without having to do a request on the website everytime.
"""

# random and time is used to follow the rules from the website
import numpy as np
import pandas as pd
import random
import time

# list of seasons
seasons = [str(season) for season in range(2010,2023)]

# list of team abbreviations
team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']


# create a dataframe, later will be read into a csv
nfl_df = pd.DataFrame()

for season in seasons:
    for team in team_abbrs:
        url = 'https://www.pro-football-reference.com/teams/' + team + '/' + season + '/gamelog/'

        # biuld a team-stats dataframe from the offensive and defensive stats and complete it
        # with missing attributes
        off_df = pd.read_html(url, header=1, attrs={'id':'gamelog' + season})[0]
        def_df = pd.read_html(url, header=1, attrs={'id':'gamelog_opp' + season})[0]
        team_df = pd.concat([off_df, def_df], axis=1)
        team_df.insert(loc=0, column='Season', value=season)
        team_df.insert(loc=2, column='Team', value=team.upper())

        # add the team dataframe to the complete nfl dataframe
        nfl_df = pd.concat([nfl_df, team_df], ignore_index=True)

        # pause requests to follow the rules from sports-reference.com
        time.sleep(random.randint(4,5))
        print(nfl_df)

# save the datafram to s csv file
nfl_df.to_csv('nfl_gamelogs_2010_2023.csv', index=False)