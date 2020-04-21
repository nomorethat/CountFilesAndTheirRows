import os

root_dir = '/home/administrator/PhpstormProjects/outlet-react/src'

total_count_rows = 0
total_count_files = 0
total_react_rows = 0
total_react_files = 0
total_less_rows = 0
total_less_files = 0


def get_file_contents(file_path):  # файлы в одной директории
    global total_count_rows
    global total_count_files
    global total_react_rows
    global total_react_files
    global total_less_rows
    global total_less_files
    print('Открываю ', file_path)
    file = open(file_path)
    print('Найдено строк: ', len(file.readlines()))
    file.seek(0)
    total_count_rows += len(file.readlines())
    file.seek(0)
    total_count_files += 1
    if file_path.endswith('.ts') or file_path.endswith('.tsx'):
        total_react_rows += len(file.readlines())
        file.seek(0)
        total_react_files += 1
    if file_path.endswith('.less'):
        total_less_rows += len(file.readlines())
        file.seek(0)
        total_less_files += 1
    print('Общее число строк: ', total_count_rows)
    file.close()


def recursive_dir_handler(path):
    print('\n\nЗахожу в', path, '\n')
    local_list_objects = os.listdir(path=path)
    print('Список объектов ', local_list_objects, '\n')
    for object in local_list_objects:
        if object == 'assets':
            continue
        object_path = path + '/' + object
        if os.path.isdir(object_path):
            recursive_dir_handler(object_path)
        if os.path.isfile(object_path):
            get_file_contents(object_path)


recursive_dir_handler(root_dir)
print('\nФайлы: количество', total_count_files, ',', 'строк', total_count_rows)
print('Файлы .ts/.tsx: количество', total_react_files, ',', 'строк', total_react_rows)
print('LESS-файлы: количество', total_less_files, ',', 'строк', total_less_rows)
