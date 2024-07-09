import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# DATA:
# https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data

# Load DF
input_file = 'input/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(input_file)
data_col = df.columns.tolist()
print(len(data_col))
# Basic visualization
for col_name in data_col[1:]:
    df_col = df[[col_name]]
    # Count the occurrences of each category
    counts = df[col_name].value_counts()
    # Determine the number of bins
    num_unique_values = len(counts)
    if num_unique_values > 50:
        bins = 25
    else:
        bins = num_unique_values
    # Plot the histogram using plt.hist()
    plt.figure()
    plt.hist(df[col_name], bins=bins, edgecolor='black', color='skyblue')
    # Add titles and labels
    plt.title(f'Histogram of {col_name}')
    plt.xlabel('Values Bins')
    plt.ylabel('Frequency')
    # Display the plot
    plt.tight_layout()
    plt.show()
