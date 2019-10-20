from runtime.query import Query, ResultSet
from core.qa import QA


class Corpus(object):

    def __init__(self):
        self.qa_corpus = []

    def query(self, q: Query) -> ResultSet:

        rs = ResultSet(q)

        for qa in self.qa_corpus:
            rs.consider(qa)

        return rs.sort()

    def crossed_inspection(self, q : Query) -> [ResultSet]:

        hyper_rs = []

        for qa in self.qa_corpus:
            for question in qa.questions():
                q.question = question
                hyper_rs.append(
                    self.query( q )
                )

        return hyper_rs


    def add(self, qa : QA):
        self.qa_corpus.append(qa)
