from source.T5_LinearStructure.P1_Stack.L5_2_Stack_recursively import Stack

def bracketsChecker(brackets_sequence):
    """ Перевіряє чи brackets_sequence правильна дужкова послідовність

    :param brackets_sequence: дужкова послідовність
    :return: True, якщо brackets_sequence - правильна дужкова послідовність
    """
    s = Stack()  # Створюємо порожній стек
    for bracket in brackets_sequence:
        if bracket == "(":
            s.push(bracket)  # Потенційний початок контейнера
        else:
            if s.empty():
                return False # Дужкова послідовність не правильна
            else:
                s.pop()      # Прибираємо контейнер з розгляду

    return s.empty()

# For testing
if __name__ == "__main__":
    print(bracketsChecker('(()())'))
    print(bracketsChecker('(()()()())'))
    print(bracketsChecker('((()))'))
    print(bracketsChecker(')()('))
    print(bracketsChecker('(((()'))
    print(bracketsChecker('())))'))
