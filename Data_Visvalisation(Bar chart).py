import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("rice_crop_analysis.csv", delimiter='\t')

# Bar Chart: Yield by Rice Variety
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(
    data=data, 
    x="Rice Variety", 
    y="Yield (kg/ha)", 
    hue="Rice Variety",  # Set hue to match x
    errorbar=None,  # Updated from ci=None
    estimator=lambda x: x.mean(), 
    palette="viridis",
    dodge=False  # Ensures bars are not separated
)
plt.title("Yield Comparison Across Rice Varieties", fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.ylabel("Yield (kg/ha)", fontsize=12)
plt.xlabel("Rice Variety", fontsize=12)
plt.legend([], [], frameon=False)  # Remove legend
plt.tight_layout()
plt.show()
