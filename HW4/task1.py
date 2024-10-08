import sys
import os

def main(dir_path, dir_diff_path):
    if not os.path.exists(dir_path):
        print(f"Каталог {dir_path} не існує.")
        return

    if not os.path.exists(dir_diff_path):
        print(f"Каталог {dir_diff_path} не існує.")
        return

    dir_files = os.listdir(dir_path)
    dir_diff_files = os.listdir(dir_diff_path)

    for file_name in dir_files:
        file_path = os.path.join(dir_path, file_name)
        file_diff_path = os.path.join(dir_diff_path, file_name)

        if os.path.isfile(file_path):
            if file_name in dir_diff_files:
                if os.path.getmtime(file_path) > os.path.getmtime(file_diff_path):
                    print(f"Файл {file_name} новіший, залишаємо його.")
                else:
                    print(f"Файл {file_name} старіший, видаляємо його з {dir_path}.")
                    os.remove(file_path)
            else:
                print(f"Файл {file_name} не існує в DIR_DIFF, залишаємо його.")

if __name__ == "__main__":
    # Аргументи командного рядка: dir_path та dir_diff_path
    if len(sys.argv) < 3:
        print("Вкажіть шляхи до каталогів DIR та DIR_DIFF")
    else:
        dir_path = sys.argv[1]
        dir_diff_path = sys.argv[2]
        main(dir_path, dir_diff_path)
