import csv
from datetime import datetime

class GasStation:
    def __init__(self, id, location):
        self.id = id
        self.location = location

class FuelPrice:
    def __init__(self, fuel_type, price):
        self.fuel_type = fuel_type
        self.price = price

class ServiceRecord:
    def __init__(self, station_id, date, fuel_type, volume):
        self.station_id = station_id
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.fuel_type = fuel_type
        self.volume = volume

def load_stations(filename):
    stations = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            station_id, location = row
            stations[station_id] = GasStation(station_id, location)
    return stations

def load_fuel_prices(filename):
    prices = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            fuel_type, price = row
            prices[fuel_type] = FuelPrice(fuel_type, float(price))
    return prices

def load_service_records(filename):
    records = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            station_id, date, fuel_type, volume = row
            records.append(ServiceRecord(station_id, date, fuel_type, float(volume)))
    return records

def calculate_revenue(stations, prices, records):
    revenue_per_station = {station_id: 0 for station_id in stations}

    for record in records:
        if record.fuel_type in prices:
            revenue = record.volume * prices[record.fuel_type].price
            revenue_per_station[record.station_id] += revenue

    for station_id, revenue in revenue_per_station.items():
        print(f"Заправка {station_id} ({stations[station_id].location}): {revenue:.2f} грн")

def calculate_revenue_by_city(records, prices, city, date):
    revenue_by_fuel = {}
    for record in records:
        if record.date == datetime.strptime(date, '%Y-%m-%d') and stations[record.station_id].location == city:
            revenue_by_fuel[record.fuel_type] = revenue_by_fuel.get(record.fuel_type, 0) + record.volume * prices[record.fuel_type].price

    for fuel_type, revenue in revenue_by_fuel.items():
        print(f"Вид пального {fuel_type}: {revenue:.2f} грн")

def calculate_total_drone_fund_by_station(records, prices):
    drone_fund_per_station = {}

    for record in records:
        if record.fuel_type in ["PULLS_95", "PULLS_Diesel"]:
            if record.station_id not in drone_fund_per_station:
                drone_fund_per_station[record.station_id] = 0
            drone_fund_per_station[record.station_id] += record.volume

    for station_id, total_fund in drone_fund_per_station.items():
        print(f"Заправка {station_id} ({stations[station_id].location}): зібрано на дрони {total_fund:.2f} грн")


def calculate_drone_fund(records):
    drone_fund = 0
    for record in records:
        if record.fuel_type in ["PULLS_95", "PULLS_Diesel"] and record.date == datetime.strptime(date, '%Y-%m-%d'):
            print(f"Додаємо {record.volume} з {record.fuel_type} до фонду дронів.")
            drone_fund += record.volume
    print(f"Фонд на дрони: {drone_fund:.2f} грн")

stations = load_stations('stations.csv')
prices = load_fuel_prices('prices.csv')
service_records = []
for service_file in ['service1.csv', 'service2.csv']:
    service_records.extend(load_service_records(service_file))

calculate_revenue(stations, prices, service_records)
city = input("Введіть місто для розрахунку: ")
date = input("Введіть дату (рррр-мм-дд): ")
calculate_revenue_by_city(service_records, prices, city, date)
calculate_drone_fund(service_records)

calculate_total_drone_fund_by_station(service_records, prices)


