#Лічилка з використанням черги

from source.T5_LinearStructure.P42_Queue.Queue import *

class Player:
    """ Реалізує клас Гравець
    n - номер гравця
    """
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

def count_counter():
    """ Функція розв'язує задачу "лічилка" """
    q = Queue()                                 #створити чергу q
    n = int(input('Кількість гравців: '))
    m = int(input('Кількість слів: '))

    for i in range(n):
        pl = Player(i+1)                        #створити гравця з номером на 1 більше i
        q.enqueue(pl)                          #додати гравця до кінця черги

    print('\nПослідовність номерів, що вибувають')
    while not q.empty():
        for i in range(m-1):                    #m-1 раз перекласти гравця з початку до кінця черги
            q.enqueue(q.dequeue())
        pl = q.dequeue()                       #узяти m-го гравця з початку черги
        print(pl)                               #та показати його номер


count_counter()
