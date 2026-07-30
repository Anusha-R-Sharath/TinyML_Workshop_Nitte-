import pandas as pd

# Load the dataset
df = pd.read_csv("../Datasets/dataset.csv")

#check missing values
print(df.isnull().sum())

#Total missing values
print("\n Total Missing Values:", df.isnull().sum().sum())