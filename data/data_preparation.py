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

atl_df = pd.read_csv('teams/atl/atl_2010_2023_gamelogs.csv')

# delete unnecessary columns
atl_df.drop(['Unnamed: 0', 'Unnamed: 3', 'Week.1', 'Day.1', 'Date.1', 'Unnamed: 3.1', 'Unnamed: 4.1',
             'OT.1', 'Unnamed: 6.1', 'Opp.2', 'Tm.1', 'Opp.1.1', 'FGM.1', 'FGA.1', 'XPM.1', 'XPA.1',
             'Pnt.1', 'Yds.3.1'], axis=1, inplace=True)

# rename the columns
atl_df.rename(columns={'Team': 'Tm_abb', 'Unnamed: 4': 'W/L', 'Unnamed: 6': 'H/A', 'Opp': 'Opp_abb',
                       'Tm': 'Tm_score', 'Opp.1': 'Opp_score', 'Cmp': 'O_P_Cmp', 'Att': 'O_P_Att',
                       'Yds': 'O_P_Yds', 'TD': 'O_P_TD', 'Int': 'O_Int', 'Sk': 'O_Sk', 'Yds.1': 'O_Yds_lost_Sk',
                       'Y/A': 'O_P_Y/A', 'NY/A': 'O_P_NY/A', 'Cmp%': 'O_P_Cmp_pct', 'Rate': 'O_QBR', 'Att.1': 'O_R_Att',
                       'Yds.2': 'O_R_Yds', 'Y/A.1': 'O_R_Y/A', 'TD.1': 'O_R_TD', 'Yds.3': 'Pnt_Yds',
                       '3DConv': 'O_3D_Conv', '3DAtt': 'O_3D_Att', '4DConv': 'O_4D_Conv', '4DAtt': 'O_4D_Att', 'ToP': 'O_ToP',
                       'Cmp.1': 'D_P_Cmp', 'Att.2': 'D_P_Att', 'Yds.4': 'D_P_Yds', 'TD.2': 'D_P_TD', 'Int.1': 'D_Int', 'Sk.1': 'D_Sk',
                       'Yds.1.1': 'D_Yds_lost_Sk', 'Y/A.2': 'D_P_Y/A', 'NY/A.1': 'D_P_NY/A', 'Cmp%.1': 'D_P_Cmp_pct', 'Rate.1': 'D_QBR',
                       'Att.1.1': 'D_R_Att', 'Yds.2.1': 'D_R_Yds', 'Y/A.1.1': 'D_R_Y/A', 'TD.1.1': 'D_R_TD',
                       '3DConv.1': 'D_3D_Conv', '3DAtt.1': 'D_3D_Att', '4DConv.1': 'D_4D_Conv', '4DAtt.1': 'D_4D_Att', 'ToP.1': 'D_ToP',}, inplace=True)

print(atl_df)

# print(atl_df.sum(axis=0, numeric_only=True))