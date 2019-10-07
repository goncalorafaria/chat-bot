from core.metric import Metric

from typing import List


class Question(object):
    def __init__(self,
                 textform: str):
        raise NotImplementedError('Not implemented')

    def distances(self,
                  question: Question,
                  metrics: List[Metric]) -> List[float]:
        raise NotImplementedError('Not implemented')

    def distance(self,
                 question: Question,
                 metric: Metric) -> float:
        return self.distances(question,[metric])[0]


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
