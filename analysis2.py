# This is an code analysis of the Fisher Iris Data set. 
# More detail is available in the README and accompanying Jupyternotebook.
# Author: Laura Lyons

# Import the libraries necessary for the analysis.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Filter the data by the species.
versicolor_df = df[df["species"] == "versicolor"]
setosa_df=df[df["species"] == "setosa"]
virginica_df=df[df["species"] == "virginica"]

# Create a figure containing a subplot for all the variables, subdivided by iris species using subplots.
fig, ax = plt.subplots(4,3, figsize=(15, 15))
fig.suptitle("Histogram of Petal Length (cm),subdivided by iris species", color='orange',fontweight='bold', fontsize=14)
plt.rc('font', size=10)        # Controls default text size
plt.rc('axes', labelsize=10)   # Font size of the x and y labels

# Lets highlight the main title by changing the text colour to orange and making bold (as above).

# Lets start some work on each individual plot
# Plot 1- Veriscolor (Petal Length)
ax[0,0].hist(versicolor_df["petal_length"], bins=10, color="blue", edgecolor='black')
ax[0,0].set_xlabel('Petal Length (cm)')
ax[0,0].set_ylabel('Frequency')
ax[0,0].set_title('Versicolor', fontweight='bold')
# No limits are set, as this will skew the visual representation of the data.

# Plot 2- Setosa (Petal Length)
ax[0,1].hist(setosa_df["petal_length"], bins=10, color="red", edgecolor='black')
ax[0,1].set_xlabel('Petal Length (cm)')
ax[0,1].set_title('Setosa', fontweight='bold')

# Plot 3- Virginica (Petal Length)
ax[0,2].hist(virginica_df["petal_length"], bins=10, color="green", edgecolor='black')
ax[0,2].set_xlabel('Petal Length (cm)')
ax[0,2].set_title('Virginica', fontweight='bold')

# Let add a second grow to this plot, Petal Width (cm)
# Plot 4- Veriscolor (Petal Width)
ax[1,0].hist(versicolor_df["petal_width"], bins=10, color="blue", edgecolor='black')
ax[1,0].set_xlabel('Petal Width (cm)')
ax[1,0].set_ylabel('Frequency')
# After looking at the graph, I removed the species title as it over crowded the graph.

# Plot 5- Setosa (Petal Width)
ax[1,1].hist(setosa_df["petal_width"], bins=10, color="red", edgecolor='black')
ax[1,1].set_xlabel('Petal Width (cm)')

# Plot 6- Virginica (Petal Width)
ax[1,2].hist(virginica_df["petal_width"], bins=10, color="green", edgecolor='black')
ax[1,2].set_xlabel('Petal Width (cm)')

# Plot 7- Veriscolor (Sepal Length)
ax[2,0].hist(versicolor_df["sepal_length"], bins=10, color="blue", edgecolor='black')
ax[2,0].set_xlabel('Sepal Length (cm)')
ax[2,0].set_ylabel('Frequency')

# Plot 8- Setosa (Sepal Length)
ax[2,1].hist(setosa_df["sepal_length"], bins=10, color="red", edgecolor='black')
ax[2,1].set_xlabel('Sepal Length (cm)')

# Plot 9- Virginica (Sepal Length)
ax[2,2].hist(virginica_df["sepal_length"], bins=10, color="green", edgecolor='black')
ax[2,2].set_xlabel('Sepal Length (cm)')

# Plot 10- Veriscolor (Sepal Width)
ax[3,0].hist(versicolor_df["sepal_width"], bins=10, color="blue", edgecolor='black')
ax[3,0].set_xlabel('Sepal Width (cm)')
ax[3,0].set_ylabel('Frequency')

# Plot 11- Setosa (Sepal Width)
ax[3,1].hist(setosa_df["sepal_width"], bins=10, color="red", edgecolor='black')
ax[3,1].set_xlabel('Sepal Width (cm)')

# Plot 12- Virginica (Sepal Width)
ax[3,2].hist(virginica_df["sepal_width"], bins=10, color="green", edgecolor='black')
ax[3,2].set_xlabel('Sepal Width (cm)')

# Adjust spacing between subplots
# Reference: https://www.geeksforgeeks.org/how-to-set-the-spacing-between-subplots-in-matplotlib-in-python/
# Reference: https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots
plt.subplots_adjust(top=0.905,bottom=0.136, left=0.097, right=0.970, wspace=0.239, hspace=0.910)
plt.show()
plt.savefig('Histogram of Petal Length (cm),subdivided by iris species.png')

# Extract data
plen = df['petal_length']
pwidth = df['petal_width']
slen = df['sepal_length']
swidth = df['sepal_width']

# Fit a straight line between petal length and petal width
# m1, c1 = np.polyfit(plen, pwidth, 1)

# Fit a straight line between sepal length and sepal width
# m2, c2 = np.polyfit(slen, swidth, 1)

# Lets get a summary of all the variables, subdivided by iris species.
summary_of_versicolor= versicolor_df.describe()

# Format the output as a table
formatted_summary_of_versicolor = summary_of_versicolor.to_markdown()
print(formatted_summary_of_versicolor)

# Print the formatted table
formatted_summary_of_versicolor.to_csv("Summary of Versicolor.txt", sep="\t", index=False)
print(" A summary of the variables according to the iris species.txt")