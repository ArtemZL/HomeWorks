class Product:
    def __init__(self, name, price, amount, id, category):
        self.name = name
        self.price = price
        self.amount = amount
        self.id = id
        self.category = category
    def print(self):
        print("Id: " + str(self.id) + ", Name: " + self.name +
              ", Price: " + str(self.price) + ", Amount: " + str(self.amount))


class Manager:
    def __init__(self):
        self.products = []

    def print_all(self):
        if not self.products:
            print("There are no products")
        for product in self.products:
            product.print()

    def print_category(self, category):
        found = False
        for product in self.products:
            if product.category == category:
                product.print()
                found = True
        if not found:
            print("There is no category")

    def print_by_price(self, price):
        found = False
        for product in self.products:
            if product.price > price:
                product.print()
                found = True
        if not found:
            print("There is no product")

    def print_by_less_price(self, price):
        found = False
        for product in self.products:
            if product.price < price:
                product.print()
                found = True
        if not found:
            print("There is no product")

    def add_product(self, name, price, amount, id, category):
        self.products.append(Product(name, price, amount, id, category))
        print("Product added successfully")

    def remove_product(self, id, number):
        for product in self.products:
            if product.id == id:
                if product.amount >= number:
                    product.amount -= number
                    print("Product removed successfully")
                    return
                else:
                    print("Product not removed successfully")
                    return
        print("Product not removed")

    def total_value(self):
        for product in self.products:
            total = product.price * product.amount
        print("Total value is: " + total)

    def print_by_amount(self, amount):
        found = False
        for product in self.products:
            if product.amount > amount:
                product.print()
        if not found:
            print("There is no product")

    def print_by_less_amount(self, amount):
        found = False
        for product in self.products:
            if product.amount < amount:
                product.print()
                found = True
        if not found:
            print("There is no product")

    def purchase_product(self, id, number):
        for product in self.products:
            if product.id == id:
                product.amount += number
                print("Product " + product.id + " purchased successfully")
                return
        print("Product not purchased")

def menu():
    print("""
    Menu:
    a. print all products
    b. print products by category
    c. print products with price more than N
    d. print products with price less than N
    e. print products with amount more than N
    f. print products with amount less than N
    g. Add new product
    h. Add multiple products
    i. Remove products (sell)
    j. Display total value of products
    k. Exit
    """)

def main():
    manager = Manager()
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "k":
            print("Thank you for using our program!")
            break

        if choice == "a":
            manager.print_all()
        elif choice == "b":
            category = input("Enter category: ")
            manager.print_category(category)

        elif choice == "c":
            price = float(input("Enter price: "))
            manager.print_by_price(price)

        elif choice == "d":
            price = float(input("Enter price: "))
            manager.print_by_less_price(price)

        elif choice == "e":
            amount = float(input("Enter amount: "))
            manager.print_by_amount(amount)

        elif choice == "f":
            amount = float(input("Enter amount: "))
            manager.print_by_less_amount(amount)

        elif choice == "g":
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            amount = int(input("Enter amount: "))
            manager.add_product(name, price, amount, id, category)

         elif choice == "h":
            id = int(input("Enter id: "))
            number = int(input("Enter number: "))
            manager.purchase_product(id, number)

        elif choice == "i":
            id = int(input("Enter id: "))
            number = int(input("Enter number to sell: "))
            manager.remove_product(id, number)

        elif choice == "j":
            manager.total_value()

        else:
            print("Invalid input")
if __name__ == "__main__":
    main()



















