import xml.sax
from question import AnswerMC
from quiz import *
from constants import QuestionType, Tag
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUESTION_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):

    def __init__(self):
        self.new_quiz = Quiz()
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, path):
        with open(path, "r") as f:
            text = f.read()
        xml.sax.parseString(text, self)
        return self.new_quiz

    def startElement(self, tagname, attrs):
        """method is called when the parser finishes parsing the opening tag of an XML element"""
        match tagname:

            case Tag.QUIZ:
                self._parse_state = QuizParserState.PARSE_QUIZ
                self.new_quiz.name = attrs["name"]

            case Tag.DESCRIPTION:
                self._parse_state = QuizParserState.PARSE_DESCRIPTION

            case Tag.QUESTION:
                self._parse_state = QuizParserState.PARSE_QUESTION
                if attrs["type"] == QuestionType.MC:
                    self._current_question = QuestionMC()
                elif attrs['type'] == QuestionType.TF:
                    self._current_question = QuestionTF()
                self._current_question.points = int(attrs["points"])
                self.new_quiz.total_points += self._current_question.points

            case Tag.QUESTION_TEXT:
                self._parse_state = QuizParserState.PARSE_QUESTION_TEXT
                self._current_question.correct_answer = attrs["answer"]

            case Tag.ANSWER:
                self._current_answer = AnswerMC()
                self._current_answer.option = attrs["option"]
                self._parse_state = QuizParserState.PARSE_ANSWER

    def endElement(self, tagname):
        """method is called when the parser finishes with a closing XML tag"""
        match tagname:

            case Tag.QUIZ:
                self._parse_state = QuizParserState.IDLE

            case Tag.DESCRIPTION:
                self._parse_state = QuizParserState.PARSE_QUIZ

            case Tag.QUESTION:
                self.new_quiz.questions.append(self._current_question)
                self._parse_state = QuizParserState.PARSE_QUIZ

            case Tag.QUESTION_TEXT:
                self._parse_state = QuizParserState.PARSE_QUESTION

            case Tag.ANSWER:
                self._current_question.answers.append(self._current_answer)
                self._parse_state = QuizParserState.PARSE_QUESTION

    def characters(self, content):
        """method is called when the parser finishes processing text content"""
        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += content
        elif self._parse_state == QuizParserState.PARSE_QUESTION_TEXT:
            self._current_question.text += content
        elif self._parse_state == QuizParserState.PARSE_ANSWER:
            self._current_answer.text = content


# if __name__ == '__main__':
#     app = QuizParser()
#     quiz = app.parse_quiz("./quizzes/SampleQuiz.xml")
#     print(quiz.name)
#     print(quiz.description)
#     print(len(quiz.questions))
#     print(quiz.total_points)
#     for q in quiz.questions:
#         print(q.text)
