class Resource:
    def __init__(self, price, origin):
        self.price = price
        self.origin = origin
        self.price_history = [price]

    def update_price(self, percentage_change):
        self.price += self.price * (percentage_change / 100)
        self.price_history.append(self.price)

    def __repr__(self):
        return f"{self.__class__.__name__} from {self.origin}: ${self.price:.2f}"

class Gold(Resource):
    def __init__(self, origin):
        super().__init__(1000, origin)

class Oil(Resource):
    def __init__(self, origin):
        super().__init__(500, origin)

class Coal(Resource):
    def __init__(self, origin):
        super().__init__(300, origin)

class Country:
    def __init__(self, name):
        self.name = name
        self.resources = {
            "Gold": Gold(name),
            "Oil": Oil(name),
            "Coal": Coal(name)
        }
        self.events_history = []

    def notify(self, event_type, percentage_change_own, percentage_change_others, all_countries):
        self.events_history.append(event_type)
        for country in all_countries:
            for resource in country.resources.values():
                if country.name == self.name:
                    resource.update_price(percentage_change_own)
                else:
                    resource.update_price(percentage_change_others)

    def generate_event(self, event_type, all_countries):
        if event_type in ["EconomicGrowth", "OlympicGames"]:
            self.notify(event_type, 10, -5, all_countries)
        elif event_type in ["Corruption", "Disaster"]:
            self.notify(event_type, -10, 5, all_countries)

def display_resources(countries):
    for country in countries:
        print(f"\nResources for {country.name}:")
        for resource in country.resources.values():
            print(resource)

def find_cheapest_resources(countries, resource_type):
    cheapest_price = None
    cheapest_resources = []

    for country in countries:
        resource = country.resources[resource_type]
        if cheapest_price is None or resource.price < cheapest_price:
            cheapest_price = resource.price
            cheapest_resources = [resource]
        elif resource.price == cheapest_price:
            cheapest_resources.append(resource)
    return cheapest_resources

def find_most_expensive_resource(countries, resource_type):
    most_expensive = None
    expensive_resources = []

    for country in countries:
        resource = country.resources[resource_type]
        if most_expensive is None or resource.price > most_expensive:
            most_expensive = resource.price
            expensive_resources = [resource]
        elif resource.price == most_expensive:
            expensive_resources.append(resource)
    return expensive_resources

def display_price_history(country, resource_type):
    resource = country.resources[resource_type]
    print(f"Price history for {resource.name} in {country.name}: {resource.price_history}")

def display_events_history(country):
    print(f"Events history for {country.name}: {country.events_history}")

def menu():
    country_a = Country("Norway")
    country_b = Country("USA")
    country_c = Country("Japan")
    countries = [country_a, country_b, country_c]

    while True:
        print("\n1. Display all resources")
        print("2. Generate event for a country")
        print("3. Find country with the cheapest resource")
        print("4. Find country with the most expensive resource")
        print("5. Display price history for a resource")
        print("6. Display events history for a country")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            display_resources(countries)

        elif choice == "2":
            country_name = input("Enter country (Norway, USA, Japan): ")
            event_type = input("Enter event (Corruption, Disaster, EconomicGrowth, OlympicGames): ")
            if country_name == "Norway":
                country_a.generate_event(event_type, countries)
            elif country_name == "USA":
                country_b.generate_event(event_type, countries)
            elif country_name == "Japan":
                country_c.generate_event(event_type, countries)

        elif choice == "3":
            resource_type = input("Enter resource type (Gold, Oil, Coal): ")
            cheapest = find_cheapest_resources(countries, resource_type)
            if cheapest:
                print(f"cheapest {resource_type}:")
                for resource in cheapest:
                    print(f"- {resource.origin} with price {resource.price:.2f}")
            else:
                print(f"No {resource_type} found.")

        elif choice == "4":
            resource_type = input("Enter resource type (Gold, Oil, Coal): ")
            most_expensive = find_most_expensive_resource(countries, resource_type)
            if most_expensive:
                print(f"Most expensive {resource_type}:")
                for resource in most_expensive:
                    print(f"- {resource.origin} with price {resource.price:.2f}")
            else:
                print(f"No {resource_type} found.")

        elif choice == "5":
            country_name = input("Enter country (Norway, USA, Japan): ")
            resource_type = input("Enter resource type (Gold, Oil, Coal): ")
            for country in countries:
                if country.name == country_name:
                    display_price_history(country, resource_type)

        elif choice == "6":
            country_name = input("Enter country (Norway, USA, Japan): ")
            for country in countries:
                if country.name == country_name:
                    display_events_history(country)

        elif choice == "7":
            break

        else:
            print("Invalid choice, try again.")
menu()
