"""
This file is just to drop the indexing column in the teams data that was written with df.to_csv
"""

import pandas as pd

team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']

for team in team_abbrs:
    df = pd.read_csv('teams/' + team + '/' + team + '_2010_2023_gamelogs.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df.to_csv('teams/' + team + '/' + team + '_2010_2023_gamelogs.csv', index=False)