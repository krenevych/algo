

def annotation(f):
    """ Декоратор @annotation. """
    def __annotation(*args, **kw):  # функція __annotation містить код, що виконується
                                    # перед та після виклику f
        print()
        print("====== %s ============" % f.__name__)
        rez = f(*args, **kw)        # викликаємо f
        print("======================")
        return rez
    return __annotation

