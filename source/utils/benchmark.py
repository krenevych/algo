#T17_11_v1
#Декоратор для обчислення часу виконання функції


def benchmark(f):
    """ Декоратор @benchmark для обчислення часу виконання функції f. """
    import time
    def _benchmark(*args, **kw): #функція _benchmark містить код, що виконується
                                 #перед та після виклику f
        t = time.clock()            #вимірюємо час перед викликом функції
        rez = f(*args, **kw)        #викликаємо f
        t = time.clock() - t        #вимірюємо різницю у часі після виклику функції
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark

