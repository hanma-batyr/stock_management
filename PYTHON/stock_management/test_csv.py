/*-import csv
from uuid import UUID
from datetime import datetime, timedelta  # Добавлены импорты

users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"

with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    for user in users:
        user_id = user["user_id"]
        try:
            user_id = UUID(user_id)
            print(user_id)
        except ValueError:
            print("Неверный тип данных UUID")

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    for stock in stocks:
        stock_id = stock["stock_id"]
        try:
            stock_id = int(stock_id)
            print(stock_id)
        except ValueError:
            print("Неверный тип данных int")

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    print("Стокс: ")
    for stock in stocks:
        stocks_id = stock["stock_id"]
        capacity_sq_m = stock["capacity_sq_m"]
        owner_id = stock["owner_id"]

        try:
            stocks_id = int(stocks_id)
        except ValueError:
            print("Неверный тип данных int")
        try:
            capacity_sq_m = float(capacity_sq_m)
        except ValueError:
            print("Неверный тип данных float")
        try:
            owner_id = UUID(owner_id)
        except ValueError:
            print("Неверный тип данных UUID")

with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    print("Итемс: ")
    for item in items:
        item_id = item["item_id"]
        stock_id = item["stock_id"]
        size = item["size"]
        arrive_at = item["arrive_at"]
        expiration_time = item["expiration_time"]

        try:
            item_id = int(item_id)
        except ValueError:
            print("Неверный тип данных int")
        try:
            stock_id = int(stock_id)
        except ValueError:
            print("Неверный тип данных int")
        try:
            size = float(size)
        except ValueError:
            print("Неверный тип данных float")
        try:
            arrive_at = datetime.strptime(arrive_at, "%Y-%m-%d")
        except ValueError:
            print("Неверный тип данных datetime")
        try:
            expiration_time = timedelta(hours=float(expiration_time))
        except ValueError:
            print("Неверный тип данных timedelta")
