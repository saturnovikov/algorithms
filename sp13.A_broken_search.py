# ID: 73120249
"""
Алла ошиблась при копировании из одной структуры данных в другую. Она хранила
массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию, и в
нём можно было найти элемент за логарифмическое время. Алла скопировала
данные из кольцевого буфера в обычный массив, но сдвинула данные исходной
отсортированной последовательности. Теперь массив не является отсортированным.
Тем не менее, нужно обеспечить возможность находить в нем элемент за O(log n).
Можно предполагать, что в массиве только уникальные элементы.
Требуется реализовать функцию, осуществляющую поиск в сломанном массиве.
Функция должна вернуть индекс элемента, равного item_find, если такой есть в
массиве (нумерация с нуля). Если элемент не найден, функция должна
вернуть: -1.
Изменять массив нельзя.

"""

from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    """
    Возвращает исходные данные для задачи.
    В первой строке записано число n - длина массива.
    Во второй строке записано положительное число desired_item — искомый
    элемент.
    На третьей строк через пробел записано n натуральных чисел – элементы
    массива.

    :rtype desired_item: int
    :return desired_item: искомый элемент, целое число.

    :rtype data: List
    :return data: массив из чисел.

    """

    _ = int(input())
    desired_item = int(input())
    data = list(map(int, input().strip().split()))
    return desired_item, data


def begin_index_item(arr: list, left: int = 0, right: int = None) -> int:
    """
    Функция для нахождения индекса элемента, с которого
    начинается сортировка.
    Применен алгоритм бинарного поиска.

    :param arr: массив, в котором необходимо найти элемент, с которого
    начинается сортировка.
    :type arr: list

    :param left: индекс элемента в массиве, с которого начинать поиск.
                 по умолчанию: 0
    :type left: int

    :param right: индекс элемента в массиве, на котором нужно закончить
                поиск.
                по умолчанию: None (в функции преобразуется
                в последнй элемент)
    :type right: int

    :rtype mind: int
    :return mind: индекс первого элемента стека.
    """

    if right is None:
        right = len(arr)-1
    if len(arr) in (1, 2):
        return 0
    mind = (right+left)//2
    if arr[mind] >= arr[mind+1]:
        return mind
    if arr[left] > arr[mind]:
        return begin_index_item(arr, left, mind)
    else:
        return begin_index_item(arr, mind, right)


def binary_search(arr: list, desired_item: int, left: int, right: int) -> int:
    """
    Функция для нахождения в массиве элемента.
    Применен алгоритм бинарного поиска.
    Выводит индекс искомого элемента или -1, если искомого элемента
    нет в массиве.

    :param arr: массив, в котором необходимо найти элемент.
    :type arr: list

    :param desired_item: массив, в котором необходимо найти элемент.
    :type desired_item: int

    :param left: индекс элемента в массиве, с которого начинается поиск.
    :type left: int

    :param right: индекс элемента в массиве, на котором нужно закончить
                поиск.
    :type right: int

    :rtype mind: int
    :return mind: индекс искомого элемента.
    """

    if right <= left:
        return -1
    mind = (left+right)//2
    if arr[mind] == desired_item:
        return mind
    if arr[mind] > desired_item:
        return binary_search(arr, desired_item, left, mind)
    else:
        return binary_search(arr, desired_item, mind+1, right)


def broken_search(arr, desired_item) -> int:
    if arr[0] > arr[-1]:
        mind = begin_index_item(arr)
        if arr[mind] == desired_item:
            index = mind
        elif arr[mind] >= desired_item >= arr[0]:
            index = binary_search(arr, desired_item, left=0, right=mind)
        else:
            index = binary_search(arr, desired_item, left=mind+1,
                                  right=len(arr))
    else:
        index = binary_search(arr, desired_item, left=0, right=len(arr))
    if index == -1:
        return -1
    else:
        return index


if __name__ == '__main__':
    desired_item, data = read_input()
    print(broken_search(data, desired_item))
