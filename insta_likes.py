import numpy as np

# Task 1: Instagram followers
followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Followers Array:")
print(followers)
print("Shape:", followers.shape)
print("Number of Dimensions:", followers.ndim)
print("Data Type:", followers.dtype)


# Task 2: Zomato order IDs
order_ids = np.arange(101, 111)

print("\nZomato Order IDs:")
print(order_ids)
print("Size:", order_ids.size)


# Task 3: 3x3 Identity Matrix
identity_matrix = np.eye(3)

print("\n3x3 Identity Matrix:")
print(identity_matrix)

# Diagonal values are 1 and all other values are 0


# Task 4: Cricket scores
cricket_scores = [45, 67, 120, 89, 54]
cricket_array = np.array(cricket_scores)

print("\nCricket Scores Array:")
print(cricket_array)
print("Item Size:", cricket_array.itemsize)