from typing import List


class Question(object):
    def __init__(self,
                 qtext : str,
                 qformat):

        self.format = qformat
        self.text = qtext

        #print(qformat)
        #print(self.text)

    def get_format(self, name : str):
        return self.format[name]

    def set_format(self, name: str, prep_format):
        self.format[name] = prep_format


class Answer(object):
    def __init__(self,
                 nr: int,
                 a=None):
        self.nr = nr
        self.a = a

    def get(self) -> int:
        return self.nr

    def text(self) -> str:
        return self.a


class QA(object):

    def __init__(self,
                 questions: List[Question],
                 answer: Answer):
        self.qs = questions
        self.ans = answer

    def questions(self):
        return self.qs

    def answer(self):
        return self.ans
