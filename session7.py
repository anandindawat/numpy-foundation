import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# TASK 1: Detect Outliers using IQR
# Zomato restaurant ratings
# =========================================================

zomato = pd.DataFrame({
    "restaurant": [
        "Restaurant A", "Restaurant B", "Restaurant C",
        "Restaurant D", "Restaurant E", "Restaurant F",
        "Restaurant G", "Restaurant H", "Restaurant I",
        "Restaurant J"
    ],
    "user_rating": [4.2, 4.5, 3.8, 4.0, 4.3, 4.1, 3.9, 4.4, 1.0, 4.2]
})

print("Zomato Dataset:")
print(zomato)

Q1 = zomato["user_rating"].quantile(0.25)
Q3 = zomato["user_rating"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = zomato[
    (zomato["user_rating"] < lower_bound) |
    (zomato["user_rating"] > upper_bound)
]

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nOutlier indices:")
print(outliers.index.tolist())

print("\nOutlier records:")
print(outliers)


# =========================================================
# TASK 2: Boxplot for Swiggy order_amount
# =========================================================

swiggy = pd.DataFrame({
    "order_amount": [
        250, 320, 450, 500, 280,
        350, 420, 600, 300, 380,
        450, 520, 700, 2500, 3000
    ]
})

print("\nSwiggy Order Amount:")
print(swiggy)

plt.boxplot(swiggy["order_amount"])
plt.xlabel("Swiggy Orders")
plt.ylabel("Order Amount")
plt.title("Swiggy Order Amount - Boxplot")
plt.show()


# =========================================================
# TASK 3: Winsorization
# Paytm transaction_amount
# =========================================================

paytm = pd.DataFrame({
    "transaction_amount": [
        100, 250, 300, 450, 500,
        600, 750, 900, 1200, 1500,
        2000, 3000, 5000, 10000, 50000
    ]
})

print("\nPaytm Original Data:")
print(paytm)

lower_limit = paytm["transaction_amount"].quantile(0.05)
upper_limit = paytm["transaction_amount"].quantile(0.95)

paytm["transaction_amount"] = paytm["transaction_amount"].clip(
    lower=lower_limit,
    upper=upper_limit
)

print("\nPaytm Data after Winsorization:")
print(paytm)

print("\nUpdated Statistics:")
print(paytm["transaction_amount"].describe())


# =========================================================
# TASK 4: Convert Flipkart prices from string to numeric
# =========================================================

flipkart = pd.DataFrame({
    "product": [
        "Mobile", "Laptop", "Headphones",
        "Keyboard", "Mouse"
    ],
    "price": [
        "₹1,29,999",
        "₹59,999",
        "₹2,499",
        "₹1,299",
        "₹799"
    ]
})

print("\nFlipkart Original Data:")
print(flipkart)

flipkart["price"] = (
    flipkart["price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

print("\nFlipkart Data after conversion:")
print(flipkart)

print("\nPrice Data Type:")
print(flipkart["price"].dtype)


# =========================================================
# TASK 5: Convert Spotify is_premium column to Boolean
# =========================================================

spotify = pd.DataFrame({
    "user": [
        "User1", "User2", "User3",
        "User4", "User5", "User6",
        "User7", "User8"
    ],
    "is_premium": [
        True, False, "yes", "no",
        1, 0, "True", "False"
    ]
})

print("\nSpotify Original Data:")
print(spotify)

spotify["is_premium"] = spotify["is_premium"].apply(
    lambda x: True
    if str(x).lower() in ["true", "1", "yes"]
    else False
)

print("\nSpotify Data after Boolean Conversion:")
print(spotify)

print("\nData Type:")
print(spotify["is_premium"].dtype)