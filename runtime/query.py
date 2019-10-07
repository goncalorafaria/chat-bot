from runtime.metric import Metric
from core.qa import Question

from typing import List


class Query(object):

    def __init__(self,
                 question: Question,
                 metrics: List[Metric],
                 n: int):
        self.question = question
        self.metrics = metrics
        self.n = n


class ResultSet(Query):

    def __init__(self,
                 query: Query):

        super(ResultSet, self).__init__(
            query.question,
            query.metrics,
            query.n)

    def consider(self, question : Question) -> bool:
        raise NotImplementedError('Not implemented')