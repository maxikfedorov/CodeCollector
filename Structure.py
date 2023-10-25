# Данный файл Structure (от слова структура) необходим для отрисовки дерева проекта
import os

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Создаем список исключений
exceptions = ["Structure.py", "node_modules", ".vscode", os.path.basename(__file__)]

# Функция для вывода содержимого директории
def print_directory_contents(path, prefix='', file=None):
    # Получаем список содержимого директории
    contents = os.listdir(path)
    # Разделяем содержимое на файлы и директории, исключая элементы из списка исключений
    files = [f for f in contents if os.path.isfile(os.path.join(path, f)) and f not in exceptions]
    dirs = [d for d in contents if os.path.isdir(os.path.join(path, d)) and d not in exceptions]

    # Выводим все файлы
    for i, file_name in enumerate(files):
        if i == len(files) - 1 and len(dirs) == 0:
            file.write(f"{prefix}└── {file_name}\n")
        else:
            file.write(f"{prefix}├── {file_name}\n")

    # Выводим все директории и рекурсивно вызываем функцию для их содержимого
    for i, dir_name in enumerate(dirs):
        if i == len(dirs) - 1:
            file.write(f"{prefix}└── {dir_name}\n")
            print_directory_contents(os.path.join(path, dir_name), prefix + " ", file)
        else:
            file.write(f"{prefix}├── {dir_name}\n")
            print_directory_contents(os.path.join(path, dir_name), prefix + "│ ", file)

# Получаем имя текущей директории
current_dir = os.path.basename(os.getcwd())

# Открываем файл для записи
with open(f"Код проекта {current_dir}.txt", "a", encoding="utf-8") as project_file:
    project_file.write("-" * 50 + "\n")
    # Вызываем функцию для вывода содержимого текущей директории
    print_directory_contents('.', file=project_file)
    project_file.write("-" * 50 + "\n")

print("Структура сформирована.")
