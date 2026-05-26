from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

class ShopAnalysis:
    def __init__(self, filename):
        self.df = pd.read_json(filename)

    def average_prices(self):
        return self.df.groupby("shop")["price"].mean().to_dict()

    def create_boxplot(self):
        self.df.boxplot(column="price", by="shop")

        plt.title("Price Comparison by Shop")
        plt.suptitle("")
        plt.xlabel("Shop")
        plt.ylabel("Price")

        plt.savefig("boxplot.png")


analysis = ShopAnalysis("prices.json")
а
@app.get("/average-prices")
def get_average_prices():
    return analysis.average_prices()


@app.get("/create-boxplot")
def create_boxplot():
    analysis.create_boxplot()

    return {
        "message": "Boxplot created successfully"
    }