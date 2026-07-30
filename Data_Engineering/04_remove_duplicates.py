import pandas as pd

# Load the dataset
df = pd.read_csv("../Datasets/dataset.csv")

# Count duplicate rows
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

#Remove duplicates
df = df.drop_duplicates()

#verify dataset
print("New Shape:", df.shape)