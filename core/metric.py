from core.qa import Question


class Metric(object):

    def __init__(self):
        raise NotImplementedError('Not implemented')

    def measure(self,
                question1: Question,
                question2: Question) -> float:
        raise NotImplementedError('Not implemented')