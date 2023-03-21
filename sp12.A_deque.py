# ID: 71998899
from typing import Tuple


class EmptyError(Exception):
    """
    Дек пустой.
    """

    pass


class CrowdedError(Exception):
    """
    В деке уже находится максимальное число элементов.
    """

    pass


class DeQue():
    """
    Класс для реализации структуры данных Дек.
    Размер Дэка определяется заданным числом - max_size_deque.
    Внимание: при реализации используеся кольцевой буфер.

    """

    def __init__(self, max_size_deque: int) -> None:
        self.__deque = max_size_deque * [None]
        self.__max_deque = max_size_deque
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def push_back(self, value):
        """
        Добавляет элемент в конец дека. Если в деке уже находится максимальное
        число элементов, выводит «error».

        :param value: элемент для добавления в дек
        :type value: int
        """

        if len(self.__deque) == self.__size:
            raise CrowdedError('error')
        self.__deque[self.__tail] = value
        self.__size += 1
        self.__tail = (self.__tail + 1) % self.__max_deque
        self.__head = (self.__tail - self.__size - 1) % self.__max_deque

    def push_front(self, value):
        """
        Добавляет элемент в начало дека. Если в деке уже находится максимальное
        число элементов, выводит «error».

        :param value: элемент для добавления в дек
        :type value: int
        """

        if len(self.__deque) == self.__size:
            raise CrowdedError('error')
        self.__deque[self.__head] = value
        self.__size += 1
        self.__head = (((self.__head - 1) * (-1)) % self.__max_deque) * (-1)
        self.__tail = (self.__head + self.__size + 1) % self.__max_deque

    def pop_front(self):
        """
        Выводит первый элемент дека и удаляет его. Если дек был пуст,
        то выводит «error».
        """

        if self.__size == 0:
            raise EmptyError('error')
        self.__head = (((self.__head + 1) * (-1)) % self.__max_deque) * (-1)
        value = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__size -= 1
        if self.__size == 0:
            self.__tail = (((self.__tail - 1) * (-1)) %
                           self.__max_deque) * (-1)
        return value

    def pop_back(self):
        """
        Выводит последний элемент дека и удаляет его. Если дек был пуст,
        то выводит «error».
        """

        if self.__size == 0:
            raise EmptyError('error')
        self.__tail = (((self.__tail - 1) * (-1)) % self.__max_deque) * (-1)
        value = self.__deque[self.__tail]
        self.__deque[self.__tail] = None
        self.__size -= 1
        if self.__size == 0:
            self.__head = (((self.__head + 1) * (-1)) %
                           self.__max_deque) * (-1)
        return value


def read_input() -> Tuple[list, int]:
    """
    Возвращает исходные данные для задачи.
    В первой строке записано количество команд number_operation — целое число,
    не превосходящее 100000. Во второй строке записано число max_size_deque —
    максимальный размер дека. Он не превосходит 50000. В следующих строках
    записана одна из команд: push_back(value), push_front(value), pop_front(),
    pop_back().

    number_operation: количество команд, n — целое число,
    не превосходящее 100000.

    :rtype operations: list
    :return operations: команды: push_back(value) – добавить элемент
                                 в конец дека

                                 push_front(value) – добавить элемент
                                 в начало дека

                                 pop_front() – вывести первый элемент дека
                                 и удалить его

                                 pop_back() – вывести последний элемент дека
                                 и удалить его
    :rtype max_size_deque: int
    :return max_size_deque: максимальный размер дека.
    """

    number_operation = int(input())
    max_size_deque = int(input())
    operations = list((input() for _ in range(number_operation)))
    return operations, max_size_deque


if __name__ == '__main__':
    operations, max_size_deque = read_input()
    instance = DeQue(max_size_deque)
    counter = 1
    for value in operations:
        new_value = value.split(' ')
        try:
            if getattr(instance, new_value[0], False):
                operation = getattr(instance, new_value[0])
                if len(new_value) == 2:
                    operation(new_value[1])
                else:
                    print(operation())
            else:
                print(f'Error: ошибка в исходных данных \n'
                      f'Проверьте название операции №{counter}: {new_value[0]}')
                break
            counter += 1
        except (EmptyError, CrowdedError) as error:
            print(error)
