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
"""

import numpy as np
from scipy import spatial
#@nltk600
#braycurtis - 0.7012820512820512 |
#canberra   - 0.6551282051282051 |
#chebyshev  - 0.4435             |
#cityblock  - 0.6615384615384615 |
#euclidean  - 0.6666666666666666 |
#cosine     - 0.6948717948717948 |

#@gustavo600
#braycurtis - 0.6923076923076923 |
#canberra   -  0.6282051282051282 |
#chebyshev  -              |
#cityblock  - |
#euclidean  -  |
#cosine     -  0.6935897435897436 |

# jaccard - 0.7141025641025641
def cos(tk1,tk2):
    result = spatial.distance.cosine(tk1,tk2)
    return result


cfg = Config(filename ="data/KB.xml",
             metric_functions=[
                 cos],
             metric_functions_names=[
                 "cossine"
             ],
             configurations=[
                {"lowercase":True,
                 "pontuation":True,
                 "stopw_minimal":True,
                 "stem":True,
                 "tokenize":True,
                 "numbers":True,
                 "tfidf": True}]
             )

"""
cfg = Config(filename ="data/KB.xml",
             metric_functions=[
                 jaccart],
             metric_functions_names=[
                 "jaccard"
             ],
             configurations=[
                {"lowercase":True, "pontuation":True, "tokenize":True, "stem":True,"stopw_nltk ":True, "numbers":True }]
             )
"""
print("start eval")

from sklearn.metrics import accuracy_score

pred, labels = cfg.evalute()

for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" f1 score : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)






"""
from process import prep

q, dev = prep.processKnowledgeBase("data/KB.xml")

flat = []
for qs in q.values():
    for quest in qs:
        flat.append(quest)

tfidf = prep.TFidf(flat)


a = tfidf(["Como obter o identificador, ao aceder ao portal ?"])

print(len(a))

"""



