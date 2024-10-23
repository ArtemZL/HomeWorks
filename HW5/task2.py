import  csv

class Car:
    def __init__(self, cur_number, brand, year):
        self.cur_number = cur_number
        self.brand = brand
        self.year = year

class Opreations:
    def __init__(self, operation_number, operation_name, cost, part_cost = 0):
        self.operation_number = operation_number
        self.operation_name = operation_name
        self.cost = cost
        self.part_cost = part_cost

class ServiceRecord:
    def __init__(self, car_number, operation_number, part_amount = 0):
        self.car_number = car_number
        self.operation_number = operation_number
        self.part_amount = part_amount

def read_cars(file_name):
    cars = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            car_number, brand, year = row
            cars[car_number] = Car(car_number, brand, year)
    return cars

def read_operations(file_name):
    operations = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            operation_number, name, cost, part_cost = row
            operations[operation_number] = Opreations(operation_number, name, float(cost), float(part_cost))
    return operations

def read_service_records(file_name):
    records = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            car_number, operation_number, part_quantity = row
            records.append(ServiceRecord(car_number, operation_number, int(part_quantity)))
    return records

def calculate_total_cost(cars, operations, service_records):
    operation_payments = {}
    operation_car_count = {}
    total_cost = 0

    for record in service_records:
        car = cars[record.car_number]
        operation = operations[record.operation_number]
        operation_cost = operation.cost + (record.part_amount * operation.part_cost)
        total_cost += operation_cost
        if operation.operation_number not in operation_payments:
            operation_payments[operation.operation_number] = 0
        operation_payments[operation.operation_number] += operation_cost
        if operation.operation_number not in operation_car_count:
            operation_car_count[operation.operation_number] = {}
        if car.brand not in operation_car_count[operation.operation_number]:
            operation_car_count[operation.operation_number][car.brand] = 0
        operation_car_count[operation.operation_number][car.brand] += 1

    return total_cost, operation_payments, operation_car_count


def main():
    car_file = "cars.csv"
    operations_file = "operations.csv"
    service_file = "service_records.csv"
    cars = read_cars(car_file)
    operations = read_operations(operations_file)
    service_records = read_service_records(service_file)
    total_payment, operation_payments, operation_car_count = calculate_total_cost(cars, operations, service_records)

    print(f"Total payment for all operations: {total_payment}")

    print("Total payment per operation:")
    for operation_number, payment in operation_payments.items():
        print(f"Operation {operation_number}: {payment}")

    input_operations = input("Enter operations: ")

    if input_operations in operation_car_count:
        print("Car count for operations " + str(input_operations) + "for brand: ")
        for brand, count in operation_car_count[input_operations].items():
            print("Brand: " + brand + ": " + str(count))
    else:
        print("No records found for operation " + input_operations)

if __name__ == "__main__":
    main()



