import pandas as pd

df = pd.read_csv("../data/insurance-data.csv", sep="|")

df = df.drop_duplicates()

df = df.dropna()

df.to_csv(
    "data/insurance-data-cleaned.csv",
    sep="|",
    index=False
)
