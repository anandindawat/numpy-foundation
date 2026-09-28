import numpy as np

ratings = np.array([
    [4, 5, 3, 4, 2],
    [5, 4, 4, 3, 5],
    [3, 5, 4, 5, 4],
    [4, 3, 5, 4, 5]
])

print("Ratings:")
print(ratings)


print("2nd and 3rd users ratings:")
print(ratings[1:3])


steps = np.array([7500, 8200, 9000, 6500, 10000,
                  7800, 8500, 9200, 7000, 11000])

result = steps[steps > 8000]

print("Steps greater than 8000:")
print(result)


ipl_scores = np.array([185, 210, 156, 198, 225, 176, 203, 190])

result = ipl_scores[[1, 4, 6]]

print("Scores of matches 2, 5 and 7:")
print(result)


prices = np.array([1000, 2500, 5000, 7500, 12000])

discounted_prices = prices * 0.90

print("Original prices:")
print(prices)

print("Prices after 10% discount:")
print(discounted_prices)


ratings = np.array([-2, 5, 3, -1, 0, 4, -3, 5])

ratings[ratings < 0] = 0

print("Updated ratings:")
print(ratings)
