from api import get_crypto_data
from save_to_db import save_to_db
from export_to_excel import export
import pandas as pd
from charts import plot_charts

def main():
    print("🚀 Starting Crypto Analytics Project")

    #   Define coins
    coins = ["bitcoin", "ethereum"]

    #  Fetch data
    dfs = []

    for coin in coins:
        df = get_crypto_data(coin)
        dfs.append(df)

    #  Combine dataset
    final_df = pd.concat(dfs, ignore_index=True)

    if final_df.empty:
        print("❌ No data fetched")
        return

    print("📡 Data fetched successfully")

    #  Analytics 
    final_df["return"] = final_df.groupby("coin")["price"].pct_change()
    final_df["ma_7"] = final_df.groupby("coin")["price"].transform(
        lambda x: x.rolling(7).mean()
    )

    #  Plot charts 
    plot_charts(final_df)

    #   Save to DB
    save_to_db(final_df)

    #   Export to Excel
    export()

    print("✅ Project Completed Successfully")


if __name__ == "__main__":
    main()