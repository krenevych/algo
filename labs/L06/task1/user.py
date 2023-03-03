"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""


class HashTable:

    def __init__(self, size=1009):  # 1009 - розмір таблиці, просте число
        self.size = size
        self.keys = [None] * size
        self.vals = [None] * size
        self.valid = [False] * size  # маркери, що беруть участь в реалізації операції видалення елементів з таблиці

    def hash(self, key: int) -> int:
        return key % self.size

    def set(self, key: int, val: str):
        h = self.hash(key)
        while self.keys[h] is not None and self.valid[h]:

            if self.keys[h] == key:
                self.vals[h] = val
                self.valid[h] = True
                return

            h = (h + 1) % self.size

        self.keys[h] = key
        self.vals[h] = val
        self.valid[h] = True

    def get(self, key: int):
        h = self.hash(key)
        while self.keys[h] is not None:
            if self.keys[h] == key:
                return self.vals[h] if self.valid[h] else None
            h = (h + 1) % self.size

        return None

    def delete(self, key: int) -> None:
        h = self.hash(key)
        while self.keys[h] is not None:
            if self.keys[h] == key:
                self.valid[h] = False
                return
            h = (h + 1) % self.size

    def __str__(self):
        return str(self.keys)



d = HashTable(1)
def init():
    """ Викликається 1 раз на початку виконання програми. """
    global d
    d = HashTable(200_003)


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    d.set(key, value)


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    return d.get(key)


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    d.delete(key)


if __name__ == '__main__':
    table = HashTable(11)
    table.set(10, "10")
    table.set(11, "11")
    table.set(22, "22")
    table.set(33, "22")
    table.set(32, "32")
    table.set(33, "33")
    table.delete(22)
    val = table.get(22)
    val = table.get(33)
    # val = table.get(99)
    table.set(99, "99")


    pass
