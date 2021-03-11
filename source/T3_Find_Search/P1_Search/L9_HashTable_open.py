class HashTable:
    """Хеш-таблиця у якій колізії розв'язуються методом лінійного зондування."""

    def __init__(self):
        """ Конструктор - ініціалізує таблицю. """
        self.max_size = 11                    # кількість слотів таблиці
        self.current_size = 0                 # поточний розмір таблиці
        self.keys = [None] * self.max_size    # слоти таблиці, що містять ключі
        self.values = [None] * self.max_size  # дані пов'язані зі слотом

    def hash(self, key):
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа
        """
        return key % self.max_size

    def put(self, key, value):
        """ Додає пару (ключ, значення) до таблиці

        :param key: ключ
        :param value: значення
        :return: None
        """
        current = self.hash(key)  # Поточний слот таблиці
        while self.keys[current] != None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current = (current + 1) % self.max_size

        # якщо ключ у таблиці не знайдений
        self.keys[current] = key      # додаємо ключ
        self.values[current] = value  # додаємо значення
        self.current_size += 1

    def get(self, key):
        """ Повертає значення за ключем

        :param key: ключ
        :return: значення
        """
        current = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                return self.values[current]
            current = (current + 1) % self.max_size

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

    def __len__(self):
        """ Перевантаження вбудованого метода len()

        :return: Кількість елементів у таблиці.
        """

        return self.current_size

    def __contains__(self, key):
        """ Перевантаження оператора in

        :param key: ключ
        :return: True, якщо ключ міситься у таблиці.
        """
        return not (self[key] is None)

    def __str__(self):
        """ Перевантаження вбудованого методу str()

        :return: Зображення таблиці у рядковому вигляді
        """
        return str(self.keys) + '\n' + str(self.values) + '\n'


M = HashTable()  # Створюємо таблицю
M.put(55, "zz")   # додаємо пару (56, "zz")
M.put(66, "AA")   # додаємо пару (66, "AA")
M.put(66, "66")   # змінюємо значення за ключем 66
M.put(77, "77")   # додаємо пару (77, "77")

M[56] = "RR"      # M.put(56, "RR")
M[55] = "55"      # M.put(55, "55")

print(M[56])      # print(M.get(56))
print(len(M))
print(62 in M)
print(66 in M)

