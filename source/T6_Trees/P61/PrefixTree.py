class PrefixTree:
    """ Клас префіксне дерево."""

    def __init__(self):
        """ Конструктор.
        Ініціалізує корінь дерева """
        self.mKey = ""       # Ключ вершини дерева
        self.mData = None    # Навантаження вершини
        self.mChildren = {}  # Словник дітей дерева, місить пари {ребро: піддерево}

    def add_key(self, key, data):
        """ Додавання даних у дерево за ключем
        :param key: Ключ
        :param data: Дані
        :return: None
        """
        self.__add_key(key, data, "")

    def __add_key(self, key, data, prefix):
        """ Допоміжний рекурсивний метод додавання даних у дерево за ключем

        Реалізується за допомогою пошуку в глибину
        :param key: Ключ
        :param data: Дані
        :param prefix: Поточний префікс ключа
        :return: None
        """

        self.mKey = prefix     # Переданий префікс - ключ вершини

        if key == "":          # Якщо досягнуто листка
            self.mData = data  # Встановлюємо навантаження на вершину
            return

        head = key[0]                    # Визначаємо ребро
        if head not in self.mChildren:   # Якщо ребро відсутнє для поточної вершини
            self.mChildren[head] = PrefixTree()  # додаємо його

        sub_tree = self.mChildren[head]  # Беремо піддерево за ребром

        tail = key[1:]               # Фрагмент ключа без першого симола (ребра)
        next_prefix = prefix + head  # Визначаємо наступний префікс ключа
        sub_tree.__add_key(tail, data, next_prefix)  # Заглиблюємося далі

    def find(self, key):
        """ Рекурсивний метод пошуку у дереві заданого ключа

        Реалізується за допомогою пошуку в глибину
        :param key: Ключ
        :return: Дані, що містяться у дереві за ключем або None, якщо дані відсутні у дереві
        """

        if key == "":          # Досягнуто листка
            return self.mData  # Повертаємо навантаження вершини

        head = key[0]
        if head not in self.mChildren:   # Якщо ребро відсутнє для поточної вершини
            return None                  # Повертаємо None - дерево не містить ключа

        sub_tree = self.mChildren[head]  # Беремо піддерево за ребром
        tail = key[1:]              # Фрагмент ключа без першого симола (ребра)
        return sub_tree.find(tail)  # Заглиблюємося далі


