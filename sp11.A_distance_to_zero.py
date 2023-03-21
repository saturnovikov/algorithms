# ID: 70564171
from typing import List


def nearest_zero(data: List[int]) -> List[int]:
    """
    Функция для решения задачи "Ближайший ноль".
    Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет
    жить, имеет длину n, то есть состоит из n одинаковых идущих подряд
    участков. Каждый участок либо пустой, либо на нём уже построен дом.
    Общительный Тимофей не хочет жить далеко от других людей на этой улице
    Поэтому ему важно для каждого участка знать расстояние до ближайшего
    пустого участка. Если участок пустой, эта величина будет равна нулю—
    расстояние до самого себя.
    Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть
    карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором
    строились, поэтому их номера на карте никак не упорядочены. Пустые
    участки обозначены нулями.
    Гарантируется, что в последовательности есть хотя бы один ноль.

    :param data: строка из n целых неотрицательных чисел — номера домов и
    обозначения пустых участков на карте (нули)
    :type data: list

    :rtype: list
    :return: возвращает список с расстоянием до ближайшего пустого
    участка (нуля) для каждого из участков.
    """

    new_value = 1
    zero_indexes = list()
    for index_data in range(len(data)):
        if data[index_data] == 0:
            zero_indexes.append(index_data)
            if len(zero_indexes) > 2:
                zero_indexes.pop(0)
            if index_data != 0 and len(zero_indexes) == 1:
                distance_to_first_zero(index_data, data)
            elif 0 < index_data < len(data):
                if zero_indexes[1] - zero_indexes[0] != 1:
                    distance_between_zeros(zero_indexes, data)
            new_value = 1
        else:
            data[index_data] = new_value
            new_value += 1
    return data


def read_input() -> List[int]:
    """
    Возвращает исходные данные для задачи.

    :rtype: list
    :return data: n целых неотрицательных чисел — номера домов и обозначения
    пустых участков на карте (нули)
    """

    _ = input().strip()
    data = list(map(int, input().strip().split()))
    return data


def distance_to_first_zero(current_index_data: int,
                           data: List[int]) -> List[int]:
    """
    Вспомогательная функция для nearest_zero.
    Возвращает список с расстояниями от участков до
    первого пустого участка (нуля)

    :param current_index_data: индекс пустого участка (нуля)
    :type data: int

    :param data: строка из n целых неотрицательных чисел — номера домов и
    обозначения пустых участков на карте (нули)
    :type data: list
    """

    new_value = 1
    for index_data in range(current_index_data-1, -1, -1):
        data[index_data] = new_value
        new_value += 1
    return data


def distance_between_zeros(zero_indexes: List[int],
                           data: List[int]) -> List[int]:
    """
    Вспомогательная функция для nearest_zero.
    Возвращает список с расстояниями от участков, находящиеся
    между пустыми участками (нулями), до пустого участка (нуля).

    :param zero_indexes: список с индексами пустых участков (нулей)
    :type data: list

    :param data: строка из n целых неотрицательных чисел — номера домов и
    обозначения пустых участков на карте (нули)
    :type data: list
    """

    new_value = 1
    for index_data in range(zero_indexes[1]-1,
                            (zero_indexes[1]+zero_indexes[0])//2, -1):
        data[index_data] = new_value
        new_value += 1
    return data


if __name__ == '__main__':
    data = read_input()
    print(*nearest_zero(data))
