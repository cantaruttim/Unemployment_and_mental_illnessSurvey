import pandas as pd
import numpy as np


# reading documents csv files
df = pd.read_csv('./CSV/CollectorList.csv')
display(df)

mentalIlness = pd.read_csv('./CSV/Mental Illness Survey 1.csv')
display(mentalIlness)

# Cleaning data

mentalIlness = mentalIlness.drop(['IP Address', 'Email Address', 'First Name', 'Last Name'], axis=1) # drop that coluns in Nan
display(mentalIlness.iloc[[0]]) # seleciona a linha de índice 0

mentalIlness = mentalIlness.rename(columns=df.iloc[0]).loc[1:] # iniciando o df no indice 1

display(mentalIlness)
