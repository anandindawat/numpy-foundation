# Task 1: Connect to database and load 'restaurants' table (first 5 rows)
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost:3306/hotel')
df_restaurants = pd.read_sql('SELECT * FROM restaurant', con=engine)
print(df_restaurants.head())

# Task 2: Fetch 'name' and 'rating' from 'movies' where rating > 8
engine = create_engine("mysql+pymysql://root:@localhost:3306/movies")
query = "SELECT name, rating FROM movies WHERE rating > 8"
df_movies = pd.read_sql_query(query, con=engine)
print(df_movies)


# Task 3: Read JSON from URL and print 'username' column
url = "https://jsonplaceholder.typicode.com/users"
df_users = pd.read_json(url)
print(df_users['username'])

# Task 4: Load CSVs using pathlib, merge on 'user_id', display username and amount
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
orders_path = BASE_DIR / "orders.csv"
users_path = BASE_DIR / "users.csv"

orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

merged = pd.merge(orders, users, on="user_id")
print(merged[["username", "amount"]])


# Task 5: Concatenate DataFrames and reset index
today_orders = pd.DataFrame({
    'order_id': [101, 102],
    'amount': [250.50, 120.00]
})
yesterday_orders = pd.DataFrame({
    'order_id': [99, 100],
    'amount': [300.00, 150.75]
})

combined_orders = pd.concat([today_orders, yesterday_orders], ignore_index=True)
print(combined_orders)