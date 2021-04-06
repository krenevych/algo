# -*- coding: utf-8 -*-

class HashTable:
    """Хеш-таблиця у якій колізії розв'язуються методом лінійного зондування."""

    TABLE_SIZE = 200000
    # TABLE_SIZE = 11

    def __init__(self):
        """ Конструктор - ініціалізує таблицю. """
        self.max_size = HashTable.TABLE_SIZE  # кількість слотів таблиці
        self.current_size = 0  # поточний розмір таблиці
        self.keys = [None] * self.max_size  # слоти таблиці, що містять ключі
        self.values = [None] * self.max_size  # дані пов'язані зі слотом

    def hash(self, key):
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа
        """
        N = 31  # Просте число, що не перевищує 255


        h = 0
        for i in range(len(key)):
            h = h * N + ord(key[i])
        return h % HashTable.TABLE_SIZE

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
            current = (current + 1) % HashTable.TABLE_SIZE

        # якщо ключ у таблиці не знайдений
        self.keys[current] = key  # додаємо ключ
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
            current = (current + 1) % HashTable.TABLE_SIZE

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

    def getList(self):
        return [key for key in self.keys if key != None]

    def __iter__(self):
        return Iterator(self.keys)


class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.currentIndex = 0

    def __next__(self):
        if self.currentIndex >= HashTable.TABLE_SIZE:
            raise StopIteration

        curr = self.collection[self.currentIndex]

        while curr is None:
            self.currentIndex += 1
            if self.currentIndex >= HashTable.TABLE_SIZE:
                raise StopIteration
            curr = self.collection[self.currentIndex]

        self.currentIndex += 1
        return curr


eng_lat = HashTable()

with open("input.txt") as f:
    for line in f:
        words = line.split()
        value = [word.strip(",") for word in words[2:]]
        eng_lat[words[0]] = value

# for key in eng_lat:
#     print(key)
#     print(eng_lat.get(key))

lat_eng = HashTable()
for key in eng_lat:
    val = eng_lat.get(key)
    for w in val:
        if w in lat_eng:
            lat_eng[w].append(key)
        else:
            lat_eng[w] = [key]


# for key in lat_eng:
#     print(key)
#     print(lat_eng.get(key))


lat = lat_eng.getList()
# print(lat)
lat.sort()

print(len(lat))
for word in lat:
    trans = lat_eng[word]
    trans.sort()
    print(word, end=" - ")
    print(*trans, sep=", ")


