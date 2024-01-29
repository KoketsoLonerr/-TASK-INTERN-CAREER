import pandas as pd
import matplotlib.pyplot as plt
import os

def process_data(input_file, output_file):
    
    df = pd.read_csv(os.path.join('data', input_file))

    
    summary_stats = df.describe()

   
    filtered_data = df[df['Age'] > 25]

    # Generate a histogram for the 'Salary' column
    df['Salary'].plot(kind='hist', bins=10, title='Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.show()

    output_path = os.path.join('output', output_file)
    filtered_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "sample_data.csv"
    output_file = "processed_data.csv"
    process_data(input_file, output_file)
