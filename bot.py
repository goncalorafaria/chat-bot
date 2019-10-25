import pickle

import nltk
from scipy import spatial
from sklearn.metrics import accuracy_score

from runtime.config import Config
from core.metric import dice, jaccart


"""

cfg2 = Config(filename ="data/KB.xml",
             metric_functions=[
                 jaccart],
             metric_functions_names=[
                 "jaccart"
             ],
             configurations=
                 cc_trad_search
             ,get_mat=False)

pred, labels = cfg2.evaluate()

accuracy = []
for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
    accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("acc_array.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

print("eval ended")

"""

"""
cfg3 = Config(filename ="data/KB.xml",
             metric_functions=[
                 spatial.distance.cosine,
                 spatial.distance.euclidean],
             metric_functions_names=[
                 "cosine",
                 "euclidean"
             ],
             configurations=
                 cc_search,
             get_mat=True
             )

pred, labels = cfg3.evaluateGroup()

accuracy = []
for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
    accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("group_acc_array_tdidf.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

#####
#####
"""

cc_trad_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                for b5 in [True, False]:
                    for b6 in [True, False]:
                        cc_trad_search.append({"pontuation": True,
                     "numbers": True,
                     "lowercase": True,
                     "tokenize": True,
                     "stem": b4,
                     "stopw_minimal": b5,
                     "stopw_nltk":False,
                     "tfidf":False})

cfg = Config(filename ="data/KB.xml",
             configurations=
                 cc_trad_search
             )

print("start")
pred, labels = cfg.searchGroup(metric_functions=[
                 jaccart,
                 dice,
                 nltk.edit_distance],
             metric_functions_names=[
                 "jaccart",
                 "dice",
                 "edit_distance"
             ])

accuracy = []
for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
    accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("group_acc_array_set.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

print("eval ended")



"""
cc_idf_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            cc_idf_search.append({"pontuation": True,
                "numbers": True,
                "acents": True,
                "lowercase":True,
                "tokenize": True,
                "stem": b1,
                "stopw_minimal": b2,
                "stopw_nltk": b3,
                "tfidf":True})

print("start")

print(cc_idf_search)


cfg1 = Config(filename ="data/KB.xml",
             configurations=
                 [],
             delay=True
             )

accuracy = []
for cc in cc_idf_search:

    pred, labels = cfg1.idfsearchGroup(
            metric_functions=[
                 spatial.distance.cosine,
                 spatial.distance.euclidean],
            metric_functions_names=[
                 "cosine",
                 "euclidean"
            ],
            idfconfig=cc)
    for km in pred.keys():

        obj = accuracy_score(labels, pred[km], normalize=True)

        print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
        accuracy.append([str(cc), km.name, obj])

filehandler = open("acc_array_tdidf.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

"""
