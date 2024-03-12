from enum import Enum


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4

    def __str__(self):
        return self.name

    @classmethod
    def has_value(cls, value):
        return value in cls._member_names_
