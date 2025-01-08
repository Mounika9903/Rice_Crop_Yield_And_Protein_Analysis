import pandas as pd

# Load the dataset with the correct delimiter
file_path = "rice_crop_analysis.csv"  # Replace with your file path
try:
    data = pd.read_csv(file_path, sep="\t")  # Adjust separator if necessary
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display the first few rows to verify the structure
print("\nFirst Five Rows of the Dataset:")
print(data.head())

# Display dataset info
print("Dataset Information:")
print(data.info())
