# Import the libraries necessary for the analysis.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv 
import prettytable as pt

# Load the Iris dataset
df = pd.read_csv('iris_dataset.csv')
styles = [dict(selector="th", props=[("text-align", "center")])]
df.style.set_table_styles(styles)

# Filter the data by the species.
versicolor_df = df[df["species"] == "versicolor"]
setosa_df=df[df["species"] == "setosa"]
virginica_df=df[df["species"] == "virginica"]

# To change the format of .describe() output:
# To set the format for floating-point numbers: (.map(lambda x: f"{x:0.2f}")
# Reference: https://stackoverflow.com/questions/55394854/how-to-change-the-format-of-describe-output
summary_versicolor = versicolor_df.describe().map(lambda x: f"{x:0.2f}")
summary_setosa= setosa_df.describe().map(lambda x: f"{x:0.2f}")
summary_virginica=virginica_df.describe().map(lambda x: f"{x:0.2f}")

# Define the CSV file path
csv_file = "combined_summary_outputs.csv"

# The following code was sourced from both Week 7, PandS and Microsoft CoPilot.
# Write the outputs to the CSV file
with open(csv_file, mode='w', newline='') as f:
    f.write('This is a summary of the 3 iris species from the Iris Dataset.\n\n')
    # This will add a heading to my 'output' .csv file.
    '''data = csv.reader(f)
    for row in data:
        print(' | '.join(row))''' 
        
with open(csv_file, mode='a', newline='') as f:
    f.write('Versicolor.\n') # This will add the heading 'Versicolor' to the data table.
    pd.concat([summary_versicolor], axis=1).to_csv(f)
with open(csv_file, mode='a', newline='') as f:
    f.write('Setosa.\n')
    pd.concat([summary_setosa], axis=1).to_csv(f)
with open(csv_file, mode='a', newline='') as f:
    f.write('Virginica.\n')
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

'''
