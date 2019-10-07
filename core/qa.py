from typing import List


class Question(object):
    def __init__(self,
                 textform: str):
        raise NotImplementedError('Not implemented')


class Answer(object):
    def __init__(self,
                 textform: str):
        self.text = textform

    def get(self) -> str:
        return self.text


class QA(object):

    def __init__(self,
                 questions: List[Question],
                 answer: Answer):
        raise NotImplementedError('Not implemented')
