"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:

    a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
    данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
        «Изготовитель системы»,
        «Название ОС»,
        «Код продукта»,
        «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
        os_prod_list,
        os_name_list,
        os_code_list,
        os_type_list.
    В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
    названия столбцов отчета в виде списка:
        «Изготовитель системы»,
        «Название ОС»,
        «Код продукта»,
        «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

    b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
    в соответствующий CSV-файл;

    c. Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re

from chardet.universaldetector import UniversalDetector

FILE_TO_SAVE = 'main_data.csv'
FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
main_data = [[]]
main_data[0] = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []


def find_encoding(file: str):
    DETECTOR = UniversalDetector()
    with open(file, 'rb') as fs:
        for i in fs:
            DETECTOR.feed(i)
            if DETECTOR.done:
                break
        DETECTOR.close()
        return DETECTOR.result['encoding']


def find_info(file: str, param_name, lst: list):
    with open(file, encoding=find_encoding(file)) as fs:
        while True:
            f_str = fs.readline()
            if not f_str:
                fs.close()
                break
            if re.match(param_name, f_str):
                lst.append(re.sub(r'(' + param_name + ':\s+)|(\n)', '', f_str))


def get_data():
    for fnum, file in enumerate(FILES, 1):
        main_data.append([])
        for search_data in main_data[0]:
            find_info(file, search_data, main_data[fnum])


def write_to_csv(f_link):
    get_data()
    with open(f_link, 'w', encoding='utf-8') as file:
        f_writer = csv.writer(file)
        f_writer.writerows(main_data)


write_to_csv(FILE_TO_SAVE)

# проверяю себя. Вывожу массив данных:
print('=====================массив данных=====================')
for data in main_data:
    print(data)
print('=======================================================\n\n')

print('====================вывод данных из файла==============')
with open(FILE_TO_SAVE, encoding='utf-8') as f_n:
    F_N_READER = csv.reader(f_n)
    F_N_HEADERS = next(F_N_READER)
    print('Headers: ', F_N_HEADERS)
    for row in F_N_READER:
        print(row)

# Не могу понять почему так? Много времени потратил и так и не смог разобраться откуда берутся пустые строки в файле csv
