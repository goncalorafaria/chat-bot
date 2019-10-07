from runtime.query import Query, ResultSet


class Corpus(object):

    def __init__(self):
        raise NotImplementedError('Not implemented')

    def query(self, q: Query) -> ResultSet:
        raise NotImplementedError('Not implemented')

    def load(self, filename : str):
        raise NotImplementedError('Not implemented')
