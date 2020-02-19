
class Node:
    """ Допоміжний клас вузол таблиці """

    def __init__(self, key: int, value):
        self.key = key      # ключ
        self.value = value  # значення
        self.next = None    # посилання на наступний вузол з таким же хеш-значенням
        self.valid = True   # чи чинний вузол (для операції видалення)


class HashTable:
    """Хеш-таблиця у якій колізії розв'язуються методом лінійного зондування."""

    MAX_SIZE = 11                    # кількість слотів таблиці

    def __init__(self):
        """ Конструктор - ініціалізує таблицю. """
        self.slots = [None] * HashTable.MAX_SIZE  # слоти таблиці, що мітять ланцюжки вузлів з однаковими хешами

    @staticmethod
    def hash(key: int) -> int:
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа
        """
        return key % HashTable.MAX_SIZE

    def put(self, key, value):
        """ Додає пару (ключ, значення) до таблиці

        :param key: ключ
        :param value: значення
        :return: None
        """
        hash_key: int = HashTable.hash(key)  # хеш ключа
        slot: Node = self.slots[hash_key]    # поточний слот таблиці
        while slot != None:
            if slot.key == key:
                slot.value = value
                slot.valid = True
                return

            slot = slot.next

        # якщо ключ у таблиці не знайдений, додаємо новий вузол
        # з ключем та значенням у початок ланцюжка
        slot = Node(key, value)
        slot.next = self.slots[hash_key]
        self.slots[hash_key] = slot

    def get(self, key):
        """ Повертає значення за ключем

        :param key: ключ
        :return: значення
        """
        hhh = HashTable.hash(key)  # Поточний слот таблиці
        slot = self.slots[hhh]
        while slot != None:
            if slot.key == key:
                return slot.value
            slot = slot.next

        # якщо ключ у таблиці не знайдений
        return None

    def __setitem__(self, key, value):
        """ Перевантаження оператора [ ] для запису

        :param key: ключ
        :param value: нове значення
        """
        self.put(key, value)

    def __getitem__(self, key):
        """ Перевантаження оператора [ ] для читання

        :param key: ключ
        :return: значення, що відповідає ключу key
        """
        return self.get(key)

    def __contains__(self, key):
        """ Перевантаження оператора in

        :param key: ключ
        :return: True, якщо ключ міситься у таблиці.
        """
        return not (self[key] is None)


M = HashTable()  # Створюємо таблицю
M.put(55, "zz")   # додаємо пару (56, "zz")
M.put(66, "AA")   # додаємо пару (66, "AA")
M.put(66, "66")   # змінюємо значення за ключем 66
M.put(77, "77")   # додаємо пару (77, "77")
M.put(88, "88")   # додаємо пару (77, "77")
M.put(99, "99")   # додаємо пару (77, "77")
M.put(98, "98")   # додаємо пару (77, "77")

M[56] = "RR"      # M.put(56, "RR")
M[55] = "55"      # M.put(55, "55")

print(M[56])      # print(M.get(56))
print(M[66])
print(M[77])
print(M[88])
print(M[99])
print(M[98])
print(M[100])
