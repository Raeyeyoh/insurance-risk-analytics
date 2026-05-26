import pandas as pd

df = pd.read_csv("../data/insurance-data.csv", sep="|")

# remove duplicates
df = df.drop_duplicates()

# remove missing values
df = df.dropna()

# save cleaned version
df.to_csv(
    "../data/insurance-data-cleaned.csv",
    sep="|",
    index=False
)
