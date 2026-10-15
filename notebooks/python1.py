import matplotlib.pyplot as plt
import seaborn as sns

# Example: Generating and saving a plot
plt.figure(figsize=(6, 4))
sns.barplot(x=["K-Means", "Agglomerative", "DBSCAN"], y=[0.5539, 0.5530, 0.3920])
plt.title("Clustering Silhouette Score Comparison")
plt.ylabel("Silhouette Score")

# Save directly into the results folder
plt.savefig("results/cluster_comparison.png", bbox_inches='tight')
plt.close()
print("Graph saved successfully!")