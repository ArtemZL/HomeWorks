def type_check(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, (name, expected_type) in enumerate(annotations.items()):
            if name == 'return':
                continue
            if name in kwargs:
                value = kwargs[name]
            elif i < len(args):
                value = args[i]
            else:
                continue
            if not isinstance(value, expected_type):
                raise TypeError(f"Аргумент '{name}' повинен бути типу {expected_type}, але отримано {type(value)}")
        return func(*args, **kwargs)
    return wrapper

def inject(**injections):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name, cls in injections.items():
                if name not in kwargs:
                    kwargs[name] = cls()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def trace_recursion(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.total_calls = max(wrapper.total_calls, wrapper.call_count)

        result = func(*args, **kwargs)
        wrapper.call_count -= 1
        if wrapper.call_count == 0:
            print(f"Загальна кількість рекурсивних викликів: {wrapper.total_calls}")

        return result
    wrapper.call_count = 0
    wrapper.total_calls = 0
    return wrapper

def rate_limiter(max_calls, time_window):
    import time
    call_times = []
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            call_times[:] = [t for t in call_times if t > current_time - time_window]
            if len(call_times) >= max_calls:
                raise Exception("Ліміт викликів перевищено")
            call_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@type_check
def concatenate(a: str, b: str) -> str:
    return a + b

class DatabaseService:
    def fetch_data(self):
        return "Data from database"

@inject(service=DatabaseService)
def get_data(service):
    print("Injected service:", service.fetch_data())  # Викликаємо метод для прикладу

@trace_recursion
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

@rate_limiter(max_calls=5, time_window=60)
def api_call():
    print("API called")


@benchmark
def slow_function():
    import time
    time.sleep(2)
    print("Функція завершила роботу")


def main():
    tasks = {
        1: ("type_check", lambda: print("Результат:", concatenate("hello", " world"))),
        2: ("inject", get_data),
        3: ("trace_recursion", lambda: print("Результат факторіала:", factorial(5))),
        4: ("rate_limiter", api_call),
        5: ("benchmark", slow_function)
    }

    while True:
        print("\nВиберіть завдання:")
        for key, (name, _) in tasks.items():
            print(f"{key}. Виконати {name}")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "0":
            print("Вихід з програми.")
            break

        if choice.isdigit() and int(choice) in tasks:
            print(f"Виконую {tasks[int(choice)][0]}:")
            tasks[int(choice)][1]()
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

