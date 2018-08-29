from source.T4.P41_Stack.Stack import Stack
from source.utils.annotation import annotation

" Словник операторів, що використовуються у калькуляторі та їхні пріоритети "
OPERATORS = {
    "+": 1,  # Оператор додавання та його пріорітет
    "-": 1,  # Оператор віднімання та його пріорітет
    "*": 2,  # Оператор множення та його пріорітет
    "/": 2,  # Оператор ділення та його пріорітет
}

class StringCalculator:
    """ Клас рядковий калькулятор.

        Обчислює значення арифметичного виразу використовуючи обернений польский запис
    """

    def __init__(self, str_expression):
        """ Конструктор

        :param str_expression: рядок, що містить правильний арифметичний вираз у інфіксному вигляді.
        """
        self.mInfixStr = str_expression               # Поле (рядок), що містить арифметичний вираз у інфіксному вигляді
        self.mPostfixList = self.convert_to_polish()  # Поле (список), що містить арифметичний вираз у постфіксному вигляді

        # self.set_expression(str_expression)         # замість двох попередніх рядків краще викликати відповідний метод

    def set_expression(self, str_expression):
        """ Задає калькулятору арифметичний вираз

        Для спрощення передбачається, що вхідний параметр

        :param str_expression: рядок, що містить правильний арифметичний вираз у інфіксному вигляді.
        :return: None
        """
        self.mInfixStr = str_expression
        self.mPostfixList = self.convert_to_polish()

    def convert_to_polish(self):
        """ Конвертує арифметичний вираз з інфіксного у постфіксний вигляд

            Для коректної роботи цього методу, передбачається, що у рядку
            (що містить арифметичний вираз) усі операнди, оператори та дужки
            записуються через символ пропуску, наприклад "25 * ( 3 + 5 )"

        :return: Рядок, що містить арифметичний вираз у постфіксному вигляді
        """
        infix_list = self.mInfixStr.split()  # Розділяємо рядок на токени
        postfix_list = []  # Список, що міститиме вираз у постфіксному вигляді
        stack = Stack()    # Допоміжний стек арифметичних операторів та дужок
        for token in infix_list:    # Ітеруємо по всіх токенах інфіксного виразу
            if token in OPERATORS:  # токен є оператором

                while not stack.empty():
                    prev = stack.top()  # підглянемо попередній оператор зі стеку
                    # Якщо попередній токен є оператором
                    # пріорітет якого вищий за пріорітет поточного оператора
                    if prev in OPERATORS and OPERATORS[prev] >= OPERATORS[token]:
                        stack.pop()                # Видаляємо його зі стеку операторів
                        postfix_list.append(prev)  # Додаємо його до постфіксного списку
                    else:
                        break

                stack.push(token)  # кладемо поточний оператор у стек

            elif token == "(":     # токен є лівою дужкою,
                stack.push(token)  # кладемо його в стек

            elif token == ")":     # якщо токен є правою дужкою,
                it = stack.pop()   # Виштовхуємо елементи зі стеку опертаорів stack
                while it != "(":   # доки не знайдемо відповідну ліву дужку.
                    postfix_list.append(it)  # при цьому кожен оператор додаємо до списку
                    it = stack.pop()

            else:                           # якщо токен є операндом
                postfix_list.append(token)  # додаємо його у кінець постфіксногосписку.

        while not stack.empty():
            postfix_list.append(stack.pop())

        return postfix_list

    @staticmethod
    def simple_operation(left, right, operator):
        """ Допоміжний метод, що обчислює значення виразу "left operator right"

        :param left: лівий операнд
        :param right: правий операнд
        :param operator: оператор
        :return: значення виразу "left operator right"
        """

        assert operator in OPERATORS

        left = float(left)
        right = float(right)

        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left / right

    def calculate_by_polish(self):
        """ Обчилює значення виразу використовуючи оберенений польский запис

        :return: Значення арифметичного виразу
        """
        stack = Stack()
        for token in self.mPostfixList:

            if token in OPERATORS:           # Якщо поточний токен оператор
                right_operand = stack.pop()  # Дістаємо перший елемент зі стеку - він відповідає правому операнду
                left__operand = stack.pop()  # Дістаємо другий елемент зі стеку - він відповідає лівому операнду
                # Обчислюємо значення простого арифмтемтиного виразу
                res = self.simple_operation(left__operand, right_operand, token)
                stack.push(res)    # Кладемо результат обчислень у стек

            else:                  # Якщо поточний токен є операндом
                stack.push(token)  # Кладемо його у стек

        return stack.pop()

    def __str__(self):
        """ Перетворення об'єкту до рядкового вигляду

        :return: Рядок, що містить обернений польський запис арифметинчого виразу
        """
        str_postfix = ""
        for el in self.mPostfixList:
            str_postfix += el + " "

        return str_postfix

    def __float__(self):
        """ Повератає float-значення поточного арифметичного виразу

        :return: значення поточного арифметичного виразу
        """
        return self.calculate_by_polish()

    def __int__(self):
        """ Повератає int-значення поточного арифметичного виразу

        :return: ціла частина значення поточного арифметичного виразу
        """
        return int(self.calculate_by_polish())


@annotation
def calculate_test_case(s):
    s_or_numbers = s.format(*numbers)

    calc = StringCalculator(s_or_numbers)

    print(str(calc) + " = " + str(float(calc)))

    # ========= Check using function eval ====================
    print("Infix    = " + s_or_numbers + " = " + str(eval(s_or_numbers)))


if __name__ == "__main__":
    A = "15"
    B = "5"
    C = "12"
    D = "3"
    E = "11"
    F = "4"
    G = "2"
    H = "9"

    letters = ("A", "B", "C", "D", "E", "F", "G", "H")
    numbers = (A, B, C, D, E, F, G, H)

    ssss = (
        "{} + {} * {} + {}",
        "( {} + {} ) * ( {} + {} )",
        "{} * ( ( {}  + {} ) + {} )",
        "{} + {}  + {} + {}",
        "{} / {}  + {} / {}",
        "{} + {}  + {} * {}",
        "{} - {} * {} + {}",
        "( {} - {} ) *  {} / ( {}  * {} ) * {} + {} * {}",
    )

    for s in ssss:
        calculate_test_case(s)
