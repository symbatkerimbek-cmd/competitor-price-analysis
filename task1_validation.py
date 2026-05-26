import json

class PriceValidator:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def validate(self):
        data = self.load_data()

        for item in data:
            if (
                "product" in item and
                "shop" in item and
                "price" in item and
                isinstance(item["price"], int)
            ):
                print("Correct:", item)
            else:
                print("Error:", item)

validator = PriceValidator("prices.json")
validator.validate()