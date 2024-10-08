from datetime import datetime


class User:
    def __init__(self, userId, firstName, lastName, Email, Phone):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.Email = Email
        self.Phone = Phone

    def __str__(self):
        return f"{self.firstName} {self.lastName} (ID: {self.userId})"


class Product:
    def __init__(self, ProductId, CategoryId, Model, Year, Price, Color):
        self.ProductId = ProductId
        self.CategoryId = CategoryId
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Color = Color

    def __str__(self):
        return f"ID: {self.ProductId}, Модель: {self.Model}, Рік: {self.Year}, Ціна: {self.Price}, Колір: {self.Color}"


class Category:
    def __init__(self, CategoryId, CategoryName):
        self.CategoryId = CategoryId
        self.CategoryName = CategoryName

    def __str__(self):
        return f"{self.CategoryName}"


class Order:
    def __init__(self, OrderId, CreateDate, Total_price, Status, UserId, Addres):
        self.OrderId = OrderId
        self.CreateDate = CreateDate
        self.Total_price = Total_price
        self.Status = Status
        self.UserId = UserId
        self.Addres = Addres


class OrderDetails:
    def __init__(self, Id_details, OrderId, ProductId, Quantity, Price):
        self.Id_details = Id_details
        self.OrderId = OrderId
        self.ProductId = ProductId
        self.Quantity = Quantity
        self.Price = Price


users = [
    User(1, "Іван", "Іванов", "ivan@gmail.com", "123456789"),
    User(2, "Петро", "Петров", "petro@gmail.com", "987654321")
]

categories = [
    Category(1, "Смартфони"),
    Category(2, "Ноутбуки")
]

products = [
    Product(1, 1, "iPhone 12", 2020, 1000.00, "Чорний"),
    Product(2, 2, "MacBook Air", 2021, 1200.00, "Сріблястий"),
    Product(3, 1, "Samsung Galaxy S21", 2021, 900.00, "Білий"),
    Product(4, 2, "Dell XPS 13", 2021, 1100.00, "Чорний")
]

orders = []
order_details = []


def display_products():
    print("\nНаявні продукти в системі:")
    for product in products:
        print(product)


def add_product():
    model = input("Введіть модель продукту: ")
    year = int(input("Введіть рік випуску продукту: "))
    id = len(products) + 1
    price = float(input("Введіть ціну продукту: "))
    color = input("Введіть бажаний колір продукту: ")
    category_id = int(input("Введіть ID категорії: "))
    product = Product(id, category_id, model, year, price, color)
    products.append(product)
    print(f"Продукт {product} додано в систему.")


def add_order():
    order_id = len(orders) + 1
    createDate = input("Введіть дату створення(YYYY-MM-DD): ")
    total_price = float(input("Введіть загальну ціну замовлення: "))
    user_id = int(input("Введіть id користувача: "))
    addres = input("Введіть адресу доставки: ")
    order = Order(order_id, createDate, total_price, "New", user_id, addres)
    orders.append(order)

    while True:
        product_id = int(input("Введіть id продукту для оформлення замовлення(0 щоб завершити замовлення): "))
        if product_id == 0:
            break
        Id_details = len(order_details) + 1
        quantity = int(input("Введіть кількість продуктів для замовлення: "))
        price = float(input("Введіть ціну за одиницю: "))
        order_detail = OrderDetails(Id_details, order_id, product_id, quantity, price)
        order_details.append(order_detail)
    print(f"Замовлення {order_id} успішно виконано.")


def update_status():
    order_id = int(input("Введіть id замовлення для оновлення статусу: "))
    new_status = input("Введіть новий статус(New, Paid, Delivered): ")

    for order in orders:
        if order.OrderId == order_id:
            order.Status = new_status
            print(f"Статус замовлення {order_id} оновлено на {new_status}.")
            return
    print("Замовлення не знайдено.")


def print_products_by_category():
    category_id = int(input("Введіть id категорії: "))
    for product in products:
        if product.CategoryId == category_id:
            print(product)


def find_regular_customers():
    customer_purchases = {}
    for order in orders:
        user_id = order.UserId
        if user_id in customer_purchases:
            customer_purchases[user_id] += 1
        else:
            customer_purchases[user_id] = 1

    print("Клієнти, які найчастіше робили покупки:")
    for user_id, count in customer_purchases.items():
        if count >= 3:
            user = next((u for u in users if u.userId == user_id), None)
            if user:
                print(f"{user}: {count} покупок")


def find_non_paid_orders():
    print("Клієнти, які не оплатили замовлення:")
    for order in orders:
        if order.Status == "New":
            user = next((u for u in users if u.userId == order.UserId), None)
            if user:
                print(f"{user} має незавершене замовлення (ID: {order.OrderId})")


def find_high_value_customers():
    average_order_value = sum(order.Total_price for order in orders) / len(orders) if orders else 0
    print(f"Середня сума усіх замовлень: {average_order_value}")

    print("Клієнти, які зробили замовлення на суму більшу ніж середня:")
    for order in orders:
        if order.Total_price > average_order_value:
            user = next((u for u in users if u.userId == order.UserId), None)
            if user:
                print(f"{user} - Сума замовлення: {order.Total_price}")


def calculate_store_revenue():
    start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("Невірний формат дати.")
        return

    total_revenue = 0
    for order in orders:
        order_date = datetime.strptime(order.CreateDate, "%Y-%m-%d")
        if order_date >= start_date and order.Status == "Paid":
            total_revenue += order.Total_price

    print(f"Загальний дохід з {start_date.strftime('%Y-%m-%d')} по сьогоднішній день: {total_revenue}")


def find_best_selling_products():
    product_sales = {}

    for detail in order_details:
        if detail.ProductId in product_sales:
            product_sales[detail.ProductId] += detail.Quantity
        else:
            product_sales[detail.ProductId] = detail.Quantity

    sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Топ 5 продуктів, які найкраще продаються:")
    for product_id, quantity in sorted_sales:
        product = next((p for p in products if p.ProductId == product_id), None)
        if product:
            print(f"{product.Model} - продано {quantity} одиниць")


def find_weekday_with_most_sales():
    weekday_sales = [0] * 7  # Індекси 0-6 відповідають дням тижня (понеділок-неділя)

    for order in orders:
        order_date = datetime.strptime(order.CreateDate, "%Y-%m-%d")
        weekday_sales[order_date.weekday()] += 1

    max_sales_day = weekday_sales.index(max(weekday_sales))
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

    print(f"Найбільше покупок робиться в {days[max_sales_day]}")


def find_category_with_highest_avg_price():
    category_prices = {}
    category_counts = {}

    for product in products:
        if product.CategoryId in category_prices:
            category_prices[product.CategoryId] += product.Price
            category_counts[product.CategoryId] += 1
        else:
            category_prices[product.CategoryId] = product.Price
            category_counts[product.CategoryId] = 1

    avg_prices = {cat_id: category_prices[cat_id] / category_counts[cat_id] for cat_id in category_prices}
    highest_avg_price_category = max(avg_prices, key=avg_prices.get)

    category = next((c for c in categories if c.CategoryId == highest_avg_price_category), None)
    if category:
        print(
            f"Категорія з найбільшою середньою вартістю товару: {category.CategoryName} із середньою ціною {avg_prices[highest_avg_price_category]}")


def main_menu():
    display_products()

    while True:
        print("\n1. Додати продукт")
        print("2. Додати замовлення")
        print("3. Оновити статус замовлення")
        print("4. Показати продукти за категорією")
        print("5. Знайти постійних клієнтів")
        print("6. Знайти клієнтів з неоплаченими замовленнями")
        print("7. Знайти клієнтів з великими замовленнями")
        print("8. Підрахувати дохід магазину")
        print("9. Знайти найбільш продавані продукти")
        print("10. Знайти день з найбільшою кількістю продажів")
        print("11. Знайти категорію з найвищою середньою ціною продукту")
        print("12. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            add_order()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print_products_by_category()
        elif choice == "5":
            find_regular_customers()
        elif choice == "6":
            find_non_paid_orders()
        elif choice == "7":
            find_high_value_customers()
        elif choice == "8":
            calculate_store_revenue()
        elif choice == "9":
            find_best_selling_products()
        elif choice == "10":
            find_weekday_with_most_sales()
        elif choice == "11":
            find_category_with_highest_avg_price()
        elif choice == "12":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
