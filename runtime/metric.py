from core.qa import Question
import nltk
from nltk.metrics import masi_distance


class Metric(object):

    def __init__(self,
                 format : str,
                 calculate,
                 name=""):
        self.format = format
        self.calculate = calculate
        self.name = name

        #print("metric format: " + self.format)

    def measure(self,
                question1: Question,
                question2: Question) -> float:

        tk1 = question1.get_format(self.format)
        tk2 = question2.get_format(self.format)

        return self.calculate(tk1,tk2)


def jaccart(tk1,tk2):
    return nltk.jaccard_distance(set(tk1),set(tk2))


def masi(tk1,tk2):
    return masi_distance(set(tk1),set(tk2))


# string jaro_similarity
# jaro_winkler_similarity