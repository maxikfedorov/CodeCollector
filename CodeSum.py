#Данный файл CodeSum (от слова суммирование) необходим для сбора кода

import os
from datetime import datetime

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Получаем имя текущей директории
current_dir = os.path.basename(os.getcwd())

# Получаем имя файла скрипта
script_name = os.path.basename(__file__)

# Создаем словарь с названиями месяцев на русском языке
months = {1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня", 7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"}

# Создаем новый файл для записи кода проекта
with open(f"Код проекта {current_dir}.txt", "w", encoding="utf-8") as project_file:
    # Записываем дату сборки в начало файла
    now = datetime.now()
    month_name = months[now.month]
    project_file.write(f"Файл проекта {current_dir}, в котором собран весь код данного приложения\n")
    project_file.write(f"Дата сборки - {now.day} {month_name} {now.strftime('%H:%M')}\n\n")

    # Список расширений файлов, которые нужно найти
    extensions = [".html", ".css", ".php", ".js", ".jsx", 
                  ".yml", ".yaml", "Dockerfile", 
                  ".sql", ".java", ".py", ".cpp", ".h", 
                  ".json", ".xml"]

    # Список исключений
    exceptions = ["Structure.py", "node_modules", ".vscode", "package-lock.json",
                  script_name]

    # Список файлов, которые не входят в список необходимых расширений
    other_files = []

    # Переменная для подсчета количества строк в проекте
    lines_count = 0

    # Итерируемся по всем файлам в текущей директории и ее поддиректориях
    for root, dirs, files in os.walk("."):
        if any(exception in root for exception in exceptions):
            continue

        # Итерируемся по всем файлам в текущей директории и ее поддиректориях
        for filename in files:
            # Проверяем, что имя файла не начинается с "Код проекта" и не входит в список исключений
            if not filename.startswith("Код проекта") and filename not in exceptions:
                # Проверяем, что файл имеет нужное расширение
                if any(filename.endswith(ext) for ext in extensions):
                    # Определяем путь к файлу
                    file_path = os.path.join(root, filename)

                    # Открываем файл и записываем его содержимое в текстовый файл
                    with open(file_path, "r", encoding="utf-8") as file:
                        project_file.write(f"\n{file_path}\n")
                        project_file.write("-" * 50 + "\n")
                        file_lines = file.readlines()
                        lines_count += len(file_lines)
                        project_file.write("".join(file_lines))
                        project_file.write("\n" + "-" * 50 + "\n")
                else:
                    # Если файл не имеет нужного расширения, добавляем его в список other_files
                    file_path = os.path.join(root, filename)
                    other_files.append(file_path)

    # Записываем файлы, которые не входят в список необходимых расширений, в текстовый файл в конце
    if other_files:
        project_file.write("\n\nПрочие файлы:\n" + "-" * 50 + "\n")
        for file_path in other_files:
            # Проверяем, что имя файла не начинается с "Код проекта" и не входит в список исключений
            if not os.path.basename(file_path).startswith("Код проекта") and os.path.basename(file_path) not in exceptions:
                project_file.write(f"\n{file_path}\n")
                project_file.write("\n" + "-" * 50 + "\n")

    # Записываем количество строк в конец файла
    project_file.write(f"\n\nКоличество строк в проекте: {lines_count}\n\n\n")
    project_file.write(f"Дерево проекта {current_dir}:\n")

os.system("python Structure.py")

# Выводим сообщение об успешном выполнении скрипта
print("Документ успешно составлен.")