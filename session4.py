import os
import pandas as pd

# Ensure script working directory matches file location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load CSV file
df_ipl = pd.read_csv("ipl_scores.csv")

# Print first 5 rows
print(df_ipl.head())


import pandas as pd

# Load JSON file
df_songs = pd.read_json("songs.json")

# Show column names and data types
print(df_songs.info())


import pandas as pd

# Load TSV file with tab separator
df_zomato = pd.read_csv("zomato_data.tsv", sep="\t")

# Summary statistics
print(df_zomato.describe(include='all'))


import pandas as pd

# Read CSV file in chunks (Note: pd.read_csv supports chunksize)
for chunk in pd.read_csv("flipkart_products.csv", chunksize=2):
    print("Rows in this chunk:", len(chunk))


import pandas as pd

# Load CSV file with semicolon separator
df_paytm = pd.read_csv("paytm_transactions.csv", sep=";")

# Detect missing values
null_columns = df_paytm.columns[df_paytm.isnull().any()]
print("Columns with null values:", null_columns.tolist())
