from core.qa import Question


class Metric(object):

    def __init__(self,
                 format : str,
                 calculate):
        self.format = format
        self.calculate = calculate

    def measure(self,
                question1: Question,
                question2: Question) -> float:

        tk1 = question1.get_format(self.format)
        tk2 = question2.get_format(self.format)

        return self.calculate(tk1,tk2)
