from typing import Union


class Technic:
    __slots__ = ('_name', '_price', '_cash')

    def __init__(self, name: str, price: Union[int, float], cash: bool):
        self._name = name
        self._price = price
        self._cash = cash

    # @property
    # def category(self):
    #     return 'Дорогой' if self.price > 1000 else 'Бюджетный'

    def __len__(self):
        # - для нахождения длины названия с помощью len()
        return len(self._name)

    def __eq__(self, other):
        # – для равенства ==
        if isinstance(other, self.__class__):
            return len(self) == len(other)

    def __ne__(self, other):
        # – для неравенства !=
        if isinstance(other, self.__class__):
            return len(self) != len(other)

    def __lt__(self, other):
        # – для оператора меньше <
        if isinstance(other, self.__class__):
            return len(self) < len(other)

    def __le__(self, other):
        # – для оператора меньше или равно <=
        if isinstance(other, self.__class__):
            return len(self) <= len(other)

    def __gt__(self, other):
        # – для оператора больше >
        if isinstance(other, self.__class__):
            return len(self) > len(other)

    def __ge__(self, other):
        # – для оператора больше или равно >=
        if isinstance(other, self.__class__):
            return len(self) >= len(other)
