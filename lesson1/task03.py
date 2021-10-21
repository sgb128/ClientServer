"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

str_words = ('attribute', 'класс', 'функция', 'type')
for w in str_words:
    if w.isascii():
        print(w.encode('utf-8'))
    else:
        print(f'{str_words} - невозможно записать в байтовом типе')