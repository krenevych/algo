"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""

en_words = []
ua_words = []

def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.

    :param eng: англійське слово
    :param translation: переклад
    """
    en_words.append(eng)
    ua_words.append(translation)



def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    left = 0                # Індекс лівого елементу
    right = len(en_words) - 1  # Індекс правого елементу

    while left < right:
        m = left + (right - left) // 2  # Індекс середнього елементу
        if eng > en_words[m]:
            left = m + 1
        else:
            right = m

    found = en_words[right]

    if found == eng:
        return ua_words[right]
    else:
        return ""


