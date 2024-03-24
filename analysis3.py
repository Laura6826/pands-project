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

# Filter the data by the species and remove the index of the original data set.
versicolor_df = df[df["species"] == "versicolor"].reset_index(drop=True)
setosa_df=df[df["species"] == "setosa"].reset_index(drop=True)
virginica_df=df[df["species"] == "virginica"].reset_index(drop=True)

summary_versicolor = versicolor_df.describe()
summary_setosa= setosa_df.describe()
summary_virginica=virginica_df.describe()

# Define the CSV file path
csv_file = "combined_summary_outputs.csv"

# The following code was sourced from both Week 7, PandS and Microsoft CoPilot.
# Write the outputs to the CSV file
with open(csv_file, mode='w', newline='') as f:
    f.write('This is a summary of the 3 iris species from the Iris Dataset.\n\n')
    data = csv.reader(f)
    for row in data:
        print(' | '.join(row)) 
        
with open(csv_file, mode='a', newline='') as f:
    pd.concat([summary_versicolor]).to_csv(f)
with open(csv_file, mode='a', newline='') as f:
    pd.concat([summary_setosa], axis=1).to_csv(f)
with open(csv_file, mode='a', newline='') as f:
    pd.concat([summary_virginica], axis=1).to_csv (f)
'''(f)
with open(csv_file,'a') as f:
    for df in list_of_dfs:
        df.to_csv(f)
        f.write("\n")
        '''
# Print a success message
print(f"The summary outputs for each iris species have been successfully written to {csv_file}.")

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
