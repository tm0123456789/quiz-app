from enum import Enum


class AnswerOptionTF(str, Enum):
    T = 't'
    F = 'f'


class AnswerOptionMC(str, Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
