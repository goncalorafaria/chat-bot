from typing import List
from runtime.config import Config
from process.prep import process_chain


class Question(object):
    def __init__(self,
                 qtext : str,
                 configurations,
                 coded=False):

        if coded:
            coded_configurations = configurations
        else:
            coded_configurations = [Config.code_config(c) for c in configurations]

        self.format = {}
        self.text = qtext

        for cc in coded_configurations:
            self.format[cc] = process_chain(self.text, coded_configurations)

    def get_format(self, name : str):
        return self.format[name]

    def set_format(self, name: str, prep_format):
        self.format[name] = prep_format


class Answer(object):
    def __init__(self,
                 nr: int):
        self.nr = nr

    def get(self) -> int:
        return self.nr


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
