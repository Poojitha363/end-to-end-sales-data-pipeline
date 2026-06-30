import logging
import os
import sys

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USERNAME,
)

# Logging setup
log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
log_file = os.path.join(log_dir, "etl.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

# PostgreSQL connection settings
username = DB_USERNAME
password = DB_PASSWORD
host = DB_HOST
port = DB_PORT
database = DB_NAME


def load_sales_data() -> pd.DataFrame:
    """Load sales data from PostgreSQL into a pandas DataFrame."""

    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )

    try:
        engine = create_engine(db_url, pool_pre_ping=True)

        with engine.connect() as connection:
            table_exists = connection.execute(
                text("SELECT to_regclass('public.sales_data')")
            ).scalar()

            if not table_exists:
                raise RuntimeError(
                    "The 'sales_data' table does not exist in the database."
                )

            query = "SELECT * FROM sales_data"
            df = pd.read_sql(query, connection)

        return df

    except Exception as exc:
        raise RuntimeError(
            f"Failed to load data from PostgreSQL: {exc}"
        ) from exc


if __name__ == "__main__":
    logging.info("ETL Pipeline Started")
    try:
        df = load_sales_data()
        logging.info(f"Data loaded successfully. Total rows: {len(df)}")

        df = df.drop_duplicates()
        df = df.dropna()

        if "order_date" in df.columns:
            df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
            df = df.dropna(subset=["order_date"])

        logging.info(f"Data cleaned successfully. Rows after cleaning: {len(df)}")

        engine = create_engine(
            URL.create(
                drivername="postgresql+psycopg2",
                username=username,
                password=password,
                host=host,
                port=port,
                database=database,
            ),
            pool_pre_ping=True,
        )

        df.to_sql("clean_sales", engine, if_exists="replace", index=False)
        logging.info("Data loaded into clean_sales table successfully")
    except Exception as exc:
        logging.error(f"Error occurred: {exc}")
    finally:
        logging.info("ETL Pipeline Execution Completed")