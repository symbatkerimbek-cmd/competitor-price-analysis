import pandas as pd

class PriceAnalysis:
    def __init__(self, filename):
        self.df = pd.read_json(filename)

    def statistics(self):
        print("MIN PRICE:", self.df["price"].min())
        print("MEAN PRICE:", self.df["price"].mean())
        print("MEDIAN PRICE:", self.df["price"].median())

    def group_by_data(self):
        grouped = self.df.groupby(["product", "shop"])["price"].mean()

        print("\nGROUPBY RESULT:\n")
        print(grouped)

analysis = PriceAnalysis("prices.json")
analysis.statistics()
analysis.group_by_data()