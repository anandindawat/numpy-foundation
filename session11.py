import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Line Chart
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
steps = [4000, 5500, 6200, 4800, 7500]

ax[0, 0].plot(days, steps, marker="o")
ax[0, 0].set_title("Daily Steps")
ax[0, 0].set_xlabel("Day")
ax[0, 0].set_ylabel("Steps")


# 2. Bar Chart
platforms = ["Swiggy", "Zomato", "Domino's"]
orders = [15, 12, 8]

ax[0, 1].bar(platforms, orders)
ax[0, 1].set_title("Food Orders")
ax[0, 1].set_xlabel("Platform")
ax[0, 1].set_ylabel("Orders")


# 3. Scatter Plot
ratings = [3.2, 3.8, 4.1, 4.5, 4.8]
prices = [250, 350, 450, 600, 750]

ax[1, 0].scatter(ratings, prices)
ax[1, 0].set_title("Rating vs Price")
ax[1, 0].set_xlabel("Rating")
ax[1, 0].set_ylabel("Price")


# 4. Pie Chart
labels = ["Food", "Travel", "Shopping", "Entertainment"]
expenses = [40, 25, 20, 15]

ax[1, 1].pie(expenses, labels=labels, autopct="%1.1f%%")
ax[1, 1].set_title("Monthly Expenses")


plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

platforms = ["Zomato", "Swiggy", "Domino's"]
delivery_time = [35, 30, 40]

colors = ["red", "blue", "orange"]
linestyles = ["-", "--", ":"]
linewidths = [2, 3, 4]

bars = plt.bar(platforms, delivery_time)

for bar, color, linestyle, linewidth in zip(
    bars, colors, linestyles, linewidths
):
    bar.set_facecolor(color)
    bar.set_edgecolor("black")
    bar.set_linestyle(linestyle)
    bar.set_linewidth(linewidth)

plt.title("Average Delivery Time")
plt.xlabel("Platform")
plt.ylabel("Delivery Time (Minutes)")

plt.show()

import matplotlib.pyplot as plt

influencers = ["A", "B", "C", "D", "E"]

followers = [1.2, 2.5, 3.8, 5.0, 6.5]
daily_posts = [2, 4, 3, 5, 6]

fig, ax1 = plt.subplots(figsize=(10, 6))

# Left Y-axis - Followers
ax1.plot(
    influencers,
    followers,
    marker="o",
    color="blue",
    label="Followers"
)

ax1.set_xlabel("Influencers")
ax1.set_ylabel("Followers (Millions)", color="blue")


# Right Y-axis - Daily Posts
ax2 = ax1.twinx()

ax2.plot(
    influencers,
    daily_posts,
    marker="s",
    color="red",
    label="Daily Posts"
)

ax2.set_ylabel("Average Daily Posts", color="red")


plt.title("Influencer Followers vs Daily Posts")

plt.show()

import matplotlib.pyplot as plt

movies = [
    "Movie A",
    "Movie B",
    "Movie C",
    "Movie D",
    "Movie E"
]

tickets = [120, 250, 180, 320, 200]
imdb_rating = [6.2, 7.5, 6.8, 8.1, 7.0]

plt.scatter(tickets, imdb_rating)

for i in range(len(movies)):
    plt.annotate(
        movies[i],
        (tickets[i], imdb_rating[i]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.title("Movie Tickets Sold vs IMDb Rating")
plt.xlabel("Tickets Sold (Lakhs)")
plt.ylabel("IMDb Rating")

plt.show()

import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

sales = [
    120, 150, 140, 180,
    200, 220, 190, 250,
    270, 300, 650, 320
]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(months, sales, marker="o")

ax.set_title("Flipkart Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹ Crore)")

# Highest sales point
highest_sales = max(sales)
highest_index = sales.index(highest_sales)

ax.annotate(
    "Big Billion Days",
    xy=(months[highest_index], highest_sales),
    xytext=(20, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.tight_layout()
plt.show()