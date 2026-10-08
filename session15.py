import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("spotify_top_100.csv")

# Generate profile report
profile = ProfileReport(
    df,
    title="Spotify Top 100 Songs Profile Report",
    explorative=True
)

# Save HTML report
profile.to_file("spotify_profile_report.html")

print("Profile report generated successfully!")


import pandas as pd
import sweetviz as sv

# Load datasets
mumbai = pd.read_csv("zomato_mumbai.csv")
delhi = pd.read_csv("zomato_delhi.csv")

# Generate comparison report
report = sv.compare(
    [mumbai, "Mumbai"],
    [delhi, "Delhi"]
)

# Save report
report.show_html("zomato_mumbai_vs_delhi.html")

print("Comparison report generated successfully!")

import pandas as pd
import dtale 

df = pd.read_csv("myntra_products.csv")

d = dtale.show(df)

d


import pandas as pd
# from ydata_profiling import ProfileReport

# Load Swiggy food order dataset
df = pd.read_csv("swiggy_food_orders.csv")

# Generate EDA report
profile = ProfileReport(
    df,
    title="Swiggy Food Orders Auto EDA Report",
    explorative=True
)

# Save report
profile.to_file("swiggy_eda_report.html")

print("Swiggy EDA report generated successfully!")