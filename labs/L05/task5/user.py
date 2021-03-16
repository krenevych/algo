"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
Реалізуйте для хеш-таблиці описаної ітеративний протокол для проходження усіх ключів хеш-таблиці.
"""

class HashTable:

    def __init__(self):
        """ Конструктор """
        pass

    def set(self, key: int, value: str) -> None:
        """ Встановлює значення value для ключа key.
        Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
        :param key: Ключ
        :param value: Значення
        """
        pass

    def get(self, key: int):
        """ За ключем key повертає значення зі структури.
        :param key: Ключ
        :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
        """
        return None


    def delete(self, key: int) -> None:
        """ Видаляє пару ключ-значення за заданим ключем.
        Якщо ключ у структурі відсутній - нічого не робить.
        :param key: Ключ
        """
        pass


    def __iter__(self):
        """ Створює ітератор для проходження хеш-таблиці
        :return: Новий ітератор
        """
        return Iterator()


class Iterator:
    """ Клас-ітератор для ітерування ключів хеш-таблиці HashTable """

    def __next__(self):
        raise StopIteration
