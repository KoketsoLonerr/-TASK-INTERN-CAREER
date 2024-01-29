```markdown
# Data Processing Project

This Python project performs data processing on a dataset, calculating summary statistics, filtering data based on specific criteria, generating data visualizations, and saving the processed data to a new file. It provides a versatile tool for handling different datasets.

## Requirements

To run this script, you need to have Python 3 and the required libraries installed:

- pandas
- matplotlib

You can install them using pip:

```bash
pip install pandas matplotlib
```

## Project Structure

```
data_processing_project/
│
├── scripts/
│   ├── data_processing_script.py
│
├── data/
│   ├── sample_data.csv
│
├── output/
│   ├── processed_data.csv
│
├── README.md
```

- **scripts/**: Contains the Python script for data processing (`data_processing_script.py`).
- **data/**: Store your input datasets in this directory.
- **output/**: This directory is where your processed data will be saved.
- **README.md**: Documentation for the project.

## Usage

1. Place your dataset in a CSV file (e.g., `sample_data.csv`) in the `data/` directory.
2. Modify the `input_file` variable in the script to match the name of your dataset.
3. Run the script using the command: `python scripts/data_processing_script.py`.
4. Check the output CSV file (`processed_data.csv`) in the `output/` directory for the filtered data.

## Script Overview

The script performs the following operations:

- Reads the dataset from the `data/` directory.
- Calculates summary statistics.
- Filters data based on specific criteria (e.g., age > 25).
- Generates a histogram for the 'Salary' column.
- Saves the processed data to a new CSV file in the `output/` directory.

## Dependencies

- pandas
- matplotlib

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Mmamonwana Marble Tjatji <tjatjikm99@gmail.com>
```