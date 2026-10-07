import pandas as pd

df = pd.DataFrame({
    "Restaurant": ["Dominos", "Pizza Hut", "Dominos", "KFC", "Dominos"],
    "Order_Date": ["2026-10-01", "2026-10-02", "2026-10-01", "2026-10-03", "2026-10-04"]
})

duplicates = df[df.duplicated(subset=["Restaurant", "Order_Date"])]

print(duplicates)


import pandas as pd

df = pd.DataFrame({
    "Review": [
        "Good product",
        "Very good",
        "Good product",
        "Excellent",
        "Good product",
        "Very good",
        "Nice product",
        "Very good"
    ]
})

counts = df["Review"].value_counts()

print(counts.head(3))

import pandas as pd

df = pd.DataFrame({
    "Playlist": [
        "My Songs",
        "Workout",
        "Party",
        "My Songs",
        "Chill",
        "Workout"
    ],
    "Creator": [
        "anand",
        "rahul",
        "amit",
        "anand",
        "neha",
        "rahul"
    ]
})

cleaned_df = df.drop_duplicates()

print(cleaned_df)

import pandas as pd

df = pd.DataFrame({
    "Username": [
        "insta_queen",
        "insta-queen",
        "instaqueen",
        "rahul123",
        "insta_queen"
    ]
})

df["Username"] = df["Username"].replace({
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen"
})

print(df)


import pandas as pd

df = pd.DataFrame({
    "Payment_Status": [
        "Yes",
        " yes ",
        "Y",
        "No",
        " no ",
        "N",
        " YES "
    ]
})

df["Payment_Status"] = (
    df["Payment_Status"]
    .str.strip()
    .str.lower()
    .map({
        "yes": 1,
        "y": 1,
        "no": 0,
        "n": 0
    })
)

print(df)


