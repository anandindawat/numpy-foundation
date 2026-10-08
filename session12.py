import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Random delivery time for 50 orders
np.random.seed(42)
delivery_time = np.random.randint(20, 61, 50)

# Histplot
sns.histplot(delivery_time, bins=10, kde=True)

plt.title("Zomato Delivery Time Distribution")
plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Number of Orders")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Boxplot
sns.boxplot(x="day", y="total_bill", data=tips)

plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Darkgrid theme
sns.set_theme(style="darkgrid")

teams = [
    "CSK", "MI", "RCB", "KKR",
    "SRH", "RR", "DC", "PBKS"
]

# Create data
np.random.seed(42)

data = []

for team in teams:
    scores = np.random.randint(120, 221, 30)

    for score in scores:
        data.append([team, score])

df = pd.DataFrame(data, columns=["Team", "Runs"])

# Violin plot
sns.violinplot(x="Team", y="Runs", data=df)

plt.title("IPL Run Distribution by Team")
plt.xlabel("Team")
plt.ylabel("Runs")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

genres = [
    "Pop", "Rock", "Hip-Hop", "Jazz",
    "Pop", "Rock", "Pop", "Hip-Hop",
    "Jazz", "Pop", "Rock", "Hip-Hop",
    "Pop", "Jazz", "Rock", "Pop",
    "Hip-Hop", "Rock", "Jazz", "Pop",
    "Rock", "Pop", "Hip-Hop", "Jazz",
    "Pop", "Rock", "Hip-Hop", "Pop",
    "Jazz", "Rock", "Pop", "Hip-Hop",
    "Rock", "Jazz", "Pop", "Rock",
    "Hip-Hop", "Pop", "Jazz", "Rock"
]

df = pd.DataFrame({"Genre": genres})

# Countplot
sns.countplot(x="Genre", data=df)

plt.title("Number of Spotify Songs by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Whitegrid theme
sns.set_theme(style="whitegrid")

# Daily steps for one week
steps = [
    4500,
    6200,
    7800,
    5200,
    9000,
    8500,
    7000
]

# KDE plot
sns.kdeplot(
    steps,
    fill=True,
    color="green"
)

plt.title("Daily Step Count Distribution")
plt.xlabel("Steps")
plt.ylabel("Density")

plt.show()