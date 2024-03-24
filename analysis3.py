# Import the libraries necessary for the analysis.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv 

'''iris='iris_dataset.csv'
with open (iris,'r') as df:
    summary= df.describe()
    print (summary)'''

# Load the Iris dataset
df = pd.read_csv('iris_dataset.csv')

# Filter the data by the species.
versicolor_df = df[df["species"] == "versicolor"]
setosa_df=df[df["species"] == "setosa"]
virginica_df=df[df["species"] == "virginica"]

summary_versicolor = versicolor_df.describe()
summary_setosa= setosa_df.describe()
summary_virginica=virginica_df.describe()

summary= (summary_versicolor, summary_setosa, summary_virginica)

# The following code was sourced from both Week 7, PandS and Microsoft CoPilot.
# Define the CSV file path
csv_file = "combined_outputs.csv"

# Write the outputs to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Output 1", "Output 2", "Output 3"])  # Write header
    writer.writerows(zip(output1, output2, output3))  # Write data

# Print a success message
print(f"The outputs are successfully written to {csv_file}.")
with open 
# Save the summary to a text file
summary.to_csv("iris_summary.txt", sep="\t\t\t")
print("Summary of each variable, subdivided by species, is saved to iris_summary.txt")


#df = pd.DataFrame(columns=df.feature_names)
#df['species'] = df.target_names[df.target]
'''
table = df.describe()
for row in table:
    print('| {:15} | {:^15} | {:>15} | {:<15} |'.format(*row))

# Save the summary to a text file
table.to_csv("iris_summary.txt", sep="\t")

# Print a success message
print("Summary of each variable saved to iris_summary.txt")
# Show first few rows of the dataset
#summary= df.describe()
#print (summary)
'''
# Group the data by species
grouped = df.groupby("species")

# Create a summary for each variable
summary = grouped.describe()

# Save the summary to a text file
summary.to_csv("iris_summary.txt", sep="\t\t\t")

print("Summary of each variable, subdivided by species, is saved to iris_summary.txt")