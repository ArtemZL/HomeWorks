class Сheck:
    def __init__(self, first_name, last_name, service_cost):
        self.first_name = first_name
        self.last_name = last_name
        self.service_cost = service_cost

    def __str__(self):
        return ("Receipt:" + self.first_name + " " + self.last_name + ", Cost: " + str(self.service_cost))

class Invoice(Сheck):
    def __init__(self, first_name, last_name, service_cost, product_name , delivery_location,  post_office):
        super().__init__(first_name, last_name, service_cost)
        self.post_office = post_office
        self.product_name = product_name
        self.delivery_location = delivery_location
    def __str__(self):
        return ("Invoice: " + self.product_name + ", delivery location: " + self.delivery_location
                +  ", post office: " + str(self.post_office)
                + " , Receiver: " + super().__str__())

class Posting:
    def __init__(self, check, invoice):
        self.check = check
        self.invoice = invoice
    def __str__(self):
        return ("Posting: " + str(self.check) + " " + str(self.invoice))

class Posting_w_delivery_location(Posting):
    def __init__(self, check, invoice, mark_up):
        super().__init__(check, invoice)
        self.mark_up = mark_up

    def total_cost(self):
        return self.invoice.service_cost + (self.invoice.service_cost * self.mark_up / 100)
    def __str__(self):
        return ("Posting with delivery: " + str(self.check) + " " + str(self.invoice)
                + ", mark_up: " + str(self.mark_up) + "%, total cost: " + str(self.total_cost()))

def calculate_service_cost(deliveres):
    total = 0
    for delivery in deliveres:
        isinstance(delivery, Posting)
        total += delivery.check.service_cost
    return total

def list_sorted_deliveries(deliveries):
    return sorted(deliveries, key=lambda delivery: delivery.invoice.delivery_location)

def calculate_total_cost_per_office(deliveres):
    cost_per_office = {}
    for delivery in deliveres:
        office_number = delivery.invoice.post_office
        if office_number not in cost_per_office:
            cost_per_office[office_number] = 0
        cost_per_office[office_number] += delivery.check.service_cost
        if isinstance(delivery, Posting_w_delivery_location):
            cost_per_office[office_number] += delivery.total_cost() - delivery.check.service_cost
    return cost_per_office

deliveries = [
    Posting(Сheck("Artem", "Dubno", 100), Invoice("Jane", "Smith", 100, "Laptop", "Chicago", 1)),
    Posting_w_delivery_location(Сheck("Marta", "Matskiv", 200), Invoice("Peter", "Williams", 200, "Phone", "Brno", 2), 10),
    Posting(Сheck("Ivan", "Rozhid", 150), Invoice("David", "Davis", 150, "Monitor", "Amsterdam", 1)),
]


def menu():
    while True:
        print("\nMenu")
        print("1. calculate_service_cost")
        print("2. list_sorted_deliveries")
        print("3. calculate_total_cost_per_office")
        print("4. exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            total_cost = calculate_service_cost(deliveries)
            print("Total service cost for the store: " + str(total_cost))

        elif choice == "2":
            sorted_deliveres = list_sorted_deliveries(deliveries)
            print("Sorted deliveres: ")
            for delivery in sorted_deliveres:
                print(delivery)

        elif choice == "3":
            total_cost_per_office = calculate_total_cost_per_office(deliveries)
            print("Total cost per office: ")
            for office, total in total_cost_per_office.items():
                print("Post office" + str(office) + ": " + str(total))

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()












