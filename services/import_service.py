import csv
import json
from repositories.customer_repository import CustomerRepository
from repositories.car_repository import CarRepository

class ImportService:

    def import_customers_csv(self, path: str):
        repo = CustomerRepository()
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                repo.add(row["name"], row["email"])

    def import_cars_json(self, path: str):
        repo = CarRepository()
        with open(path, encoding="utf-8") as f:
            cars = json.load(f)
            for car in cars:
                repo.add(
                    car["brand"],
                    car["model"],
                    float(car["price"]),
                    car["fuel"]
                )
