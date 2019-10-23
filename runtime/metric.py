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

    stki1 = set(tk1)
    stki2 = set(tk2)

    l_inters = len( stki1.intersection(stki2) )
    l_unions = len( stki1.union(stki2) )


    if (l_unions == 0):
        return 1
    else:
        return l_inters / l_unions

def dice(tk1,tk2):

    stki1 = set(tk1)
    stki2 = set(tk2)

    l_inters = len( stki1.intersection(stki2) )
    l_1 = len(stki1 )
    l_2 = len(stki2)

    if (l_1 == 0 or l_2 == 0):
        return 1
    else:
        return 1 - 2 * l_inters / (l_1 * l_2)


#def masi(tk1,tk2):

#    return masi_distance(set(tk1),set(tk2))


# string jaro_similarity
# jaro_winkler_similarity