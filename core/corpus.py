from runtime.query import Query, ResultSet
from core.qa import QA
import pickle


class Corpus(object):

    def __init__(self):
        self.qa_corpus = []

    def query(self, q: Query) -> ResultSet:

        rs = ResultSet(q)

        for qa in self.qa_corpus:
            rs.consider(qa)

        return rs

    @staticmethod
    def load(filename : str):
        with open(filename + '.pkl', 'rb') as f:
            return pickle.load(f)

    def save(self, filename:str):
        with open(filename + '.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def add(self, qa : QA):
        self.qa_corpus.append(qa)
