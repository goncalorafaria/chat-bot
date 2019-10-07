from core.qa import QA


class Metric(object):

    def __init__(self):
        raise NotImplementedError('Not implemented')

    def measure(self,
                question1: QA.Question,
                question2: QA.Question) -> float:
        raise NotImplementedError('Not implemented')