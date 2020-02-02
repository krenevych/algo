#Лічилка з використанням деку
from source.T5_LinearStructure.P2_Queue.examples.counter_game import Player
from source.T5_LinearStructure.P2_Queue.L4_Deque import Deque


def count_counter():
    """ Функція розв'язує задачу "лічилка" """
    d = Deque()                                 # створити дек d
    n = int(input('Кількість гравців: '))
    m = int(input('Кількість слів: '))

    for i in range(n):
        pl = Player(i+1)                     # створити гравця з номером на 1 більше i
        d.append(pl)                         # додати гравця у кінець деку

    print('\nПослідовність номерів, що вибувають')
    while not d.empty():
        for i in range(m-1):                 # m-1 раз перекласти гравця з початку до кінця деку
            d.append(d.popleft())
        pl = d.popleft()                     # узяти m-го гравця з початку деку
        print(pl)                            # та показати його номер


count_counter()
