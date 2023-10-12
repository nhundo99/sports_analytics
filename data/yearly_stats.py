"""
In this file i to create yearly stats for each year for each team
"""

import pandas as pd
import numpy as np

# season
seasons = [str(season) for season in range(2010,2023)]

# team abbreviations
team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']

df = pd.read_csv('teams/atl/atl_2010_2023_gamelogs.csv')

# Create new dataframe with columns
df_yearly = pd.DataFrame(columns=['Season', 'Tm_abb', 'Games', 'Wins', 'Losses', 'Win_Pct', 'Points_Scored', 'Points_allowed',
                                  'O_P_Cmp', 'O_P_ATT', 'O_P_Yds', 'O_P_TD', 'O_Int', 'O_Sk' 'O_Yds_lost_Sk', 'O_P_Y/A',
                                  'O_P_NY/A', 'O_P_Cmp_pct', 'O_R_Att', 'O_R_Yds', 'O_R_Y/A', 'O_R_TD',
                                  'FGM', 'FGA', 'XPM', 'XPA', 'Pnt', 'Pnt_Yds', 'O_3D_Conv', 'O_3D_Att',
                                  'O_4D_Conv', 'O_4D_Att', 'D_P_Cmp', 'D_P_Att', 'D_P_Yds',
                                  'D_P_TD', 'D_Int', 'D_Sk', 'D_Yds_lost_Sk', 'D_P_Y/A', 'D_P_NY/A',
                                  'D_P_Cmp_pct', 'D_QBR', 'D_R_Att', 'D_R_Yds', 'D_R_Y/A', 'D_R_TD',
                                  'D_3D_Conv', 'D_3D_Att', 'D_4D_Conv', 'D_4D_Att', 'D_ToP'])

# we now want to iterate over all the seasons to compute the seasonal values
df_season = df.loc[df['Season'] == 2010]

# figure out best way to do this part
# we have to index column AND ROW for the yearly dataframe, now we only have column
"""
for season in range(2010,2023):
    # df_season = df.loc[df['Season'] == season]
    df_yearly['Season'] = season
    df_yearly['Tm_abb'] = 'ATL' # adjust to loop over team abbs
    df_yearly['Wins'] = len(df_season.loc[df_season['W/L'] == 'W'])
    df_yearly['Losses'] = len(df_season.loc[df_season['W/L'] == 'L'])
    df_yearly['Games'] = df_yearly.loc[season-2010, 'Wins'] + df_yearly.loc[season-2010, 'Losses']
    df_yearly['Win_Pct'] = df_yearly.loc[season-2010, 'Games'] / df_yearly.loc[season-2010, 'Wins'] * 100
    df_yearly['Points_Scored'] = df_season['Tm_score'].sum()
    df_yearly['Points_allowed'] = df_season['Opp_score'].sum()
    df_yearly['O_P_Cmp'] = df_season['O_P_Cmp'].sum()
    df_yearly['O_P_Att'] = df_season['O_P_Att'].sum()
    df_yearly['O_P_Yds'] = df_season['O_P_Yds'].sum()
    df_yearly['O_P_TD'] = df_season['O_P_TD'].sum()
    df_yearly['O_Int'] = df_season['O_Int'].sum()
    df_yearly['O_Sk'] = df_season['O_Sk'].sum()
    df_yearly['O_Yds_lost_Sk'] = df_season['O_Yds_lost_Sk'].sum()
    df_yearly['O_P_Y/A'] = df_yearly.loc[season-2010, 'O_P_Yds'] / df_yearly.loc[season-2010, 'O_P_Att']
    df_yearly['O_P_NY/A'] = (df_yearly.loc[season-2010, 'O_P_Yds'] - )
    df_yearly['']
    df_yearly['']
    df_yearly['']
    df_yearly['']
"""

for col in df_season.columns:
    print(col)

print(df_season['Tm_score'].sum())