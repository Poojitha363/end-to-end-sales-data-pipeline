from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()

engine = create_engine(
    "postgresql+psycopg2://postgres:Poojitha@789@localhost:5432/sales_data"
)

@app.get("/")
def home():
    return {"message": "Sales ETL API is running successfully!"}

@app.get("/sales")
def get_sales():
    query = "SELECT * FROM sales_data LIMIT 100"
    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")