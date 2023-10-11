"""
in this file i want to prepare the data for easier analysis

will do first for only the atl data and then just impement it into a for loop
over all the teams



team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']

seasons = [str(season) for season in range(2010,2023)]
"""

import numpy as np
import pandas as pd

team_abbrs = ['crd', 'atl', 'rav', 'buf',
              'car', 'chi', 'cin', 'cle',
              'dal', 'den', 'det', 'gnb',
              'htx', 'clt', 'jax', 'kan',
              'sdg', 'ram', 'rai', 'mia',
              'min', 'nwe', 'nor', 'nyg',
              'nyj', 'phi', 'pit', 'sea',
              'sfo', 'tam', 'oti', 'was']


# for loop over every team
for team in team_abbrs:

    df = pd.read_csv('teams/' + team + '/' + team + '_2010_2023_gamelogs.csv')

    # delete unnecessary columns
    df.drop(['Unnamed: 0', 'Unnamed: 3', 'Week.1', 'Day.1', 'Date.1', 'Unnamed: 3.1', 'Unnamed: 4.1',
                'OT.1', 'Unnamed: 6.1', 'Opp.2', 'Tm.1', 'Opp.1.1', 'FGM.1', 'FGA.1', 'XPM.1', 'XPA.1',
                'Pnt.1', 'Yds.3.1'], axis=1, inplace=True)

    # rename the columns
    df.rename(columns={'Team': 'Tm_abb', 'Unnamed: 4': 'W/L', 'Unnamed: 6': 'H/A', 'Opp': 'Opp_abb',
                        'Tm': 'Tm_score', 'Opp.1': 'Opp_score', 'Cmp': 'O_P_Cmp', 'Att': 'O_P_Att',
                        'Yds': 'O_P_Yds', 'TD': 'O_P_TD', 'Int': 'O_Int', 'Sk': 'O_Sk', 'Yds.1': 'O_Yds_lost_Sk',
                        'Y/A': 'O_P_Y/A', 'NY/A': 'O_P_NY/A', 'Cmp%': 'O_P_Cmp_pct', 'Rate': 'O_QBR', 'Att.1': 'O_R_Att',
                        'Yds.2': 'O_R_Yds', 'Y/A.1': 'O_R_Y/A', 'TD.1': 'O_R_TD', 'Yds.3': 'Pnt_Yds',
                        '3DConv': 'O_3D_Conv', '3DAtt': 'O_3D_Att', '4DConv': 'O_4D_Conv', '4DAtt': 'O_4D_Att', 'ToP': 'O_ToP',
                        'Cmp.1': 'D_P_Cmp', 'Att.2': 'D_P_Att', 'Yds.4': 'D_P_Yds', 'TD.2': 'D_P_TD', 'Int.1': 'D_Int', 'Sk.1': 'D_Sk',
                        'Yds.1.1': 'D_Yds_lost_Sk', 'Y/A.2': 'D_P_Y/A', 'NY/A.1': 'D_P_NY/A', 'Cmp%.1': 'D_P_Cmp_pct', 'Rate.1': 'D_QBR',
                        'Att.1.1': 'D_R_Att', 'Yds.2.1': 'D_R_Yds', 'Y/A.1.1': 'D_R_Y/A', 'TD.1.1': 'D_R_TD',
                        '3DConv.1': 'D_3D_Conv', '3DAtt.1': 'D_3D_Att', '4DConv.1': 'D_4D_Conv', '4DAtt.1': 'D_4D_Att', 'ToP.1': 'D_ToP',}, inplace=True)

    # want to change the opponents name to it's abbreviation
    df.loc[df['Opp_abb'] == 'Pittsburgh Steelers', 'Opp_abb'] = 'PIT'
    df.loc[df['Opp_abb'] == 'Arizona Cardinals', 'Opp_abb'] = 'CRD'
    df.loc[df['Opp_abb'] == 'New Orleans Saints', 'Opp_abb'] = 'NOR'
    df.loc[df['Opp_abb'] == 'San Francisco 49ers', 'Opp_abb'] = 'SFO'
    df.loc[df['Opp_abb'] == 'Cleveland Browns', 'Opp_abb'] = 'CLE'
    df.loc[df['Opp_abb'] == 'Baltimore Ravens', 'Opp_abb'] = 'RAV'
    df.loc[df['Opp_abb'] == 'Tampa Bay Buccaneers', 'Opp_abb'] = 'TAM'
    df.loc[df['Opp_abb'] == 'Kansas City Chiefs', 'Opp_abb'] = 'KAN'
    df.loc[df['Opp_abb'] == 'Carolina Panthers', 'Opp_abb'] = 'CAR'
    df.loc[df['Opp_abb'] == 'Philadelphia Eagles', 'Opp_abb'] = 'PHI'
    df.loc[df['Opp_abb'] == 'Seattle Seahawks', 'Opp_abb'] = 'SEA'
    df.loc[df['Opp_abb'] == 'Minnesota Vikings', 'Opp_abb'] = 'MIN'
    df.loc[df['Opp_abb'] == 'New England Patriots', 'Opp_abb'] = 'NWE'
    df.loc[df['Opp_abb'] == 'Denver Broncos', 'Opp_abb'] = 'DEN'
    df.loc[df['Opp_abb'] == 'Atlanta Falcons', 'Opp_abb'] = 'ATL'
    df.loc[df['Opp_abb'] == 'Buffalo Bills', 'Opp_abb'] = 'BUF'
    df.loc[df['Opp_abb'] == 'Cincinnati Bengals', 'Opp_abb'] = 'CIN'
    df.loc[df['Opp_abb'] == 'New York Jets', 'Opp_abb'] = 'NYJ'
    df.loc[df['Opp_abb'] == 'Detroit Lions', 'Opp_abb'] = 'DET'
    df.loc[df['Opp_abb'] == 'Chicago Bears', 'Opp_abb'] = 'CHI'
    df.loc[df['Opp_abb'] == 'Houston Texans', 'Opp_abb'] = 'HTX'
    df.loc[df['Opp_abb'] == 'Green Bay Packers', 'Opp_abb'] = 'GNB'
    df.loc[df['Opp_abb'] == 'Miami Dolphins', 'Opp_abb'] = 'MIA'
    df.loc[df['Opp_abb'] == 'Jacksonville Jaguars', 'Opp_abb'] = 'JAX'
    df.loc[df['Opp_abb'] == 'Dallas Cowboys', 'Opp_abb'] = 'DAL'
    df.loc[df['Opp_abb'] == 'Tennessee Titans', 'Opp_abb'] = 'OTI'
    df.loc[df['Opp_abb'] == 'Indianapolis Colts', 'Opp_abb'] = 'CLT'
    df.loc[df['Opp_abb'] == 'New York Giants', 'Opp_abb'] = 'NYG'
    df.loc[df['Opp_abb'] == 'Washington Commanders', 'Opp_abb'] = 'WAS'
    df.loc[df['Opp_abb'] == 'Washington Redskins', 'Opp_abb'] = 'WAS'
    df.loc[df['Opp_abb'] == 'Washington Football Team', 'Opp_abb'] = 'WAS'
    df.loc[df['Opp_abb'] == 'Los Angeles Chargers', 'Opp_abb'] = 'SDG'
    df.loc[df['Opp_abb'] == 'San Diego Chargers', 'Opp_abb'] = 'SDG'
    df.loc[df['Opp_abb'] == 'Las Vegas Raiders', 'Opp_abb'] = 'RAI'
    df.loc[df['Opp_abb'] == 'Oakland Raiders', 'Opp_abb'] = 'RAI'
    df.loc[df['Opp_abb'] == 'Los Angeles Rams', 'Opp_abb'] = 'RAM'
    df.loc[df['Opp_abb'] == 'St. Louis Rams', 'Opp_abb'] = 'RAM'

    df.loc[df['OT'] == 'OT', 'OT'] = 'Y'
    df.loc[df['H/A'] == '@', 'H/A'] = 'A'
    df['OT'] = df['OT'].fillna('N')
    df['H/A'] = df['H/A'].fillna('H')
    
    df.to_csv('teams/' + team + '/' + team + '_2010_2023_gamelogs.csv')


# print(atl_df.sum(axis=0, numeric_only=True))