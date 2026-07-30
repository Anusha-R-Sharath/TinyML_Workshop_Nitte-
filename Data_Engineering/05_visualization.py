import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../Datasets/dataset.csv")

#plot accelerometer signals
plt.figure(figsize=(12,5))
plt.plot(df["Ax"],label="ax")
plt.plot(df["Ay"],label="ay")
plt.plot(df["Az"],label="az")

plt.title("Accelerometer Signals")
plt.xlabel("Sample Number")
plt.ylabel("Acceleration (g)")
plt.legend()
plt.grid(True)
plt.show()