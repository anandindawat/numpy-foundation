import numpy as np

# Friend 1 and Friend 2 daily steps
friend1 = np.array([5000, 7000, 6500, 8000, 9000, 7500, 6000])
friend2 = np.array([4500, 6500, 7000, 7500, 8500, 8000, 5500])

print("Friend 1 Steps:")
print(friend1)

print("\nFriend 2 Steps:")
print(friend2)

print("\nAddition:")
print(friend1 + friend2)

print("\nSubtraction:")
print(friend1 - friend2)

print("\nMultiplication:")
print(friend1 * friend2)

print("\nDivision:")
print(friend1 / friend2)


user_preferences = np.array([
    [5, 4, 3],
    [3, 5, 4],
    [4, 3, 5]
])

song_popularity = np.array([
    [4, 3, 5],
    [5, 4, 3],
    [3, 5, 4]
])

print("User Preferences:")
print(user_preferences)

print("\nSong Popularity:")
print(song_popularity)

# Using dot()
recommendation_dot = np.dot(user_preferences, song_popularity)

# Using matmul()
recommendation_matmul = np.matmul(user_preferences, song_popularity)

print("\nRecommendation Matrix using dot():")
print(recommendation_dot)

print("\nRecommendation Matrix using matmul():")
print(recommendation_matmul)


image = np.array([
    [120, 150, 180, 200],
    [100, 130, 160, 190],
    [90, 140, 170, 210],
    [110, 125, 155, 195]
])

print("Original Image Matrix:")
print(image)

# Transpose
rotated_image = image.T

print("\nTransposed Image:")
print(rotated_image)

print("\nMean:", np.mean(rotated_image))
print("Median:", np.median(rotated_image))
print("Standard Deviation:", np.std(rotated_image))
print("Variance:", np.var(rotated_image))


ratings = np.array([
    [4, 2, 1],
    [2, 5, 2],
    [1, 2, 4]
])

print("Zomato Rating Matrix:")
print(ratings)

# Determinant
det = np.linalg.det(ratings)

print("\nDeterminant:")
print(det)

# Inverse
if det != 0:
    inverse = np.linalg.inv(ratings)
    print("\nInverse:")
    print(inverse)
else:
    print("\nMatrix is not invertible.")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(ratings)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


orders = np.array([
    [10, 15, 20, 25, 30, 35],
    [12, 18, 22, 28, 32, 40]
])

print("Original (2, 6) Array:")
print(orders)

# Reshape to (3, 4)
reshaped = orders.reshape(3, 4)

print("\nReshaped (3, 4) Array:")
print(reshaped)

# Flatten
flattened = reshaped.flatten()

print("\nFlattened Array:")
print(flattened)

# Split into two equal parts
part1, part2 = np.split(flattened, 2)

print("\nPart 1:")
print(part1)

print("\nPart 2:")
print(part2)

# Stack vertically
stacked = np.vstack((part1, part2))

print("\nVertically Stacked Array:")
print(stacked)


