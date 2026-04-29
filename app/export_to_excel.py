import pandas as pd
from db_conn import get_connection

def export(filename="crypto_da1.xlsx"):
    conn = get_connection()

    if conn is None:
        print("❌ Database connection failed")
        return

    try:
        query = "SELECT * FROM crypto_prices"
        df = pd.read_sql(query, conn)

        if df.empty:
            print("⚠️ No data to export")
            return

        df.to_excel(filename, index=False)

        print("📊 Exported to Excel ✔")

    except Exception as e:
        print("❌ Export error:", e)

    finally:
        conn.close()