"""
3. Задание на закрепление знаний по модулю yaml.
    Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
        a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
            второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число
            с юникод-символом, отсутствующим в кодировке ASCII (например, €);
        b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
            При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
            возможность работы с юникодом: allow_unicode = True;
        c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

from pprint import pprint

import yaml

OUT_FILE = 'file.yaml'

FIRST_ELEM = ['hund', 'fahrradfahrer', 'kanninchen', 'spielzeug', 'getrank', 'schule']
SECOND_ELEM = 5
THIRD_ELEM = {'hund':          '1 собака',
              'fahrradfahrer': '2 велосипедист',
              'kanninchen':    '3 кролик',
              'spielzeug':     '4 игрушка',
              'getrank':       '5 напиток',
              'schule':        '6 школа'}

DATA_YAML = {'woerder': FIRST_ELEM, 'zahl': SECOND_ELEM, 'uebersetzung': THIRD_ELEM}


def is_confirm(data_1, data_2):
    return data_1 == data_2


def wr2_yaml(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


def rd_frm_yaml(file_name):
    with open(file_name, encoding='utf-8') as file:
        content = yaml.load(file, Loader=yaml.FullLoader)
        return content


wr2_yaml(OUT_FILE, DATA_YAML)
file_data = rd_frm_yaml(OUT_FILE)

pprint(file_data)

print('====Сравнение исходных данных с результатом=======')
if is_confirm(DATA_YAML, file_data):
    print('Данные совпадают!')
else:
    print('Данные не совпадают!')
