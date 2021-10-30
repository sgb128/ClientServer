"""Программа-клиент"""

import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, PORT
from lesson3.common.utils import rsvmsg, sndmsg


def create_presence(port, account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        PORT: port,
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def check_answer(answer):
    """
    Функция разбирает ответ сервера
    :param answer:
    :return:
    """
    if RESPONSE in answer:
        if answer[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {answer[ERROR]}'
    raise ValueError


def main():
    # Загружаем параметы коммандной строки
    try:
        s_address = sys.argv[2]
        s_port = int(sys.argv[1])
        if s_port < 1024 or s_port > 65535:
            raise ValueError
    except IndexError:
        s_address = DEFAULT_IP_ADDRESS
        s_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((s_address, s_port))
    message = create_presence(s_port)
    sndmsg(tcp, message)
    try:
        answer = check_answer(rsvmsg(tcp))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
