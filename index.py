import pandas as pd
import numpy as np


# reading documents csv files
df = pd.read_csv('./CSV/CollectorList.csv')
display(df)

mentalIlness = pd.read_csv('./CSV/Mental Illness Survey 1.csv')
display(mentalIlness)

mentalIlness.head(10)

