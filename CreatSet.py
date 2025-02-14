
import pandas as pd

# read csv file
df = pd.read_csv("dictionnaire_fr.csv",header=None )

# transforme csv file to set
french_words = set(df[0])

# test complete



