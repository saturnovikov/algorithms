# ID: 70564277
from typing import Tuple


def sleight_of_hand(number_of_buttons: int, data: str) -> int:
    """
    Функция для решения задачи "Ловкость рук".
    Игра «Тренажёр для скоростной печати» представляет собой поле из
    клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и
    точек. На клавише написана либо точка, либо цифра от 1 до 9.
    В момент времени t (1-9) игрок должен одновременно нажать на все клавиши,
    на которых написана цифра t (1-9). Гоша и Тимофей могут нажать в один
    момент времени на k клавиш каждый. Если в момент времени t нажаты все
    нужные клавиши, то игроки получают 1 балл.
    Найдите число баллов, которое смогут заработать Гоша и Тимофей,
    если будут нажимать на клавиши вдвоём.

    :param number_of_buttons: число клавиш от [1 до 5]
    :type number_of_buttons: int
    :param data: строка с конфигурацией цифр и точек. Либо точка, либо цифра
    от [1 до 9]
    :type data: str

    :rtype: int
    :return: число баллов, которые смогут заработать участники.
    """

    unique_values = set(data)
    if len(unique_values) == 1 and '.' in unique_values:
        return 0
    unique_values.discard('.')
    scores = 0
    for element in unique_values:
        if data.count(element) <= 2*number_of_buttons:
            scores += 1
    return scores


def read_input() -> Tuple[int, str]:
    """
    Возвращает исходные данные для задачи.
    В первой строке вводится number_of_buttons.
    В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой
    строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной
    строки идут подряд и не разделены пробелами.

    :rtype number_of_buttons: int
    :return number_of_buttons: число клавиш от [1 до 5]
    :rtype data: str
    :return data: строка с конфигурацией цифр и точек. Либо точка, либо цифра
    от [1 до 9]
    """

    number_of_buttons = int(input())
    data = "".join((input() for _ in range(4)))
    return number_of_buttons, data


if __name__ == '__main__':
    number_of_buttons, data = read_input()
    print(sleight_of_hand(number_of_buttons, data))
