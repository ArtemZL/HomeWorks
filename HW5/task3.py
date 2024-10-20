import csv


TARIFF_RATES = {
    1: 100,
    2: 120,
    3: 150,
}

class Service:
    def __init__(self, service_id, service_name):
        self.service_id = service_id
        self.service_name = service_name

class Employee:
    def __init__(self, employee_id, employee_lname, tariff_grade):
        self.employee_id = employee_id
        self.employee_lname = employee_lname
        self.tariff_grade = int(tariff_grade)

    @property
    def tarife_rate(self):
        return TARIFF_RATES.get(self.tariff_grade, 0)

class WorkRecord:
    def __init__(self, date, service_id, employee_id, hours_worked, fuel_used=0):
        self.date = date
        self.service_id = service_id
        self.employee_id = employee_id
        self.hours_worked = float(hours_worked)
        self.fuel_used = float(fuel_used)

class PaymentCalc:
    COST_OF_FUEL = 55

    def __init__(self, employees, services, work_records):
        self.employees = employees
        self.services = services
        self.work_records = work_records

    def calculate_payment(self):
        total_payment = 0
        for record in self.work_records:
            employee = self.employees[record.employee_id]
            payment_for_hours = employee.tarife_rate * record.hours_worked
            fuel_cost = record.fuel_used * self.COST_OF_FUEL
            total_payment += payment_for_hours + fuel_cost
        return total_payment

    def calculate_employee_payments(self):
        employee_payments = {}
        for record in self.work_records:
            employee = self.employees[record.employee_id]
            payment_for_hours = employee.tarife_rate * record.hours_worked
            fuel_cost = record.fuel_used * self.COST_OF_FUEL
            total_payment = payment_for_hours + fuel_cost

            if employee.employee_id not in employee_payments:
                employee_payments[employee.employee_id] = 0
            employee_payments[employee.employee_id] += total_payment
        return employee_payments

    def calculate_payments_with_without_equipment(self):
        payments_with_equipment = 0
        payments_without_equipment = 0
        for record in self.work_records:
            employee = self.employees[record.employee_id]
            payment_for_hours = employee.tarife_rate * record.hours_worked
            if record.fuel_used > 0:
                fuel_cost = record.fuel_used * self.COST_OF_FUEL
                payments_with_equipment += payment_for_hours + fuel_cost
            else:
                payments_without_equipment += payment_for_hours
        return payments_without_equipment, payments_with_equipment

    def calculate_by_lname(self, lname):
        for employee_id, employee in self.employees.items():
            if employee.employee_lname == lname:
                employee_payments = self.calculate_employee_payments()
                return employee_payments.get(employee_id, 0)
        return None

    def calculate_daily_payments(self):
        daily_payments = {}
        for record in self.work_records:
            date = record.date
            employee = self.employees[record.employee_id]
            payment_for_hours = employee.tarife_rate * record.hours_worked
            fuel_cost = record.fuel_used * self.COST_OF_FUEL if record.fuel_used else 0
            if date not in daily_payments:
                daily_payments[date] = {'with_equipment': 0, 'without_equipment': 0}
            if record.fuel_used > 0:
                daily_payments[date]['with_equipment'] += payment_for_hours + fuel_cost
            else:
                daily_payments[date]['without_equipment'] += payment_for_hours

        return daily_payments

def read_employees(file_name):
    employees = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) < 3:
                continue
            employee_id, lname, tariff_grade = row
            employees[employee_id] = Employee(employee_id, lname, tariff_grade)
    return employees



def read_services(file_name):
    services = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) < 2:
                continue
            service_id, service_name = row
            services[service_id] = Service(service_id, service_name)
    return services



def read_work_records(file_name):
    work_records = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) < 5:
                continue
            date, service_id, employee_id, hours_worked, fuel_used = row
            work_records.append(WorkRecord(date, service_id, employee_id, hours_worked, fuel_used))
    return work_records


def main():
    employees_file = "employees.csv"
    services_file = "services.csv"
    work_records_file = "work_records.csv"

    employees = read_employees(employees_file)
    services = read_services(services_file)
    work_records = read_work_records(work_records_file)
    calculation = PaymentCalc(employees, services, work_records)

    total_payment = calculation.calculate_payment()
    payments_without_equipment, payments_with_equipment = calculation.calculate_payments_with_without_equipment()

    print(f"Total Payment for all employees: {total_payment}")
    lname = input("Enter last name of the employee: ")
    payment = calculation.calculate_by_lname(lname)
    if payment is not None:
        print(f"Payment for {lname} is: {payment}")
    else:
        print(f"Employee with last name {lname} not found")

    daily_payments = calculation.calculate_daily_payments()
    for date, payments in daily_payments.items():
        print(f"Date: {date}")
        print(f"  Without equipment: {payments['without_equipment']}")
        print(f"  With equipment: {payments['with_equipment']}")

if __name__ == '__main__':
    main()
