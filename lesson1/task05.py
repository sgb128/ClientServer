"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet

ARGS_YA = ['ping', 'yandex.ru']
ARGS_YT = ['ping', 'youtube.com']

YA_PING = subprocess.Popen(ARGS_YA, stdout=subprocess.PIPE)
YT_PING = subprocess.Popen(ARGS_YT, stdout=subprocess.PIPE)

print('utf-8')

for line in YA_PING.stdout:
    line_info = chardet.detect(line)
    line = line.decode(line_info['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

print('windows-1251')

for line in YT_PING.stdout:
    line_info = chardet.detect(line)
    line = line.decode(line_info['encoding']).encode('cp1251')
    print(line.decode('cp1251'))
