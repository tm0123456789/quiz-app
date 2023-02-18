from enum import Enum


class AnswerOptionTF(str, Enum):
    T = 't'
    F = 'f'


class AnswerOptionMC(str, Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'


class QuestionType(str, Enum):
    TF = 'tf'
    MC = 'mc'


class Tag(str, Enum):
    QUIZ = "Quiz"
    DESCRIPTION = "Description"
    QUESTION = "Question"
    QUESTION_TEXT = "QuestionText"
    ANSWER = "Answer"
