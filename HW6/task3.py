import csv
from datetime import datetime

class ComputerType:
    def __init__(self, comp_id, brand, price):
        self.comp_id = comp_id
        self.brand = brand
        self.price = float(price)

class OperatingSystem:
    def __init__(self, os_id, name, price):
        self.os_id = os_id
        self.name = name
        self.price = float(price)

class Receipt:
    def __init__(self, date, comp_id, os_id, quantity):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.comp_id = int(comp_id)
        self.os_id = int(os_id)
        self.quantity = int(quantity)

class SalesManager:
    def __init__(self):
        self.computer_types = {}
        self.operating_systems = {}
        self.receipts = []

    def load_computer_types(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                comp_id, brand, price = row
                self.computer_types[int(comp_id)] = ComputerType(comp_id, brand, price)

    def load_operating_systems(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                os_id, name, price = row
                self.operating_systems[int(os_id)] = OperatingSystem(os_id, name, price)

    def load_receipts(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                date, comp_id, os_id, quantity = row
                self.receipts.append(Receipt(date, comp_id, os_id, quantity))

    def calculate_total_sales(self):
        total_sales = 0
        for receipt in self.receipts:
            comp = self.computer_types[receipt.comp_id]
            os = self.operating_systems.get(receipt.os_id, OperatingSystem(0, "No OS", 0))
            total_sales += receipt.quantity * (comp.price + os.price)
        return total_sales

    def calculate_sales_per_brand(self):
        sales_per_brand = {}
        for receipt in self.receipts:
            comp = self.computer_types[receipt.comp_id]
            os = self.operating_systems.get(receipt.os_id, OperatingSystem(0, "No OS", 0))
            if comp.brand not in sales_per_brand:
                sales_per_brand[comp.brand] = 0
            sales_per_brand[comp.brand] += receipt.quantity * (comp.price + os.price)
        return sales_per_brand

    def calculate_sales_per_os_for_brand(self, brand):
        sales_per_os = {}
        for receipt in self.receipts:
            comp = self.computer_types[receipt.comp_id]
            if comp.brand == brand:
                os = self.operating_systems.get(receipt.os_id, OperatingSystem(0, "No OS", 0))
                if os.name not in sales_per_os:
                    sales_per_os[os.name] = 0
                sales_per_os[os.name] += receipt.quantity * (comp.price + os.price)
        return sales_per_os

manager = SalesManager()
manager.load_computer_types("computer_types.csv")
manager.load_operating_systems("operating_systems.csv")
manager.load_receipts("receipts_part1.csv")
manager.load_receipts("receipts_part2.csv")
print("Загальна вартість проданої техніки:", manager.calculate_total_sales())
print("Вартість проданої техніки по марках:", manager.calculate_sales_per_brand())
brand = input("Введіть марку для обчислення вартості по ОС: ")
print(f"Вартість для марки {brand} по ОС:", manager.calculate_sales_per_os_for_brand(brand))
