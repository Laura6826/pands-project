# This is an analysis of the Fisher Iris Data set.
# Author: Laura Lyons

# Import the libraries necessary for the analysis.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Fisher Iris data set.
df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# It would be helpful to know what type fo data each of the variables is?
types= df.dtypes
print(types)

# Get a summary of each variable
summary = df.describe()

# Save the summary to a text file
#summary.to_csv("iris_summary.txt", sep="\t", index=False)
#print(" A summary of each variable saved to iris_summary.txt")

# It would be useful if we could get a summary of the variables, subdivided by the iris species.
summary_by_species = df.groupby('species').describe()
summary_by_species.to_csv("iris_summary_by_species.txt", sep="\t")
print("A summary of each variable, subdivided by iris type, has been saved to iris_summary_by_species.txt")