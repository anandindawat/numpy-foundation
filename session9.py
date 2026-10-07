import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent

dates = [
    '2024-06-01 14:30',
    '2024-06-02 09:15',
    '2024-06-03 20:45'
]

df = pd.DataFrame({
    "delivery_time": dates
})

df["delivery_time"] = pd.to_datetime(df["delivery_time"])

print(df)

import pandas as pd
import numpy as np

df = pd.read_csv(BASE_DIR / "orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.day_name()

print(df)

import pandas as pd
import numpy as np

df = pd.read_csv(BASE_DIR / "orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

df = df.set_index("order_date")

weekly_orders = df.resample("W").size()

print(weekly_orders)

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "posted_at": [
        "2024-06-01 10:00:00",
        "2024-06-02 12:30:00",
        "2024-06-03 15:45:00",
        "2024-06-04 08:20:00",
        "2024-06-05 18:10:00"
    ]
})

df["posted_at"] = pd.to_datetime(df["posted_at"], utc=True)

df["posted_at_india"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")

print(df["posted_at_india"].head())

import pandas as pd
import numpy as np

df = pd.read_csv(BASE_DIR / "orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

df["is_weekend"] = df["order_date"].dt.dayofweek >= 5

print(df)