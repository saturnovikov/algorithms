# ID: 73204596
"""
Тимофей решил организовать соревнование по спортивному программированию,
чтобы найти талантливых стажёров. Задачи подобраны, участники
зарегистрированы, тесты написаны. Осталось придумать, как в конце
соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится,
к нему будут привязаны два показателя: количество решённых задач Pi и
размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное
на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении
двух участников выше будет идти тот, у которого решено больше задач. При
равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же
и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в
алфавитном (лексикографическом) порядке.
Для отсортированного списка участников выведите по порядку их логины
по одному в строке.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Intern():
    """
    Класс информации участников.
    login: логин участника.
    solved_tasks: количество решенных задач.
    penalty: штраф. Начисляется за неудачные попытки и время,
    затраченное на задачу.
    """

    _login: str
    _solved_tasks: int
    _penalty: int

    def __post_init__(self):
        self._solved_tasks = int(self._solved_tasks)
        self._penalty = int(self._penalty)

    def __gt__(self, other):
        """
        Метод сравнения экземпляра класса.
        Описана логика сравнения двух участников.
        """

        return (-self._solved_tasks, self._penalty, self._login) < (
            -other._solved_tasks, other._penalty, other._login)

    def __str__(self) -> str:
        return f'{self._login}'


def read_input() -> List[Intern]:
    """
    Возвращает исходные данные для задачи.
    В первой строке задано число участников (number_of_interns).
    В каждой из последующих строк задана информация про одного из
    участников.

    number_of_interns: число участников, целое число,
    1 ≤ number_of_interns ≤ 100 000.

    :rtype data: list
    :return data: информация про участника: уникальный логин (строка из
                                           строчных латинских букв
                                           длиной не более 20)

                                           число решённых задач Pi

                                           штраф Fi

                                           Fi и Pi — целые числа, лежащие в
                                           диапазоне от 0 до 10^9
    """

    number_of_interns = int(input())
    data = list(Intern(*(input().split()))
                for _ in range(number_of_interns))
    return data


def quicksort_revers(arr: list, begin: int = 0, end: int = None) -> List:
    """
    Метод быстрой реверсионной сортировки,
    модификация in-place.

    :param arr: массив для сортировки
    :type arr: Any[Any]

    :param begin: индекс элемента в массиве, с которого нужно начинать
                  сортировку, по умолчанию: 0
    :type begin: int

    :param end: индекс элемента в массиве, на котором нужно закончить
                сортировку.
                по умолчанию: None (в функции преобразуется
                в последнй элемент)
    :type end: int

    :rtype arr: List
    :return arr: отсортированный массив.
    """

    if end is None:
        end = len(arr)-1
    if begin >= end:
        return
    pivot = arr[begin]
    left, right = begin, end
    while left <= right:
        while arr[left] > pivot:
            left += 1
        while arr[right] < pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    quicksort_revers(arr, begin, right)
    quicksort_revers(arr, left, end)
    return arr


if __name__ == '__main__':
    interns = read_input()
    quicksort_revers(interns)
    print(*interns, sep='\n')
