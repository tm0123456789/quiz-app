from constants import YesNo
from quizmanager import QuizManager


class QuizApp:
    QUIZ_FOLDER = 'quizzes'

    def __init__(self):
        self.username = ""
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def hello(self):
        print('---------------------------------------------')
        print('------------------ Welcome ------------------')
        print('---------------------------------------------')

        self.username = input('What is your name? ')
        print(f'Welcome, {self.username}')

    def goodbye(self):
        print('---------------------------------------------')
        print(f'See you, {self.username}!')
        print('---------------------------------------------')
        print()

    # ==================== MENU ====================

    def menu_error(self):
        print('Not valid selection. Please try again...')
        print('---------------------------------------------\n')

    def menu_header(self):
        print('Please make a selection:')
        print('[M] - menu')
        print('[L] - list quizes')
        print('[T] - take a quiz')
        print('[Q] - quit')
        print('---------------------------------------------\n')

    def menu(self):
        self.menu_header()

        while (True):
            selection = input("What is your choice? ").capitalize()

            match selection:

                # menu
                case 'M':
                    self.menu_header()
                    continue

                # quit
                case 'Q':
                    self.goodbye()
                    break

                # list quizzes
                case 'L':
                    print('Available quizes:')
                    self.qm.list_quizzes()
                    print('---------------------------------------------\n')

                    continue

                # take quiz
                case 'T':
                    # select quiz
                    while (True):
                        try:
                            quiz_num = int(input('Quiz number: '))
                            if not quiz_num in self.qm.quizzes:
                                raise
                            print(f'Quiz N {quiz_num} selected!')
                            print('---------------------------------------------\n')
                            break
                        except:
                            self.menu_error()
                            continue
                    # take quiz
                    self.qm.take_quiz(quiz_num, self.username)
                    self.qm.print_results()

                    # save the results
                    do_save = input('Save the results? (y/n) ').lower()
                    while (True):
                        match do_save:
                            case YesNo.Y:
                                self.qm.save_results()
                                break
                            case YesNo.N:
                                print('Ok, good luck')
                                break
                            case _:
                                self.menu_error()
                                continue
                    break
                case _:
                    self.menu_error()
                    continue

    # ==================== RUN ====================

    def run(self):
        self.hello()
        self.menu()


if __name__ == '__main__':
    app = QuizApp()
    app.run()
