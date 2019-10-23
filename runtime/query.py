from runtime.metric import Metric
from core.qa import QA, Question
import heapq

from typing import List


class Query(object):

    def __init__(self,
                 question,
                 metrics: List[Metric],
                 n=1):
        self.question = question
        self.metrics = metrics
        self.n = n


class ResultSet(Query):
    class Node:
        def __init__(self,
                     q,
                     score: float,
                     qa: QA):
            self.q = q
            self.score = score
            self.qa = qa

        def __lt__(self, other):
            return self.score < other.score

        def __eq__(self, other):
            return self.score == other.score

        def get_score(self):
            return self.score

        def get_qa(self):
            return self.qa

        def get_question(self):
            return self.q

    def __init__(self,
                 query: Query):

        super(ResultSet, self).__init__(
            query.question,
            query.metrics,
            query.n)

        self.rankings = [(mt, []) for mt in self.metrics]

    def sort(self):
        self.rankings.sort(key=lambda x:  x[1][0] if len(x[1]) > 0 else 100000)

        return self

    def consider(self, qa : QA) -> int:

        r = 0

        for candidate in qa.questions(): ## for every question in qa

            for mt, heap_sc in self.rankings :
                value = mt.measure(candidate, self.question)

                if len(heap_sc) < self.n:
                    heapq.heappush(heap_sc, self.Node(candidate,value, qa))
                    r += 1
                else:
                    if value < heap_sc[0].score:
                        heapq.heappop(heap_sc)
                        heapq.heappush(heap_sc, self.Node(candidate, value, qa))
                        r += 1

        return r

    def considerGroup(self, qa: QA) -> int:

        r = 0

        for mt, heap_sc in self.rankings:
            coe = 1 / len(qa.questions())
            value = 0
            for candidate in qa.questions():  ## for every question in qa
                value += coe * mt.measure(candidate, self.question)

            if len(heap_sc) < self.n:
                heapq.heappush(heap_sc, self.Node(None, value, qa))
                r += 1
            else:
                if value < heap_sc[0].score:
                    heapq.heappop(heap_sc)
                    heapq.heappush(heap_sc, self.Node(None, value, qa))
                    r += 1

            return r
