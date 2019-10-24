from runtime.config import Config

import nltk
from runtime.metric import dice, jaccart
from sklearn.metrics import accuracy_score
from scipy import spatial
import numpy as np
import pickle
"""
cc_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                for b5 in [True, False]:
                    cc_search.append({"pontuation": True,
                     "numbers": b1,
                     "lowercase": b2,
                     "tokenize": True,
                     "stem": b3,
                     "stopw_minimal": b4,
                     "stopw_nltk":b5,
                     "tfidf":True})


cc_trad_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                for b5 in [True, False]:
                    cc_trad_search.append({"pontuation": True,
                     "numbers": b1,
                     "lowercase": b2,
                     "tokenize": True,
                     "stem": b3,
                     "stopw_minimal": b4,
                     "stopw_nltk":b5,
                     "tfidf":False})


cfg1 = Config(filename ="data/KB.xml",
             metric_functions=[
                 spatial.distance.cosine,
                 spatial.distance.euclidean],
             metric_functions_names=[
                 "cosine",
                 "euclidean"
             ],
             configurations=
                 cc_search
             )

pred, labels = cfg1.evaluate()

accuracy = []
for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
    accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("acc_array_tdidf.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

#####
#####

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

cfg4 = Config(filename ="data/KB.xml",
             metric_functions=[
                 jaccart,
                 dice,
                 nltk.edit_distance],
             metric_functions_names=[
                 "jaccart",
                 "dice",
                 "edit_distance"
             ],
             configurations=
                 cc_trad_search,
             get_mat=False
             )

pred, labels = cfg4.evaluateGroup()

accuracy = []
for km in pred.keys():
    obj = accuracy_score(labels, pred[km],normalize=True)
    print(km.format)
    print(" acc : " + str(obj) + " : " + str(Config.decode_config(km.format)) + " : name: " + km.name)
    accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("group_acc_array.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()

print("eval ended")

"""

cc_idf_search = []

for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                for b5 in [True, False]:
                    for b6 in [True, False]:
                        for b7 in [True, False]:
                            cc_idf_search.append({"pontuation": b1,
                     "numbers": b2,
                     "acents": b3,
                     "lowercase": b4,
                     "tokenize": True,
                     "stem": b5,
                     "stopw_minimal": b6,
                     "stopw_nltk": b7,
                     "tfidf":True})

print("start")
cfg = Config(filename ="data/KB.xml",
             configurations=
                 cc_idf_search,
             delay=True
             )

accuracy = []
for cc in cc_idf_search:

    pred, labels = cfg.idfsearch(
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
        accuracy.append([str(Config.decode_config(km.format)), km.name, obj])

filehandler = open("acc_array_tdidf.obj","wb")
pickle.dump(accuracy,filehandler)
filehandler.close()
