"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з розв’язанням колізій методом ланцюжків.
"""

TABLE_SIZE = 500_003
# TABLE_SIZE = 11

slots = [None]


##############
class Node:  # службовий клас - вузол хеш-таблиці,
    # що містить ключ значення та посилання на наступний
    # елемент у ланцюжку елементів таблиці з однаковими ключами
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.valid = True

    def __str__(self) -> str:
        return f"Node({self.key}, {self.val})"


####################

def hash(key: int) -> int:  # Хеш-функція
    return key % TABLE_SIZE


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None] * TABLE_SIZE


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """

    found_slot = _get(key)
    if found_slot is not None:
        found_slot.val = value
        found_slot.valid = True
        return

    h = hash(key)
    new = Node(key, value)
    new.next = slots[h]
    slots[h] = new


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None,
             якщо ключ відсутній у структурі.
    """
    slot = _get(key)
    if slot is not None and slot.valid:
        return slot.val

    return None


def _get(key: int):
    """
    Допоміжний метод пошуку вузла у таблиці,
    що відповідає заданому ключу key
    """
    h = hash(key)
    slot: Node = slots[h]
    while slot is not None:
        if slot.key == key:
            return slot
        slot = slot.next

    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    found_slot = _get(key)
    if found_slot is not None:
        found_slot.valid = False


if __name__ == '__main__':
    init()
    set(14, "14")
    set(3, "3")
    set(25, "25")

    delete(3)
    print(get(3))

    set(3, "333")
    print(get(3))
    delete(3)
    print(get(3))
