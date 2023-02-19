import os

from quizparser import QuizParser


class QuizManager:
    def __init__(self, quizfolder: str):
        self.quizfolder = quizfolder
        self.the_quiz = None    # most recently selected quiz
        self.quizzes = dict()   # collection of quizzes
        self.results = None     # results of the most recent quiz
        self.quiztaker = ''     # name of the person taking the quiz

        if not os.path.exists(quizfolder):
            raise FileNotFoundError('Quiz folder does not exist')
        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)

    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"[{k}]: {v.name}")

    def take_quiz(self, quiz_num: int, username: str):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quiz_num]
        self.results = self.the_quiz.take_quiz()

    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)


# if __name__ == '__main__':
#     qm = QuizManager('quizzes')
#     qm.list_quizzes()
