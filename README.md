# End-to-End Sales Data Pipeline using Python, PostgreSQL, FastAPI & Streamlit

##  Project Overview

This project demonstrates a complete End-to-End Data Engineering Pipeline using Python, PostgreSQL, FastAPI, and Streamlit.

The pipeline extracts sales data from a CSV file, performs data cleaning and transformation, loads the cleaned data into PostgreSQL, exposes REST APIs using FastAPI, and visualizes the data through an interactive Streamlit dashboard.

This project simulates a real-world sales analytics system and follows modular software engineering practices.

---

#  Project Architecture

```
Sales Dataset (CSV)
        │
        ▼
Python ETL Pipeline
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
PostgreSQL Database
        │
        ▼
FastAPI REST APIs
        │
        ▼
Streamlit Dashboard
```

---

#  Project Folder Structure

```
End_to_end_pipeline/
│
├── api/
│   └── main.py
│
├── config/
│   └── config.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── raw/
│       └── sales_data.csv
│
├── database/
│
├── docs/
│
├── etl/
│   └── etl_pipeline.py
│
├── logs/
│   └── etl.log
│
├── notebooks/
│
├── scripts/
│
├── tests/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

#  Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | ETL Development |
| PostgreSQL | Database |
| Pandas | Data Cleaning & Processing |
| SQLAlchemy | Database Connectivity |
| FastAPI | REST API Development |
| Streamlit | Dashboard Development |
| Plotly | Interactive Charts |
| Logging | Pipeline Monitoring |

---

#  Features

- Generate Sales Dataset
- Data Cleaning
- Duplicate Removal
- Missing Value Handling
- PostgreSQL Integration
- ETL Pipeline
- Logging
- REST API Development
- Interactive Dashboard
- KPI Cards
- City-wise Sales Analysis
- Top Products Analysis
- Sales by Category
- Daily Sales Trend
- Sidebar Filters
- CSV Download Feature

---

#  Dashboard Features

### KPI Cards

- Total Orders
- Total Sales
- Average Sales

### Interactive Charts

- City-wise Sales
- Top Products
- Sales by Category (Pie Chart)
- Daily Sales Trend (Line Chart)

### Filters

- Date Filter
- City Filter
- Product Filter
- Category Filter

### Export

- Download Filtered Data as CSV

---

#  API Endpoints

## Home

```
GET /
```

Returns

```json
{
  "message": "Sales ETL API is running successfully!"
}
```

---

## Sales Data

```
GET /sales
```

Returns sales records from PostgreSQL.

---

## Summary

```
GET /summary
```

Returns

- Total Orders
- Total Sales
- Average Sales

---

## Customer Sales

```
GET /customer_sales
```

Returns top customers based on sales.

---

## City Sales

```
GET /city_sales
```

Returns city-wise sales summary.

---

## Top Products

```
GET /top_products
```

Returns top selling products.

---

#  Setup Instructions

## 1 Clone Repository

```bash
git clone https://github.com/Poojitha363/end-to-end-data-pipeline.git
```

---

## 2 Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Configure PostgreSQL

Update

```
config/config.py
```

with your PostgreSQL credentials.

---

## 5 Run ETL Pipeline

```bash
python etl/etl_pipeline.py
```

---

## 6 Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## 7 Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Open

```
http://localhost:8501
```

---

#  Dashboard Screenshots

## Home Dashboard

(<img width="1912" height="887" alt="Sales Dashboard" src="https://github.com/user-attachments/assets/ce619157-6713-48b1-81aa-f74f07bce3c9" />)


---

## City-wise Sales

(<img width="1403" height="712" alt="City wise sales" src="https://github.com/user-attachments/assets/f2c1caf9-1965-4d2d-9e2c-60ed1b542727" />
)

---

## Top Products

(<img width="1458" height="682" alt="Top Products" src="https://github.com/user-attachments/assets/7d1f15d0-75a3-41a4-bd49-92ac21d43f8a" />
)

---

## Category Sales

(<img width="1472" height="665" alt="Sales by Category" src="https://github.com/user-attachments/assets/2bab7007-7a34-4d5d-a15a-12ac4422e479" />
)

---

## Daily Sales Trend
(<img width="1521" height="678" alt="Daily Sales Trend" src="https://github.com/user-attachments/assets/01b52b2a-940d-47a3-b799-1ecc5f48f731" />
)


---

#  Future Improvements

- Docker Support
- Apache Airflow Integration
- AWS S3 Data Storage
- Power BI Dashboard
- Authentication
- CI/CD Pipeline
- Automated Testing

---

#  Learning Outcomes

This project demonstrates practical experience in:

- ETL Pipeline Development
- Data Cleaning
- SQL & PostgreSQL
- REST API Development
- Dashboard Development
- Logging
- Data Visualization
- Software Project Structure

---

#  Author

**Poojitha Indirala**

B.Tech CSE From NIT Warangal | Aspiring Data Engineer

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
