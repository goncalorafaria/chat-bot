from core.metric import Metric

from typing import List


class QA(object):

    class Question(object):
        def __init__(self,
                     textform: str):
            raise NotImplementedError('Not implemented')

        def distances(self,
                      questions: QA.Question,
                      metric: List[Metric]) -> List[float]:
            raise NotImplementedError('Not implemented')

        def distance(self,
                     question: QA.Question,
                     metric: Metric) -> float:
            return self.distances(question,[metric])[0]

    class Answer(object):
        def __init__(self,
                     textform: str):
            self.text = textform

        def get(self) -> str:
            return self.text

    def __init__(self,
                 questions: List[Question],
                 answer: Answer):
        raise NotImplementedError('Not implemented')
