import matplotlib.pyplot as plt
import seaborn as sns

def plot_charts(df):

    #  Price + Moving Average + Volume (per coin)
    for coin in df["coin"].unique():
        temp = df[df["coin"] == coin]

        fig, ax1 = plt.subplots(figsize=(10,5))

        # Price line
        ax1.plot(temp["timestamp"], temp["price"], color="blue", label="Price")
        ax1.plot(temp["timestamp"], temp["ma_7"], color="green", label="7-day MA")
        ax1.set_ylabel("Price", color="blue")

        # Volume bars (secondary axis)
        ax2 = ax1.twinx()
        ax2.bar(temp["timestamp"], temp["volume"], alpha=0.3, color="gray", label="Volume")
        ax2.set_ylabel("Volume", color="gray")

        plt.title(f"{coin.upper()} Price + Volume")
        fig.legend(loc="upper left")
        plt.grid()
        plt.show()

    #  Comparison chart (price only)
    plt.figure(figsize=(10,5))
    sns.lineplot(data=df, x="timestamp", y="price", hue="coin")

    plt.title("Crypto Price Comparison")
    plt.grid()
    plt.show()