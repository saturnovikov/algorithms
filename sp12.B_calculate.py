# ID: 71917096
import math
from typing import List


def read_input() -> List[str]:
    """
    Возвращает исходные данные для задачи.

    :rtype: list
    :return data: выражение, записанное в обратной польской нотации.
    Числа и арифметические операции записаны через пробел.
    На вход могут подаваться операции: +, -, *, / и числа, по модулю не
    превосходящие 10000.

    """

    data = list(map(str, input().strip().split()))
    return data


class Stack():
    """
    Класс для вычисления значения выражения, записанного в обратной польской
    нотации.
    Организован через стек.
    """

    mathematical_action = {
        '*': lambda x, y: x*y,
        '/': lambda x, y: math.floor(y/x),
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x
    }

    def __init__(self):
        self.__items = []

    def push(self, item):
        """
        Добавляет элемент на вершину стека.

        :param item: элемент для добавления в cтек
        :type item: Any
        """

        self.__items.append(item)

    def pop(self):
        """
        Удаляет элемент с вершины стека.
        """

        self.__items.pop()

    def peek(self):
        """
        Возвращает элемент с вершины стека.
        """

        return self.__items[-1]

    def items(self):
        """
        Возвращает первый и второй элемент стека.
        """

        return int(self.__items[-1]), int(self.__items[-2])


if __name__ == '__main__':
    data = read_input()
    number_of_elements = len(data)
    instance = Stack()
    index = 0
    while index < number_of_elements:
        if data[index] not in instance.mathematical_action:
            instance.push(data[index])
        else:
            x, y = instance.items()
            volume = instance.mathematical_action[data[index]](x, y)
            for _ in range(2):
                instance.pop()
            instance.push(volume)
        index += 1
    print(instance.peek())
