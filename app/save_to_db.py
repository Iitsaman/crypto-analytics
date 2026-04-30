from db_conn import get_connection

def save_to_db(df):
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()

    sql = """
    INSERT INTO crypto_prices (name, price,volume, created_at,returns, ma_7)
    VALUES (%s, %s,%s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(sql, (
            row["coin"],
            row["price"],
            row["volume"],
            row["timestamp"],
            row["return"],
            row["ma_7"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("30-day data saved ✔")