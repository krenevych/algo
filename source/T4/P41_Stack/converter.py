from source.T4.P41_Stack.Stack_recursively import Stack


def get_char_digit(digit):
    """ Допоміжний метод, що за числом повертає символ-цифру системи числення

    0 -> '0'
    ...
    9 -> '9'
    10 -> 'A'
    ...
    15 -> 'F'

    :param digit: число з проміжку 0,.., 15
    :return: рядок що місить символ-цифру системи числення
    """

    assert digit <= 16
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)

    return str_digit

def convert(dec_number, base):
    """ перетворює задане десяткове число, до заданої системи числення

    :param dec_number: десяткове число
    :param base: основа системи числення [2, 16]
    :return: рядок-число у системи числення з основою base
    """

    assert 2 <= base <= 16

    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    converted = ""
    while not stack.empty():
        converted = converted + get_char_digit(stack.pop())

    return converted


# For testing
if __name__ == "__main__":
    print(convert(100, 2))
    print(convert(63, 8))
    print(convert(102234, 11))
    print(convert(2286755, 16))
