from .runtime.metric import Metric
from .core.qa import Question, Answer, QA
from .runtime.query import Query
from .core.corpus import Corpus

import nltk


q = Question({})
ans = Answer(1)

q.set_format("bag", {"Como", "obter", "id", "?"})

q.set_format("bag_stem_lowercase", {"com", "obt", "id" })

qa = QA([q], ans)
kb = Corpus()

kb.add(qa)

edit_distsance_metric = Metric("bag", nltk.edit_distance)

jaccard_metric = Metric("bag_stem_lowercase", nltk.jaccard_distance)

qy = Query(q, [jaccard_metric, edit_distsance_metric])

rs = kb.query( qy )

