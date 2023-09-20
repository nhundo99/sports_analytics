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


