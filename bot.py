from runtime.config import Config

import nltk
from runtime.metric import masi, jaccart


"""
qa = QA([
    Question("Como obter id ?"),
    Question("Como obter o identificador ?"),
    Question("Como obter o número de identificação ?")]
    , Answer(1))

kb = Corpus()

kb.add(qa)

edit_distance_metric = Metric("list", nltk.edit_distance)

jaccard_metric = Metric("bag", nltk.jaccard_distance)

qy = Query(Question("Como obter ident ?"), [edit_distance_metric,jaccard_metric ], n=3)

rs = kb.query(qy)


print("query : Como obter ident ? ")

for m in rs.rankings:
    for rn in m[1]:
        print( "score: " + str(rn.score) + " question : " + str(rn.q.get_format("bag")))

"""


cc_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                for b5 in [True, False]:
                    cc_search.append({"pontuation": b1,
                     "numbers": b2,
                     "lowercase": b3,
                     "tokenize": True,
                     "stem": b3,
                     "stopw_minimal": b4,
                     "stopw_nltk":b5})

cfg = Config(filename ="data/KB.xml",
             metric_functions=[
                 nltk.edit_distance,
                 jaccart,
                 masi],
             metric_functions_names=[
                 "nltk.edit_distance",
                 "jaccart",
                 "masi"
             ],
             configurations=cc_search
             )

print("start eval")

from sklearn.metrics import f1_score

pred, labels = cfg.evalute("data/test_question.pickle")

for km in pred.keys():
    obj = f1_score(labels, pred[km],average="micro")
    print(km.format)
    print(" f1 score : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)







