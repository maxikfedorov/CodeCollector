#Данный файл CodeDet (от слова детерменирование) необходим для реструктуризации созданных txt файлов
# с помощью CodeSum обратно в полноценный проект

import os
import re

# Название файла с информацией о проекте
project_info_file = [f for f in os.listdir('.') if f.startswith('Код проекта')][0]

# Открываем файл с информацией о проекте
with open(project_info_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()


# Извлекаем имя проекта из названия файла
project_name = re.search(r'^Код проекта (.+)\.txt$', project_info_file).group(1)


# Создаем папку с названием проекта
os.makedirs(project_name, exist_ok=True)

# Ищем строки с названиями файлов и их содержимым
file_regex = r'^\.\\(.+)\n-{50}\n([\s\S]+?)(?=\n-{50}|\Z)'
file_matches = re.findall(file_regex, ''.join(lines), re.MULTILINE)

# Создаем файлы и записываем в них содержимое
for file_match in file_matches:
    file_path = os.path.join(project_name, file_match[0])
    file_content = file_match[1].strip()
    # Если в пути файла есть папки, то создаем их
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Записываем содержимое в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)

# Ищем строки с прочими файлами
other_files_regex = r'^\.\\(.+)$'
other_files_matches = re.findall(other_files_regex, ''.join(lines), re.MULTILINE)

# Создаем прочие файлы
for other_file_match in other_files_matches:
    other_file_path = os.path.join(project_name, other_file_match)
    # Если в пути файла есть папки, то создаем их
    os.makedirs(os.path.dirname(other_file_path), exist_ok=True)
    # Создаем пустой файл
    open(other_file_path, 'a', encoding='utf-8').close()
