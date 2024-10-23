import csv
TARIFFS = {
    'cold_water_price': 15.0,
    'hot_water_price': 30.0,
    'heating_price': 5.0,
}

class Flat:
    def __init__(self, flat_id, flat_number, house_number):
        self.flat_id = flat_id
        self.flat_number = flat_number
        self.house_number = house_number

class ColdWaterUsage:
    def __init__(self, flat_id, month, cold_water_volume):
        self.flat_id = flat_id
        self.month = month
        self.cold_water_volume = float(cold_water_volume)

class HotWaterUsage:
    def __init__(self, flat_id, month, hot_water_volume, heating_gcal):
        self.flat_id = flat_id
        self.month = month
        self.hot_water_volume = float(hot_water_volume)
        self.heating_gcal = float(heating_gcal)

class PaymentCalc:
    def __init__(self, flats, cold_water_usages, hot_water_usages):
        self.flats = flats
        self.cold_water_usages = cold_water_usages
        self.hot_water_usages = hot_water_usages

    def calculate_monthly_house_payment(self, month):
        house_report = {}
        for flat in self.flats:
            cold_total = 0
            hot_total = 0
            for cold_usage in self.cold_water_usages:
                if cold_usage.flat_id == flat.flat_id and cold_usage.month == month:
                    cold_total += cold_usage.cold_water_volume * TARIFFS['cold_water_price']
            for hot_usage in self.hot_water_usages:
                if hot_usage.flat_id == flat.flat_id and hot_usage.month == month:
                    hot_total += (hot_usage.hot_water_volume * TARIFFS['hot_water_price']) + \
                                 (hot_usage.heating_gcal * TARIFFS['heating_price'])

            if flat.house_number not in house_report:
                house_report[flat.house_number] = {'cold_total': 0, 'hot_total': 0}

            house_report[flat.house_number]['cold_total'] += cold_total
            house_report[flat.house_number]['hot_total'] += hot_total

        return house_report

    def calculate_total_costs(self):
        total_costs = {}
        for flat in self.flats:
            cold_total = 0
            hot_total = 0
            for cold_usage in self.cold_water_usages:
                if cold_usage.flat_id == flat.flat_id:
                    cold_total += cold_usage.cold_water_volume * TARIFFS['cold_water_price']
            for hot_usage in self.hot_water_usages:
                if hot_usage.flat_id == flat.flat_id:
                    hot_total += (hot_usage.hot_water_volume * TARIFFS['hot_water_price']) + \
                                 (hot_usage.heating_gcal * TARIFFS['heating_price'])

            if flat.house_number not in total_costs:
                total_costs[flat.house_number] = {'total_cold': 0, 'total_hot': 0}
            total_costs[flat.house_number]['total_cold'] += cold_total
            total_costs[flat.house_number]['total_hot'] += hot_total

        return total_costs

    def calculate_flats_payments(self, month):
        flats_payments = {}
        for flat in self.flats:
            cold_payment = 0
            hot_payment = 0
            for cold_usage in self.cold_water_usages:
                if cold_usage.flat_id == flat.flat_id and cold_usage.month == month:
                    cold_payment = cold_usage.cold_water_volume * TARIFFS['cold_water_price']
            for hot_usage in self.hot_water_usages:
                if hot_usage.flat_id == flat.flat_id and hot_usage.month == month:
                    hot_payment = (hot_usage.hot_water_volume * TARIFFS['hot_water_price']) + \
                                  (hot_usage.heating_gcal * TARIFFS['heating_price'])

            flats_payments[flat.flat_id] = {'cold_payment': cold_payment, 'hot_payment': hot_payment}

        return flats_payments


def read_flats(file_name):
    flats = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            flat_id, house_number, flat_number = row
            flats.append(Flat(flat_id, house_number, flat_number))
    return flats


def read_cold_water_usages(file_name):
    usages = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            flat_id, month, cold_water_volume = row
            usages.append(ColdWaterUsage(flat_id, month, cold_water_volume))
    return usages


def read_hot_water_usages(file_name):
    usages = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            flat_id, month, hot_water_volume, heating_gcal = row
            usages.append(HotWaterUsage(flat_id, month, hot_water_volume, heating_gcal))
    return usages


def main():
    # Ім'я файлів CSV
    flats_file = "flats.csv"
    cold_water_usages_file = "cold_water_usages.csv"
    hot_water_usages_file = "hot_water_usages.csv"

    flats = read_flats(flats_file)
    cold_water_usages = read_cold_water_usages(cold_water_usages_file)
    hot_water_usages = read_hot_water_usages(hot_water_usages_file)

    payment_system = PaymentCalc(flats, cold_water_usages, hot_water_usages)
    total_costs = payment_system.calculate_total_costs()


    print("Total water cost by houses:")
    for house_number, costs in total_costs.items():
        total_cost = costs['total_cold'] + costs['total_hot']
        print("House " + str(house_number) + ": " + str(round(total_cost, 2)) + " UAH")
    print('-' * 60)

    month = input("Enter the month: ")
    monthly_house_report = payment_system.calculate_monthly_house_payment(month)

    print("Monthly payment for cold and hot water by houses:")
    for house_number, totals in monthly_house_report.items():
        print("House " + str(house_number) + ":")
        print("  " + month + ": cold water - " + str(round(totals['cold_total'], 2)) + " UAH, hot water - " + str(
            round(totals['hot_total'], 2)) + " UAH")
    print('-' * 60)

    flats_payments = payment_system.calculate_flats_payments(month)
    print("Payments for " + month + ":")
    for flat_id, payments in flats_payments.items():
        flat = next(f for f in flats if f.flat_id == flat_id)
        print("House " + str(flat.house_number) + ":")
        print("  Flat " + str(flat.flat_number) + ": cold water - " + str(
            round(payments['cold_payment'], 2)) + " UAH, hot water - " + str(
            round(payments['hot_payment'], 2)) + " UAH")
    print('-' * 60)


if __name__ == '__main__':
    main()

