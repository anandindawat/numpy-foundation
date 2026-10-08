import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

# Create pairplot
sns.pairplot(tips)

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load flights dataset
flights = sns.load_dataset("flights")

# Reshape data using pivot_table
flights_pivot = flights.pivot_table(
    index="month",
    columns="year",
    values="passengers"
)

# Create heatmap
sns.heatmap(
    flights_pivot,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Number of Passengers by Month and Year")
plt.xlabel("Year")
plt.ylabel("Month")

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load fmri dataset
fmri = sns.load_dataset("fmri")

# Create relplot
sns.relplot(
    data=fmri,
    x="timepoint",
    y="signal",
    hue="event",
    kind="line"
)

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# Catplot for survival rate
sns.catplot(
    data=titanic,
    x="class",
    y="survived",
    kind="bar",
    errorbar="ci"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Jointplot with regression line
sns.jointplot(
    data=penguins,
    x="bill_length_mm",
    y="flipper_length_mm",
    kind="reg"
)

plt.show()