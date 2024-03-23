import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Filter the data for the "versicolor" species
versicolor_df = df[df["species"] == "versicolor"]

# Create a histogram of petal length for the "versicolor" species
plt.figure(figsize=(8, 6))
sns.histplot(versicolor_df["petal_length"], bins=10, kde=True, color="blue")
plt.title("Histogram of Petal Length (Versicolor)")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.legend()
plt.show()