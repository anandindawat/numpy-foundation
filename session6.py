import pandas as pd
import numpy as np

# --------------------------------------------------
# TASK 1: Load IPL player stats dataset
# --------------------------------------------------

data = {
    "player_name": [
        "Virat Kohli",
        "Rohit Sharma",
        "MS Dhoni",
        "AB de Villiers",
        "Suresh Raina",
        "Chris Gayle",
        "Jasprit Bumrah",
        "Ravindra Jadeja"
    ],
    "runs": [726, 648, np.nan, 512, 389, np.nan, 45, 234],
    "matches": [14, 14, 13, np.nan, 12, 10, 14, 13]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing values using isnull():")
print(df.isnull().sum())

print("\nNon-missing values using notnull():")
print(df.notnull().sum())


# --------------------------------------------------
# TASK 2: Drop rows containing missing values
# --------------------------------------------------

df_dropped = df.dropna(axis=0, how="any")

print("\nDataset after dropping rows with missing values:")
print(df_dropped)

print("\nShape before dropping:")
print(df.shape)

print("Shape after dropping:")
print(df_dropped.shape)


# --------------------------------------------------
# TASK 3: Fill missing runs with mean
# --------------------------------------------------

df["runs"] = df["runs"].fillna(df["runs"].mean())

print("\nRuns column after filling missing values with mean:")
print(df["runs"])


# --------------------------------------------------
# TASK 4: Zomato-style ratings dataset
# --------------------------------------------------

ratings = pd.DataFrame({
    "restaurant": [
        "Restaurant A",
        "Restaurant B",
        "Restaurant C",
        "Restaurant D",
        "Restaurant E",
        "Restaurant F"
    ],
    "rating": [4.5, np.nan, 3.8, np.nan, np.nan, 4.2]
})

print("\nZomato-style dataset BEFORE filling:")
print(ratings)

# Forward fill
ratings["rating"] = ratings["rating"].ffill()

# Backward fill remaining missing values
ratings["rating"] = ratings["rating"].bfill()

print("\nZomato-style dataset AFTER filling:")
print(ratings)


# --------------------------------------------------
# TASK 5: Missingness mechanism
# --------------------------------------------------

print("\nTASK 5 Explanation:")

print("""
The missing values in the runs column are most likely MCAR
(Missing Completely At Random) for this simulated dataset.
The missing values were intentionally introduced randomly and
there is no relationship between the missing values and other
variables such as player name or matches.
""")