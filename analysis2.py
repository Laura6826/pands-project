import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Filter the data for the "versicolor" species
versicolor_df = df[df["species"] == "versicolor"]
setosa_df=df[df["species"] == "setosa"]
virginica_df=df[df["species"] == "virginica"]
'''
# Create a histogram of petal length for the "versicolor" species
plt.figure(figsize=(8, 6))
sns.histplot(versicolor_df["petal_length"], bins=10, kde=True, color="blue")
plt.title("Histogram of Petal Length (Versicolor)")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()
'''

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
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.hist(versicolor_df["petal_length"], bins=10, color="blue")
ax1.set_xlabel('Petal Length (cm)')
ax1.set_ylabel('Frequency')
ax1.set_title('Histogram of Petal Length (Versicolor)')
ax1.legend()
# Set axes limits.
'''ax1.set_xlim(0, 8)
ax1.set_ylim(0, 4)'''


ax2.hist(setosa_df["petal_length"], bins=10, color="red")
ax2.set_xlabel('Petal Length (cm)')
ax2.set_ylabel('Frequency')
ax1.set_title('Histogram of Petal Length (Setosa)')
ax1.legend()

ax3.hist(virginica_df["petal_length"], bins=10, color="green")
ax3.set_xlabel('Petal Length (cm)')
ax3.set_ylabel('Frequency')
ax3.set_title('Histogram of Petal Length (Virginica)')
ax3.legend()

plt.show()