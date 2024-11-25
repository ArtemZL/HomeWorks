import pandas as pd
import matplotlib.pyplot as plt

class Component:
    def __init__(self, id, name, material, price):
        self.id = id
        self.name = name
        self.material = material
        self.price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID компонента має бути додатним цілим числом")
        self._id = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Ціна компонента має бути додатним числом")
        self._price = value


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID категорії має бути додатним цілим числом")
        self._id = value


class Order:
    def __init__(self, order_id, component_id, category_id, product_name):
        self.order_id = order_id
        self.component_id = component_id
        self.category_id = category_id
        self.product_name = product_name

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID замовлення має бути додатним цілим числом")
        self._order_id = value


class AssemblyOperation:
    def __init__(self, order_id, component_id, date, status):
        self.order_id = order_id
        self.component_id = component_id
        self.date = date
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ['done', 'processing']:
            raise ValueError("Статус має бути 'done' або 'processing'")
        self._status = value

def load_csv():
    components_df = pd.read_csv('components.csv')
    categories_df = pd.read_csv('furnitureСategory.csv')
    orders_df = pd.read_csv('funitureOrder.csv')
    operations_df = pd.read_csv('assemblyOperations.csv')
    components = [Component(row['id'], row['name'], row['material'], row['price']) for _, row in components_df.iterrows()]
    categories = [Category(row['id'], row['name']) for _, row in categories_df.iterrows()]
    orders = [Order(row['order_id'], None, row['category_id'], row['product_name']) for _, row in orders_df.iterrows()]
    operations = [AssemblyOperation(row['order_id'], row['component_id'], row['date'], row['status']) for _, row in operations_df.iterrows()]
    return components_df, categories_df, orders_df, operations_df

def task1(operations, components):
    used_components = operations[operations['status'] == 'done'].groupby('component_id').size()
    used_components = used_components.reset_index(name='count')
    used_components = used_components.merge(components, left_on='component_id', right_on='id')
    used_components['total_cost'] = used_components['count'] * used_components['price']
    print(used_components)
    bar_labels = ['green', 'yellow']
    plt.bar(used_components['name'], used_components['total_cost'], label=used_components['component_id'],
            color=bar_labels)
    plt.title('Діаграма компонентів відносно ціни')
    plt.ylabel('Сумарна вартість')
    plt.xlabel('Компонент')
    plt.show()

def task2(operations, components):
    operations = operations[operations['status'] == 'done']
    operations = operations.merge(components, left_on='component_id', right_on='id')
    operations['date'] = pd.to_datetime(operations['date'])
    start_date = input("Введіть початкову дату(YYYY-MM-DD): ")
    end_date = input("Введіть кінцеву дату(YYYY-MM-DD): ")
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    operations = operations[operations['date'].between(start_date, end_date)]
    grouped = operations.groupby(operations['date'].dt.date)['price'].sum()
    print(f"Сумарна вартість компонентів за період з {start_date.date()} по {end_date.date()}")
    print(grouped)
    grouped.plot(kind='line', marker='o', title='Сумарна вартість компонентів за датами')
    plt.xlabel('Дата')
    plt.ylabel('Сумарна вартість')
    plt.grid()
    plt.show()

def task3(operations, components):
    used_component_ids = operations['component_id'].unique()
    unused_components = components[~components['id'].isin(used_component_ids)]
    print("Компоненти, які не були встановлені:")
    print(unused_components)
    return unused_components

def task4(operations):
    grouped = operations.groupby('status').size()
    ready_orders = grouped.get('done', 0)
    not_ready_orders = grouped.get('processing', 0)
    print(f"Готові замовлення: {ready_orders}")
    print(f"Неготові замовлення: {not_ready_orders}")
    bar_labels = ['Готові', 'Неготові']
    bar_values = [ready_orders, not_ready_orders]
    plt.bar(bar_labels, bar_values, color=['green', 'yellow'])
    plt.title("Загальна кількість готових і неготових замовлень")
    plt.xlabel("Стан замовлень")
    plt.ylabel("Загальна кількість")
    plt.show()
    return ready_orders, not_ready_orders

def task5(operations, components):
    ready_orders = operations[operations['status'] == 'done']
    ready_orders = ready_orders.merge(components, left_on='component_id', right_on='id', how='left')
    ready_orders['total_cost'] = ready_orders['price']
    ready_orders = ready_orders.sort_values(by=['total_cost'], ascending=False)
    print("Готові замовлення з вартістю:")
    print(ready_orders[['order_id', 'component_id', 'name', 'total_cost']])
    return ready_orders

def task6(ready_orders):
    top_5_orders = ready_orders.nlargest(5, 'total_cost')
    plt.bar(top_5_orders['id'], top_5_orders['total_cost'], color='orange')
    plt.xlabel('ID Замовлення')
    plt.ylabel('Загальна вартість')
    plt.title('ТОП-5 готових замовлень за вартістю')
    plt.show()

def task7(data):
    data.to_csv('exported_data.csv', index=False)
    data.to_excel('exported_data.xlsx', index=False)
    print("Дані експортовано у файли: exported_data.csv та exported_data.xlsx")

def menu():
    components, categories, orders, operations = load_csv()
    while True:
        print("\nМеню:")
        print("1. Підрахунок кількості використаних компонентів (таблиця)")
        print("2. Сумарна вартість компонентів за період")
        print("3. Список невикористаних компонентів")
        print("4. Готові та неготові замовлення")
        print("5. Таблиця вартості готових замовлень")
        print("6. ТОП-5 замовлень за вартістю (діаграма)")
        print("7. Експорт даних у CSV та Excel")
        print("0. Вихід")
        choice = input("Виберіть пункт меню: ")

        if choice == '1':
            task1(operations, components)
        elif choice == '2':
            task2(operations, components)
        elif choice == '3':
            task3(operations, components)
        elif choice == '4':
            task4(operations)
        elif choice == '5':
            task5(operations, components)
        elif choice == '6':
            ready_orders = task5(operations, components)
            task6(ready_orders)
        elif choice == '7':
            data = task5(operations, components)
            task7(data)
        elif choice == '0':
            print("Роботу завершено!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
menu()
