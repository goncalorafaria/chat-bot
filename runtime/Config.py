from core.corpus import Corpus
from runtime.query import Query
from process import prep
from core.qa import Question, Answer, QA
from runtime.metric import Metric


class Config(object):

    preprocessing_methods = [
        "pontuation",
        "numbers",
        "lowercase",
        "tokenize",
        "stem",
        "stopw_nltk",
        "stopw_minimal"
    ]

    preprocessing_method_functions = {
        "pontuation": prep.removePunctuation,
        "numbers": prep.removeNumbers,
        "lowercase": prep.lowerCase,
        "tokenize": prep.tokenize,
        "stem": prep.stem,
        "stopw_nltk": prep.RemoveStopWords(
            prep.stopwords_list["nltk"]),
        "stopw_minimal": prep.RemoveStopWords(
            prep.stopwords_list["minimal"]),
    }

    def __init__(self,
                 filename,
                 metric_functions,
                 configurations):
        self.corpus = Corpus()

        coded_configurations = [Config.code_config(c) for c in configurations]
        for k,qs in prep.processKnowledgeBase(filename).items():
            self.corpus.add(
                QA(
                    [Question(
                        q, coded_configurations, coded=True
                    ) for q in qs], Answer(k)))

        metrics = []
        for mf in metric_functions:
            for cc in coded_configurations:
                metrics.append( Metric(cc,mf))

        full_rs = self.corpus.query(
            Query(question=None,
                  metrics = metrics,
                  n=1)
        )





    @staticmethod
    def code_config(p_dict):

        code = ""
        for pp in Config.preprocessing_methods:
            if pp in p_dict:
                if p_dict[pp]:
                    code += "1"
                else:
                    code += "0"
            else:
                code += "0"

        return code

    @staticmethod
    def decode_config(code):

        r_dict = {}
        for i in range(len(Config.preprocessing_methods)):
            if int(code[i]) == 1:
                r_dict[Config.preprocessing_methods[i]] = True

        return r_dict


