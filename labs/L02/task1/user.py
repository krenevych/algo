"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""

dict_en = []
dict_ua = []

def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.

    :param eng: англійське слово
    :param translation: переклад
    """
    dict_en.append(eng)
    dict_ua.append(translation)


def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    # eng = transmigrate
    left = 0
    right = len(dict_en) - 1
    while left < right:
        m = left + (right - left) // 2 # m = (left + right) // 2 <- for Python only
        curent_eng = dict_en[m]  # curent_eng = instill
        if eng > curent_eng:
            left = m + 1
        else:
            right = m

    if dict_en[left] == eng:
        return dict_ua[left]

    return ""
