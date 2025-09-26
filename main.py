# Project_template/main.py

import pandas as pd
from loguru import logger
import duckdb
from pathlib import Path

from helpers.utils import make_soup
from helpers.utils import parse_page

db_path = Path.cwd() / "results.db"
disk_path = Path.cwd() / "results.parquet"
logger.info(f"disk_path is {disk_path}")


def save_disk(df_: pd.DataFrame) -> None:
    df.to_parquet(disk_path, engine="pyarrow", index=False)


url = "https://www.villagehatshop.com/collections/mens-outback-hats"

soup = make_soup(url)
results = []
hats = soup.find_all("li", class_="grid__item")
results = parse_page(hats, results)

df = pd.DataFrame(results)

save_disk(df)
conn = duckdb.connect()

conn.sql("""
    CREATE TABLE IF NOT EXISTS hats AS SELECT * FROM df;
""")

# just to check the above table exists
df2 = conn.sql("""
    SELECT * FROM hats;
""").to_df()
print(df2.info())
