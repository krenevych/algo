class HashTable:
    """Хеш-таблиця у якій колізії розв'язуються методом лінійного зондування."""

    def __init__(self):
        """ Конструктор - ініціалізує таблицю. """
        self.size = 11         # кількість слотів таблиці
        self.current_size = 0  # поточний розмір таблиці
        self.slots = [None] * self.size  # список слотів
        self.data = [None] * self.size   # дані пов'язані з слотом

    def hash(self, key):
        """ Повертає хеш для ключа

        :param key: ключ
        :return: хеш ключа
        """
        return key % self.size

    def rehash(self, prevhash):
        """ Функція повторного хешування, використовується
        у методі лінійного зондування для розв'язання колізій

        :param prevhash: попередній хеш
        :return: новий хеш
        """
        return (prevhash + 1) % self.size

    def put(self, key, value):
        """ Додає пару (ключ, значення) до таблиці

        :param key: ключ
        :param value: значення
        :return: None
        """
        if self.current_size == self.size:
            raise IndexError
        hash = self.hash(key)         # обчислення хешу ключа
        if self.slots[hash] is None:  # якщо відповідний слот вільний
            self.slots[hash] = key    # додаємо ключ
            self.data[hash] = value   # додаємо значення
            self.current_size += 1    # збільшуємо на 1 кількість елементів
        elif self.slots[hash] == key: # слот зайнятий елеметом з ключем key
            self.data[hash] = value   # змінюємо значення, що відповідає ключу
        else:
            # пошук вільного слота у таблиці або слота, що відповідає ключу
            next = self.rehash(hash)
            while self.slots[next] is not None and self.slots[next] != key:
                next = self.rehash(next)

            if self.slots[next] is None: # Знайдено вільний слот
                self.slots[next] = key   # додаємо ключ
                self.data[next] = value  # додаємо значення
                self.current_size += 1   # збільшуємо на 1 кількість елементів
            else:                        # Знайдено слот, з ключем key
                self.data[next] = value  # змінюємо значення, що відповідає ключу

    def get(self, key):
        """ Повертає значення за ключем

        :param key: ключ
        :return: значення
        """
        hash = self.hash(key)          # обчислення хешу ключа
        if self.slots[hash] is None:   # якщо відповідний слот вільний
            return None                # таблиця не містить ключа
        elif self.slots[hash] == key:  # слот зайнятий елеметом з ключем key
            return self.data[hash]     # повертаємо значення
        else:
            # Пошук слота з ключем key
            next = self.rehash(hash)
            while self.slots[next] is not None and self.slots[next] != key and next != hash:
                next = self.rehash(next)

            # Якщо знайдений слот вільний або пройшли таблицю по колу до вихідного слота
            if self.slots[next] is None or next == hash:
                return None      # таблиця не містить ключа

            elif self.slots[next] == key:  # знайдений слот зайнятий елеметом key
                return self.data[next]     # повертаємо значення

    def __setitem__(self, key, value):
        """ Перевизначення оператора [ ] для запису

        :param key: ключ
        :param value: нове значення
        """
        self.put(key, value)

    def __getitem__(self, key):
        """ Перевизначення оператора [ ] для читання

        :param key: ключ
        :return: значення, що відповідає ключу key
        """
        return self.get(key)

    def __len__(self):
        """ Перевизначення вбудованого метода len()

        :return: Кількість елементів у таблиці.
        """

        return self.current_size

    def __contains__(self, key):
        """ Перевизначення оператора in

        :param key: ключ
        :return: True, якщо ключ міситься у таблиці.
        """
        return not (self[key] is None)

    def __str__(self):
        """ Перевизначення вбудованого методу str()

        :return: Зображення таблиці у рядковому вигляді
        """
        return str(self.slots) + '\n' + str(self.data) + '\n'


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

