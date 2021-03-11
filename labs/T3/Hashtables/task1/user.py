"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""

class HashTable:

    TABLE_SIZE = 200000

    def __init__(self):
        """ Конструктор """
        pass

        self.max_size = HashTable.TABLE_SIZE  # кількість слотів таблиці
        self.current_size = 0  # поточний розмір таблиці
        self.keys = [None] * self.max_size  # слоти таблиці, що містять ключі
        self.values = [None] * self.max_size  # дані пов'язані зі слотом
        self.isValid = [False] * self.max_size  # дані пов'язані зі слотом


    def hash(self, key):
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа
        """
        return key % self.max_size

    def set(self, key: int, value: str) -> None:
        """ Встановлює значення value для ключа key.
        Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
        :param key: Ключ
        :param value: Значення
        """
        current = self.hash(key)  # Поточний слот таблиці
        while self.keys[current] != None:
            if self.keys[current] == key:
                self.values[current] = value
                self.isValid[current] = True
                return
            current = (current + 1) % HashTable.TABLE_SIZE

        # якщо ключ у таблиці не знайдений
        self.keys[current] = key  # додаємо ключ
        self.values[current] = value  # додаємо значення
        self.isValid[current] = True
        self.current_size += 1

    def get(self, key: int):
        """ За ключем key повертає значення зі структури.
        :param key: Ключ
        :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
        """
        current = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                return self.values[current] if self.isValid[current] else None
            current = (current + 1) % HashTable.TABLE_SIZE

        # якщо ключ у таблиці не знайдений
        return None


    def delete(self, key: int) -> None:
        """ Видаляє пару ключ-значення за заданим ключем.
        Якщо ключ у структурі відсутній - нічого не робить.
        :param key: Ключ
        """
        current = self.hash(key)  # Поточний слот таблиці
        while self.keys[current] != None:
            if self.keys[current] == key:
                self.isValid[current] = False
                return
            current = (current + 1) % HashTable.TABLE_SIZE


    def __iter__(self):
        """ Створює ітератор для проходження хеш-таблиці

        :return: Новий ітератор
        """
        return Iterator(self)


class Iterator:
    def __init__(self, collection):
        self.collection = collection.keys
        self.valid = collection.isValid
        self.currentIndex = 0

    def __next__(self):
        if self.currentIndex >= HashTable.TABLE_SIZE:
            raise StopIteration

        while self.collection[self.currentIndex] is None or not self.valid[self.currentIndex]:
            self.currentIndex += 1
            if self.currentIndex >= HashTable.TABLE_SIZE:
                raise StopIteration


        curr = self.collection[self.currentIndex]
        self.currentIndex += 1
        return curr

if __name__ == "__main__":
    table = HashTable()
    table.set(1354, "23")
    table.set(1214, "23")
    table.set(1674, "23")
    table.set(124, "23")
    table.set(146, "23")
    table.set(114, "23")

    for i in table:
        print(i)


