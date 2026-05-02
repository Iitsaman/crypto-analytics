# Crypto Analytics Dashboard

An end-to-end data analytics and data engineering project that fetches Bitcoin and Ethereum data, stores it in a PostgreSQL database, and visualizes it through Streamlit and Power BI dashboards.

# Live Dashboard

🔗 [Click here to view live dashboard](https://live-crypto-analytics.streamlit.app/)

## Tech Stack

- Python
- PostgreSQL
- Pandas
- Streamlit
- Power BI
- Matplotlib
- CoinGecko API

## Features

- Fetches hourly Bitcoin and Ethereum price and volume data from CoinGecko API
- Stores 700+ records in PostgreSQL database
- Calculates 7-day moving average and hourly returns
- Interactive web dashboard built with Streamlit deployed on cloud
- Business intelligence dashboard built with Power BI
- Automated daily data pipeline using Windows Task Scheduler
- Excel export for offline analysis

## Project Structure

```text
crypto-analytics/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── charts.py
│   ├── db_conn.py
│   ├── save_to_db.py
│   ├── export_to_excel.py
│   └── dashboard.py
├── screenshots/
├── run_crypto.bat
├── requirements.txt
├── .gitignore
└── README.md
```

## Screenshots

### Streamlit Dashboard

![Streamlit Price Chart](screenshots/streamlit.png)

### Power BI Dashboard

![Power BI Dashboard](screenshots/powerbi_combined.png)

## How to Run

### 1. Clone the repository

```
git clone https://github.com/yourusername/crypto-analytics.git
```

### 2. Create virtual environment

```
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:

```
DB_HOST=localhost
DB_NAME=crypto_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_PORT=5432
```

### 5. Set up PostgreSQL database

```sql
CREATE TABLE crypto_prices (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50),
    price NUMERIC(18,8),
    volume NUMERIC(18,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

);
```

### 6. Run the pipeline

```
python main.py
```

### 7. Run the dashboard

```
streamlit run dashboard.py
```

## Key Insights

- Bitcoin and Ethereum prices are highly correlated — both peaked on April 17
- Ethereum volume spiked 2x on April 15 coinciding with price increase
- 7-day moving average stayed close to price indicating stable trend in April

## What I Learned

- Building automated end to end data pipelines
- Storing and querying data with PostgreSQL
- Data analysis and transformation with Pandas
- Building interactive dashboards with Streamlit
- Business intelligence reporting with Power BI
- Scheduling automated tasks with Windows Task Scheduler
