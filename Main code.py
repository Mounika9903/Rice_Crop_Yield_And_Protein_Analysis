import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# Load the dataset
data = pd.read_csv("rice_crop_analysis.csv", delimiter="\t")

# Rename columns if needed
data.rename(columns={
    'Temperature (Â°C)': 'Temperature (°C)',
    'Rainfall (mm/month)': 'Rainfall (mm/month)',
    'Soil pH': 'Soil pH',
    'Nitrogen Fertilizer Used (kg/ha)': 'Nitrogen Fertilizer Used (kg/ha)',
    'Yield': 'Yield (kg/ha)',
    'Protein Deficiency': 'Protein Deficiency Severity',
    'Rice Variety': 'Rice Variety'
}, inplace=True)

# Ensure columns are numeric
data['Temperature (°C)'] = pd.to_numeric(data['Temperature (°C)'], errors='coerce')
data['Rainfall (mm/month)'] = pd.to_numeric(data['Rainfall (mm/month)'], errors='coerce')
data['Soil pH'] = pd.to_numeric(data['Soil pH'], errors='coerce')
data['Nitrogen Fertilizer Used (kg/ha)'] = pd.to_numeric(data['Nitrogen Fertilizer Used (kg/ha)'], errors='coerce')

# Map protein deficiency to numeric values
data['Protein Deficiency Severity'] = data['Protein Deficiency Severity'].map({'Mild': 0, 'Moderate': 1, 'Severe': 2})

# Drop any rows with missing values
data.dropna(inplace=True)

# Features and targets
X = data[['Temperature (°C)', 'Rainfall (mm/month)', 'Soil pH', 'Nitrogen Fertilizer Used (kg/ha)']]
y_yield = data['Yield (kg/ha)']
y_protein = data['Protein Deficiency Severity']
y_variety = data['Rice Variety']

# Train-test split
X_train, X_test, y_yield_train, y_yield_test = train_test_split(X, y_yield, test_size=0.2, random_state=42)
X_train_p, X_test_p, y_protein_train, y_protein_test = train_test_split(X, y_protein, test_size=0.2, random_state=42)
X_train_v, X_test_v, y_variety_train, y_variety_test = train_test_split(X, y_variety, test_size=0.2, random_state=42)

# Train Random Forest models
rf_yield = RandomForestRegressor(n_estimators=100, random_state=42)
rf_yield.fit(X_train, y_yield_train)

rf_protein = RandomForestRegressor(n_estimators=100, random_state=42)
rf_protein.fit(X_train_p, y_protein_train)

rf_variety = RandomForestClassifier(n_estimators=100, random_state=42)
rf_variety.fit(X_train_v, y_variety_train)

# Model Accuracy for Yield (R^2 Score)
y_yield_pred = rf_yield.predict(X_test)
yield_r2_score = r2_score(y_yield_test, y_yield_pred)
print(f"\nYield Model R² Score: {yield_r2_score:.2f}")

# Model Accuracy for Protein Deficiency (R^2 Score)
y_protein_pred = rf_protein.predict(X_test_p)
protein_r2_score = r2_score(y_protein_test, y_protein_pred)
print(f"Protein Deficiency Model R² Score: {protein_r2_score:.2f}")

# Model Accuracy for Rice Variety (Accuracy Score)
y_variety_pred = rf_variety.predict(X_test_v)
variety_accuracy = accuracy_score(y_variety_test, y_variety_pred)
print(f"Rice Variety Model Accuracy: {variety_accuracy:.2f}")

# Function to provide solutions for reducing protein deficiency
def protein_deficiency_solutions(severity_category):
    recommendations = {
        'Mild': [
            "Ensure balanced nitrogen fertilizer application (e.g., Urea or Calcium Ammonium Nitrate).",
            "Plant high-protein rice varieties like IR64 or Pusa Basmati 1509.",
            "Regularly monitor soil pH to optimize nutrient absorption."
        ],
        'Moderate': [
            "Use high-protein rice varieties such as Swarna Sub1 or Dhan 44.",
            "Increase organic matter in soil using compost or vermicompost.",
            "Apply micronutrient fertilizers like Zinc Sulfate or Boron (Borax)."
        ],
        'Severe': [
            "Adopt slow-release nitrogen fertilizers like Neem-Coated Urea.",
            "Use foliar feeding with Iron (Ferrous Sulfate) for immediate nutrient correction.",
            "Conduct a detailed soil test and apply fertilizers tailored to deficiencies."
        ]
    }
    return recommendations.get(severity_category, ["Consult an agronomist for tailored solutions."])

# Function to predict crop conditions
def predict_crop_conditions():
    print("Enter the following details to predict yield, protein deficiency, and rice variety:")

    try:
        temp = float(input("Temperature (°C): "))
        rainfall = float(input("Rainfall (mm/month): "))
        soil_ph = float(input("Soil pH: "))
        nitrogen = float(input("Nitrogen Fertilizer Used (kg/ha): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Prepare input data
    user_input = pd.DataFrame([[temp, rainfall, soil_ph, nitrogen]], columns=X.columns)

    # Predictions
    predicted_yield = rf_yield.predict(user_input)[0]
    predicted_protein = rf_protein.predict(user_input)[0]
    predicted_variety = rf_variety.predict(user_input)[0]

    # Convert protein severity to category
    severity_map = {0: 'Mild', 1: 'Moderate', 2: 'Severe'}
    predicted_protein_category = severity_map.get(int(predicted_protein), 'Unknown')

    # Get recommendations
    solutions = protein_deficiency_solutions(predicted_protein_category)

    # Display predictions and recommendations
    print(f"\nPredicted Yield (kg/ha): {predicted_yield:.2f}")
    print(f"Predicted Protein Deficiency Severity: {predicted_protein_category}")
    print(f"Suggested Rice Variety: {predicted_variety}")
    print("\nRecommendations to Reduce Protein Deficiency:")
    for solution in solutions:
        print(f"- {solution}")

# Call the function
predict_crop_conditions()
