import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Filter the data for the "versicolor" species
versicolor_df = df[df["species"] == "versicolor"]
setosa_df=df[df["species"] == "setosa"]
virginica_df=df[df["species"] == "virginica"]

# Extract data
plen = df['petal_length']
pwidth = df['petal_width']
slen = df['sepal_length']
swidth = df['sepal_width']

# Fit a straight line between petal length and petal width
# m1, c1 = np.polyfit(plen, pwidth, 1)

# Fit a straight line between sepal length and sepal width
# m2, c2 = np.polyfit(slen, swidth, 1)

# Create subplots
# This is how i will code how i want the histograms to appear.
fig, ax = plt.subplots(2,3)
fig.suptitle("Histogram of Petal Length (cm) subdivided by iris species", color='orange')
#fig.title('Histogram of the petal lenght (cm) for each species')

# Lets start some work on each individual plot
# Plot 1- Veriscolor (Petal Length)
ax[0,0].hist(versicolor_df["petal_length"], bins=10, color="blue", edgecolor='black')
ax[0,0].set_xlabel('Petal Length (cm)')
ax[0,0].set_ylabel('Frequency')
ax[0,0].set_title('Versicolor')

# No limits are set, as this will skew the visual representation of the data.

# Plot 2- Setosa (Petal Length)
ax[0,1].hist(setosa_df["petal_length"], bins=10, color="red", edgecolor='black')
ax[0,1].set_xlabel('Petal Length (cm)')
ax[0,1].set_title('Setosa')

# Plot 3- Virginica (Petal Length)
ax[0,2].hist(virginica_df["petal_length"], bins=10, color="green", edgecolor='black')
ax[0,2].set_xlabel('Petal Length (cm)')
ax[0,2].set_title('Virginica')

# Plot 4- Veriscolor (Petal Width)
ax[1,0].hist(versicolor_df["petal_width"], bins=10, color="blue", edgecolor='black')
ax[1,0].set_xlabel('Petal Width (cm)')
ax[1,0].set_ylabel('Frequency')
ax[1,0].set_title('Versicolor')

# Plot 5- Setosa (Petal Width)
ax[1,1].hist(setosa_df["petal_width"], bins=10, color="red", edgecolor='black')
ax[1,1].set_xlabel('Petal Width (cm)')
ax[1,1].set_title('Setosa')

# Plot 6- Virginica (Petal Width)
ax[1,2].hist(virginica_df["petal_width"], bins=10, color="green", edgecolor='black')
ax[1,2].set_xlabel('Petal Width (cm)')
ax[1,2].set_title('Virginica')


# Adjust spacing between subplots
# Reference: https://www.geeksforgeeks.org/how-to-set-the-spacing-between-subplots-in-matplotlib-in-python/
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()