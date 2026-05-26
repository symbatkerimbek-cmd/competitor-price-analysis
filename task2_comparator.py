import json

class PriceComparator:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def cheapest_product(self):
        item = min(self.data, key=lambda x: x["price"])
        print("Cheapest product:")
        print(item)

    def average_price(self):
        prices = [item["price"] for item in self.data]
        avg = sum(prices) / len(prices)

        print("Average price:", avg)

comparator = PriceComparator("prices.json")
comparator.cheapest_product()
comparator.average_price()