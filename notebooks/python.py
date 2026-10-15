import os
import pandas as pd
import matplotlib.pyplot as plt

# Get current folder directory and ensure results folder exists
current_dir = os.getcwd()
results_dir = os.path.join(current_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# 1. Save CSV Table
results_data = {
    "Category": ["Clustering", "Regression", "Classification"],
    "Dataset": ["Mall_Customers.csv", "insurance_pre.csv", "Social_Network_Ads.csv"],
    "Best Algorithm": ["K-Means", "Gradient Boosting Regressor", "AdaBoost Classifier"],
    "Best Metric Value": ["Silhouette: 0.5539", "R2: 0.8781", "Accuracy: 90.00%"]
}
df_results = pd.DataFrame(results_data)
csv_path = os.path.join(results_dir, "metrics_summary.csv")
df_results.to_csv(csv_path, index=False)
print(f"Saved CSV successfully at: {csv_path}")

# 2. Save Graph (Using pure Matplotlib - no seaborn needed!)
plt.figure(figsize=(6, 4))
plt.bar(["K-Means", "Agglomerative", "DBSCAN"], [0.5539, 0.5530, 0.3920], color=['#3498db', '#e67e22', '#2ecc71'])
plt.title("Clustering Silhouette Score Comparison")
plt.ylabel("Silhouette Score")
plt.ylim(0, 1.0)

img_path = os.path.join(results_dir, "cluster_comparison.png")
plt.savefig(img_path, bbox_inches='tight')
plt.close()
print(f"Saved Image successfully at: {img_path}")
