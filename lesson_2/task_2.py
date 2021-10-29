"""
2. Задание на закрепление знаний по модулю json.
    Есть файл orders в формате JSON с информацией о заказах.
    Написать скрипт, автоматизирующий его заполнение данными.
    Для этого:
        a. Создать функцию write_order_to_json(), в которую передается 5 параметров:
                товар       (item)
                количество  (quantity)
                цена        (price)
                покупатель  (buyer)
                дата        (date)

            Функция должна предусматривать запись данных в виде словаря в файл orders.json.
            При записи данных указать величину отступа в 4 пробельных символа;
        b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого
            параметра.
"""

import json

OUT_FILE = 'orders.json'
JS_INDENT = 4


def write_order_to_json(item, quantity, price, buyer, date):
    current_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    # читаем данные из файла
    with open(OUT_FILE, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # записываем данные в orders.json
    with open(OUT_FILE, 'w', encoding='utf-8') as file:
        json_data['orders'].append(current_order)
        json.dump(json_data, file, indent=JS_INDENT, ensure_ascii=False)


# проверяю себя
write_order_to_json('ключ гаечный 32х36', '30', '300', 'ООО "Мосводоканал"', '27-08-2021')
write_order_to_json('ключ гаечный 27х30', '20', '350', 'ООО "Мосводоканал"', '27-08-2021')
write_order_to_json('ножницы гидравлические', '30', '300', 'ООО "Мосводоканал"', '27-08-2021')