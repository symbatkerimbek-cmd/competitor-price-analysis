import json
import random

class JSONPriceGenerator:
    def __init__(self):
        self.products = ["Mouse", "Keyboard", "Monitor"]
        self.shops = ["ShopA", "ShopB", "ShopC"]

    def generate(self):
        result = []

        for _ in range(10):
            result.append({
                "product": random.choice(self.products),
                "shop": random.choice(self.shops),
                "price": random.randint(3000, 150000)
            })

        return result

    def save(self, filename="generated_prices.json"):
        data = self.generate()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("JSON file saved!")


generator = JSONPriceGenerator()
generator.save()