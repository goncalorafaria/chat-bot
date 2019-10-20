from runtime.config import Config

import nltk


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

from runtime.metric import jaccart

cfg = Config(filename ="data/KB.xml",
             metric_functions=[
                 nltk.edit_distance,
                 jaccart],
             metric_functions_names=[
                 "nltk.edit_distance",
                 "jaccart"
             ],
             configurations=[{"pontuation":True,
                              "numbers":True,
                              "lowercase":True,
                              "tokenize":True,
                              "stem":True,
                              "stopw_minimal":True},
                             {"numbers": True,
                              "lowercase": True,
                              "tokenize": True,
                              "stem": True,
                              "stopw_minimal": True},
                             {"pontuation":True,
                              "numbers":True,
                              "lowercase":True,
                              "tokenize":True,
                              "stem":True,
                              "stopw_nltk":True},
                             {"numbers": True,
                              "lowercase": True,
                              "tokenize": True,
                              "stem": True,
                              "stopw_nltk": True}
                             ]
             )

print("start eval")

from sklearn.metrics import f1_score

pred, labels = cfg.evalute("data/test_question.pickle")

for km in pred.keys():
    obj = f1_score(labels, pred[km],average="micro")
    print(km.format)
    print(" f1 score : " + str(obj) + " : " + str(km.format) + " : name: " + km.name)







