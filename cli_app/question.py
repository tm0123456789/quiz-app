from constants import AnswerOptionMC, AnswerOptionTF


class Question:
    def __init__(
        self,
        points: int = 0,
        text: str = "",
        correct_answer: str = ""
    ) -> None:
        self.points = points
        self.text = text
        self.correct_answer = correct_answer
        self.is_correct = False


class QuestionTF(Question):
    """Class for True/False questions"""

    def __init__(
            self,
            points: int = 0,
            text: str = "",
            correct_answer: AnswerOptionTF = ""
    ) -> None:
        super().__init__(points, text, correct_answer)

    def ask(self) -> None:
        while True:

            # print question and answer options
            print(f'(T)rue or (F)alse: {self.text}')
            response = input('? ').lower()

            # validate input
            if (len(response) == 0) or (not response in [i for i in AnswerOptionTF]):
                print('Not valid response. Please try again...')
                continue

            # check the answer
            elif response == self.correct_answer:
                self.is_correct = True

            break


class AnswerMC:
    def __init__(
        self,
        option: AnswerOptionMC = "",
        text: str = ""
    ) -> None:
        self.option = option
        self.text = text


class QuestionMC(Question):
    """Class for multiple-choice questions"""

    def __init__(
        self,
        points: int = 0,
        text: str = "",
        correct_answer: AnswerOptionMC = "",
        answers: list[AnswerMC] = None
    ) -> None:
        super().__init__(points, text, correct_answer)
        self.answers = answers if answers else []

    def ask(self):
        while True:

            # print question and answer options
            print(self.text)
            for a in self.answers:
                print(f'[{a.option}] {a.text}')

            response = input('? ').lower()

            # validate input
            if (len(response) == 0) or (not response in [i for i in AnswerOptionMC]):
                print('Not valid response. Please try again...')
                continue

            # check the answer
            elif response == self.correct_answer:
                self.is_correct = True

            break


# if __name__ == '__main__':
#     q1 = QuestionTF(5, 'Is 2+2 equals 4?', 't')
#     q1.ask()
#     q2 = QuestionMC(10, 'What is 2+2?', 'a',
#                     [AnswerMC('a', '4'), AnswerMC('b', '5'), AnswerMC('c', '2'), AnswerMC('d', '8')])
#     q2.ask()
#     print(q1.is_correct)
#     print(q2.is_correct)
