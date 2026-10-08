import pandas as pd

# Load IPL dataset
df = pd.read_csv("ipl_matches.csv")

# Summary statistics
print("Mean:", df["total_runs"].mean())
print("Median:", df["total_runs"].median())
print("Minimum:", df["total_runs"].min())
print("Maximum:", df["total_runs"].max())
print("Standard Deviation:", df["total_runs"].std())


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("flipkart_reviews.csv")

# Count reviews for each rating
rating_counts = df["rating"].value_counts().sort_index()

print(rating_counts)

# Bar plot
sns.barplot(
    x=rating_counts.index,
    y=rating_counts.values
)

plt.title("Number of Flipkart Reviews by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Reviews")

plt.show()

