import sys
from runtime.query import Query
from core.qa import Question
from core.metric import Metric
from process.prep import get_fromfile as loadtest
from runtime.config import process_chain, Config
from scipy.spatial.distance import euclidean
from time import time

assert len(sys.argv) > 2 , "Insufficient number of arguments"

print("Analysing the Knowledge Base.")

start_time = time()

kb_filename = sys.argv[1]
output_filename = "resultados.txt"
test_filename = sys.argv[2]

config = Config.code_config(
                    {"pontuation": True,
                     "numbers": True,
                     "acents": True,
                     "lowercase": True,
                     "tokenize": True,
                     "stem": True,
                     "stopw_minimal": False,
                     "tfidf":True})

corpus = Config.loadCorpus(
    kb_filename,
    config
)

questions = [Question(q ,{config : process_chain(q.strip(), config)})
             for q in loadtest(test_filename)]

measure = Metric(config, euclidean)

queries = [Query(q, [measure]) for q in questions]

results = [corpus.queryGroup(query) for query in queries]

with open(output_filename, "w") as ofile:
    for result in results:

        score = result.top().score
        #print(score)
        if score <= 1.1 :
            answer = result.top().qa.answer().get()
            print(answer, file=ofile)
        else:
            print("0", file=ofile)

print("Elapsed time: " + str(time() - start_time))
print("Terminated answering every query.")