import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in 'tips' dataset
tips = sns.load_dataset('tips')

# Display the first few rows of the dataset
print("First five rows of the dataset:")
print(tips.head())

# 1. Scatter Plot - Total Bill vs Tip
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='day', style='sex', palette='coolwarm')
plt.title("Scatter Plot of Total Bill vs Tip")
plt.grid(True)
plt.show()

# 2. Box Plot - Distribution of Total Bill by Day
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips, palette='coolwarm')
plt.title("Box Plot of Total Bill by Day")
plt.grid(True)
plt.show()

# 3. Count Plot - Number of smokers and non-smokers
plt.figure(figsize=(8, 6))
sns.countplot(x='smoker', data=tips, palette='coolwarm')
plt.title("Count Plot of Smokers vs Non-Smokers")
plt.grid(True)
plt.show()

# 4. Pair Plot - Pairwise relationships in the dataset
plt.figure(figsize=(8, 6))
sns.pairplot(data=tips, hue='sex', palette='coolwarm')
plt.show()
