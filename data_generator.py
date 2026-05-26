import json
import random

class DataGenerator:
    def __init__(self):
        self.products = ["Laptop", "Phone", "Tablet", "Headphones"]
        self.shops = ["TechStore", "MegaShop", "ITMarket"]

    def generate_prices(self, count=20):
        data = []

        for _ in range(count):
            item = {
                "product": random.choice(self.products),
                "shop": random.choice(self.shops),
                "price": random.randint(50000, 700000)
            }
            data.append(item)

        return data

    def save_to_json(self, filename="prices.json"):
        data = self.generate_prices()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"{filename} created successfully!")

generator = DataGenerator()
generator.save_to_json()