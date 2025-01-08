import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("rice_crop_analysis.csv", delimiter='\t')

# Heatmap: Correlation Between Numeric Columns
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
correlation_matrix = data[numeric_columns].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14)
plt.tight_layout()
plt.show()
