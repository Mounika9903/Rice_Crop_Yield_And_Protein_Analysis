# Check if the data is loaded into a single column
if len(data.columns) == 1:
    print("\nSingle-column issue detected. Attempting to split columns...")
    data = data.iloc[:, 0].str.split("\t", expand=True)
    print("Columns split successfully!")

# Rename columns (ensure correct naming)
data.columns = [
    "Region", "Issue", "Weather", "Soil Type", "Rice Variety", "Soil pH", 
    "Nitrogen Fertilizer Used (kg/ha)", "Water Availability", "Temperature (°C)", 
    "Rainfall (mm/month)", "Yield (kg/ha)", "Protein Deficiency Severity"
]

# Verify column names
print("\nUpdated Column Names:")
print(data.columns)
#Convert relevant columns to numeric and handle invalid entries
numeric_columns = [
    "Soil pH", "Nitrogen Fertilizer Used (kg/ha)", "Temperature (°C)", 
    "Rainfall (mm/month)", "Yield (kg/ha)", "Protein Deficiency Severity"
]

print("\nConverting numeric columns...")
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors="coerce")
    print(f"Converted {col}")
# Check for missing values
print("\nMissing Values in the Dataset:")
print(data.isnull().sum())
# Display cleaned data information
print("\nCleaned Dataset Preview (First 5 Rows):")
print(data.head())

