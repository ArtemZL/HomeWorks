import csv

class Reading:
    def __init__(self, day_current, day_previous, night_current, night_previous):
        self.day_current = day_current
        self.day_previous = day_previous
        self.night_current = night_current
        self.night_previous = night_previous

    @property
    def consumption_day(self):
        return self.day_current - self.day_previous
    @property
    def consumption_night(self):
        return self.night_current - self.night_previous
    @property
    def total_consumption(self):
        return self.consumption_day + self.consumption_night

class ElectricCounter(Reading):
    def __init__(self, apartment_number, month, day_current, day_previous, night_current, night_previous):
        super().__init__(day_current, day_previous, night_current, night_previous)
        self.apartment_number = apartment_number
        self.month = month

def load_data_from_csv(file_paths):
    counters = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                apartment_number = int(row['Apartment'])
                month = int(row['Month'])

                # Створюємо об'єкт ElectricCounter як нащадок Reading
                counter = ElectricCounter(
                    apartment_number=apartment_number,
                    month=month,
                    day_current=float(row['DayCurrent']),
                    day_previous=float(row['DayPrevious']),
                    night_current=float(row['NightCurrent']),
                    night_previous=float(row['NightPrevious'])
                )
                counters.append(counter)

    return counters

def build_combined_table_and_check_data(counters):
    print("Перевірка даних та побудова загальної таблиці:")
    errors_found = False
    for counter in counters:
        if counter.day_current < counter.day_previous or counter.night_current < counter.night_previous:
            errors_found = True
            print(f"Помилка: Квартира {counter.apartment_number}, Місяць {counter.month} - "
                  f"Поточні показники менші за попередні.")

    if not errors_found:
        print("Усі дані коректні. Поточні показники не менші за попередні.")
    else:
        print("Знайдено некоректні дані.")

def get_monthly_report(counters, target_month):
    print(f"Дані для місяця {target_month}:")
    monthly_data = [c for c in counters if c.month == target_month]

    for counter in monthly_data:
        print(f"Квартира {counter.apartment_number}: "
              f"День - {counter.consumption_day} кВт/год, "
              f"Ніч - {counter.consumption_night} кВт/год, "
              f"Сумарно - {counter.total_consumption} кВт/год")

def get_total_consumption(counters):
    total_day = sum(c.consumption_day for c in counters)
    total_night = sum(c.consumption_night for c in counters)

    print("Загальне споживання електрики:")
    print(f"День: {total_day} кВт/год")
    print(f"Ніч: {total_night} кВт/год")
    print(f"Сумарно: {total_day + total_night} кВт/год")

def get_quarterly_cost(counters, day_rate, night_rate):
    quarterly_data = {1: [], 2: [], 3: [], 4: []}

    for counter in counters:
        quarter = (counter.month - 1) // 3 + 1
        quarterly_data[quarter].append(counter)

    print("Вартість спожитої електрики по кварталах:")
    for quarter, data in quarterly_data.items():
        if data:
            total_day = sum(c.consumption_day for c in data)
            total_night = sum(c.consumption_night for c in data)

            cost_day = total_day * day_rate
            cost_night = total_night * night_rate
            total_cost = cost_day + cost_night

            print(f"Квартал {quarter}: Вартість вдень - {cost_day} грн, "
                  f"Вартість вночі - {cost_night} грн, "
                  f"Сумарна вартість - {total_cost} грн")

def get_max_monthly_consumption(counters):
    max_consumption = {}
    for counter in counters:
        if counter.apartment_number not in max_consumption:
            max_consumption[counter.apartment_number] = {
                "day": (counter.month, counter.consumption_day),
                "night": (counter.month, counter.consumption_night),
                "total": (counter.month, counter.total_consumption)
            }
        else:
            if counter.consumption_day > max_consumption[counter.apartment_number]["day"][1]:
                max_consumption[counter.apartment_number]["day"] = (counter.month, counter.consumption_day)
            if counter.consumption_night > max_consumption[counter.apartment_number]["night"][1]:
                max_consumption[counter.apartment_number]["night"] = (counter.month, counter.consumption_night)
            if counter.total_consumption > max_consumption[counter.apartment_number]["total"][1]:
                max_consumption[counter.apartment_number]["total"] = (counter.month, counter.total_consumption)

    print("Найбільше місячне споживання для кожної квартири:")
    for apartment, data in max_consumption.items():
        print(f"Квартира {apartment}: "
              f"Максимум вдень - {data['day'][1]} кВт/год у місяці {data['day'][0]}, "
              f"Максимум вночі - {data['night'][1]} кВт/год у місяці {data['night'][0]}, "
              f"Максимум сумарно - {data['total'][1]} кВт/год у місяці {data['total'][0]}")
def main():
    file_paths = ["data1.csv", "data2.csv"]
    counters = load_data_from_csv(file_paths)

    while True:
        print("\nМеню:")
        print("1. Перевірка даних та побудова загальної таблиці")
        print("2. Дані для конкретного місяця")
        print("3. Загальна кількість спожитої електрики у всьому будинку")
        print("4. Вартість спожитої електрики по кварталах")
        print("5. Найбільше місячне споживання для кожної квартири")
        print("0. Вихід")
        choice = input("Введіть номер опції: ")

        if choice == "1":
            build_combined_table_and_check_data(counters)
        elif choice == "2":
            month = int(input("Введіть номер місяця (1-12): "))
            get_monthly_report(counters, month)
        elif choice == "3":
            get_total_consumption(counters)
        elif choice == "4":
            day_rate = float(input("Введіть вартість за кВт/год вдень: "))
            night_rate = float(input("Введіть вартість за кВт/год вночі: "))
            get_quarterly_cost(counters, day_rate, night_rate)
        elif choice == "5":
            get_max_monthly_consumption(counters)
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")
if __name__ == "__main__":
    main()
