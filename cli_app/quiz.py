from question import QuestionMC, QuestionTF


class Quiz:
    def __init__(
        self,
        name: str = "",
        description: str = "",
        questions: list[QuestionMC | QuestionTF] = None
    ):
        self.name = name
        self.description = description
        self.questions = questions if questions else []
        self.score = 0
        self.correct_count = 0
        self.total_points = sum(
            q.points for q in self.questions) if self.questions else 0

    def print_header(self):
        print(f'QUIZ NAME: {self.name}')
        print(f'DESCRIPTION: {self.description}')
        print(f'QUESTIONS: {len(self.questions)}')
        print(f'TOTAL POINTS: {self.total_points}')
        print('---------------------------------------------\n')

    def print_results(self, quiztaker):
        print(f'Congratulations, {quiztaker}!')
        print(
            f'You answered {self.correct_count} out of {len(self.questions)} questions')
        print(f'Your score: {self.score} out of {self.total_points}')
        print('---------------------------------------------\n')

    def take_quiz(self):
        # initialize quiz state
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        # print header
        self.print_header()

        # execute each question
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points

        print('---------------------------------------------\n')

        # return the results
        return (self.score, self.correct_count, self.total_points)


# if __name__ == '__main__':
#     from question import AnswerMC
#     q1 = QuestionTF(5, 'Is 2+2 equals 4?', 't')
#     q2 = QuestionMC(10, 'What is 2+2?', 'a',
#                     [AnswerMC('a', '4'), AnswerMC('b', '5'), AnswerMC('c', '2'), AnswerMC('d', '8')])
#     quiz = Quiz('Quiz_1', 'Test quiz', [q1, q2])
#     result = quiz.take_quiz()
#     print(result)
