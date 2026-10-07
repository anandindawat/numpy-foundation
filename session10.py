import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4500, 6200, 7100, 5800, 8200, 10500, 9000]

plt.plot(days, steps, marker="o")

plt.title("Daily Steps - Last 7 Days")
plt.xlabel("Day")
plt.ylabel("Number of Steps")

plt.grid(True)
plt.savefig("steps_lineplot.png")
plt.show()

import matplotlib.pyplot as plt

restaurants = [
    "Restaurant 1", "Restaurant 2", "Restaurant 3",
    "Restaurant 4", "Restaurant 5", "Restaurant 6",
    "Restaurant 7", "Restaurant 8", "Restaurant 9",
    "Restaurant 10"
]

ratings = [3.2, 4.1, 3.8, 4.5, 3.5, 4.2, 4.7, 3.9, 4.3, 3.6]

meal_price = [250, 500, 350, 700, 300, 550, 800, 400, 650, 280]

plt.scatter(ratings, meal_price)

plt.title("Restaurant Ratings vs Average Meal Price")
plt.xlabel("Zomato Rating")
plt.ylabel("Average Meal Price (₹)")

plt.show()


import matplotlib.pyplot as plt

platforms = ["Swiggy", "Zomato", "Domino's"]
orders = [12, 8, 5]

colors = ["red", "blue", "orange"]

for i in range(len(platforms)):
    plt.bar(platforms[i], orders[i], color=colors[i],
            label=platforms[i])

plt.title("Food Orders in Last Month")
plt.xlabel("Food Platform")
plt.ylabel("Number of Orders")

plt.legend()
plt.show()

import matplotlib.pyplot as plt

durations = [
    25, 40, 35, 50, 60,
    45, 30, 55, 70, 20,
    35, 40, 65, 80, 50,
    45, 30, 90, 60, 40
]

plt.hist(
    durations,
    bins=5,
    color="purple",
    edgecolor="black"
)

plt.title("Spotify Listening Session Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")

plt.show()

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

screen_time = [2.5, 3.0, 2.8, 3.5, 4.0, 5.2, 4.5]

likes = [20, 25, 18, 30, 35, 45, 40]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First subplot - Line Plot
ax[0].plot(days, screen_time, marker="o")

ax[0].set_title("Daily Instagram Screen Time")
ax[0].set_xlabel("Day")
ax[0].set_ylabel("Screen Time (Hours)")


# Second subplot - Bar Chart
ax[1].bar(days, likes)

ax[1].set_title("Instagram Posts Liked")
ax[1].set_xlabel("Day")
ax[1].set_ylabel("Number of Likes")


plt.tight_layout()

plt.savefig("social_media_usage.png")

plt.show()