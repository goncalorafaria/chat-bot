from core.query import Query, ResultSet
from core.qa import QA


class Corpus(object):

    def __init__(self):
        self.qa_corpus = []

    def query(self, q: Query) -> ResultSet:

        rs = ResultSet(q)

        for qa in self.qa_corpus:
            rs.consider(qa)

        return rs.sort()


    def add(self, qa : QA):

        self.qa_corpus.append(qa)

    def queryGroup(self, q: Query) -> ResultSet:

        rs = ResultSet(q)

        for qa in self.qa_corpus:
            rs.considerGroup(qa)

        return rs