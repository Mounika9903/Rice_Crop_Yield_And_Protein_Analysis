from sklearn.model_selection import train_test_split
X = data[['Temperature (°C)', 'Rainfall (mm/month)', 'Soil pH', 'Nitrogen Fertilizer Used (kg/ha)']]
y_yield = data['Yield (kg/ha)']
y_protein = data['Protein Deficiency Severity']
X_train, X_test, y_yield_train, y_yield_test = train_test_split(X, y_yield, test_size=0.2, random_state=42)
X_train_p, X_test_p, y_protein_train, y_protein_test = train_test_split(X, y_protein, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
print(y_yield_train)
print(y_yield_test)
print(y_protein_test)
print(y_protein_train)
