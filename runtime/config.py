from core.corpus import Corpus
from core.query import Query
from process import prep
from core.qa import Question, Answer, QA
from core.metric import Metric
import unidecode
import sklearn
from process.prep import processKnowledgeBase as extract


def process_chain(text ,coded_config ):

    stream = text
    for i in range(len(coded_config)):
        if int(coded_config[i]) == 1:
            stream = Config.preprocessing_method_functions[
                Config.preprocessing_methods[i]
            ](stream)

    return stream


class TFidf:
    def __init__(self,
                 train_question, idformat, runtime=False):
        self.vectorizer = sklearn.\
            feature_extraction.\
            text.\
            TfidfVectorizer(analyzer='word',
                            smooth_idf=True,
                            sublinear_tf=True,
                            max_features=5000)
        flat = []
        tmp = list(idformat)
        tmp[-1] = "0"

        idformat= "".join(tmp)
        #print(train_question)
        for qs in train_question.values():
            if runtime:
                for quest in qs[0]:
                    flat.append(" ".join(process_chain(quest, idformat)))
            else:
                for quest in qs:
                    #print(quest)
                    flat.append(" ".join(process_chain(quest, idformat)))

        self.vectorizer.fit(flat)

        #self.pca = PCA(n_components=82 0)
        #self.pca.fit(X.toarray())

    def __call__(self, string):
        v = self.vectorizer.transform([" ".join(string)])
        #return self.pca.transform(v.toarray())[0]
        return v.toarray()[0]

class Config(object):

    preprocessing_methods = [
        "pontuation",
        "acents",
        "numbers",
        "lowercase",
        "tokenize",
        "stopw_nltk",
        "stopw_minimal",
        "stem",
        "tfidf",

    ]

    preprocessing_method_functions = {
        "pontuation": prep.removePunctuation,
        "acents":unidecode.unidecode,
        "numbers": prep.removeNumbers,
        "lowercase": prep.lowerCase,
        "tokenize": prep.tokenize,
        "stem": prep.stem,
        "stopw_nltk": prep.RemoveStopWords(
            prep.stopwords_list["nltk"]),
        "stopw_minimal": prep.RemoveStopWords(
            prep.stopwords_list["minimal"]),
        "tfidf" : None
    }

    def __init__(self,
                 filename,
                 configurations, delay= False):

        self.corpus = Corpus()

        self.coded_configurations = [Config.code_config(c) for c in configurations]
        ## pode ser feito em paralelo
        train, dev = prep.processKnowledgeBase(filename, validate=True)


        self.dev = dev

        self.train = train

        if not delay:
            for k, qs in self.train.items():
                qs_q = []

                for qtext in qs:

                    qformat = {}

                    for cc in self.coded_configurations:
                        qformat[cc] = process_chain(qtext, cc)

                    qs_q.append(
                        (qtext, qformat)
                    )

                self.corpus.add(
                    QA(
                        [Question(
                            qtext,
                            qformat
                        ) for qtext, qformat in qs_q]
                        , Answer(k)))

    def search(self,
               metric_functions,
               metric_functions_names):

        return self._search(
                metric_functions,
                metric_functions_names,
                self.corpus.query)

    def searchGroup(self,
               metric_functions,
               metric_functions_names):

        return self._search(
            metric_functions,
            metric_functions_names,
            self.corpus.queryGroup)

    def _search(self,
                metric_functions,
                metric_functions_names,
                query_func):

        metrics = []
        i = 0
        for mf in metric_functions:
            for cc in self.coded_configurations:
                metrics.append(Metric(cc, mf, name=metric_functions_names[i]))
            i += 1


        return self._evaluate(query_func,metrics)

    #Config.preprocessing_method_functions["tfidf"] = prep.TFidf(
        #self.train,
        #idfqformat)

    def idfsearch(self,
                   idfconfig,
                   metric_functions,
                   metric_functions_names):

        self.corpus = Corpus()

        idfformat = Config.code_config(idfconfig)

        Config.preprocessing_method_functions["tfidf"] = TFidf(
            self.train,
            idfformat)

        for k, qs in self.train.items():

            qs_q = []
            #print(qs)
            for qtext in qs:

                qformat = {}

                qformat[idfformat] = process_chain(qtext, idfformat)

                qs_q.append(
                    (qtext, qformat)
                )

            self.corpus.add(
                QA(
                    [Question(
                        qtext,
                        qformat
                    ) for qtext, qformat in qs_q]
                    , Answer(k)))


        metrics = []
        i = 0
        for mf in metric_functions:
            metrics.append(Metric(idfformat, mf, name=metric_functions_names[i]))
            i += 1

        return self._evaluate(self.corpus.query, metrics)

    def idfsearchGroup(self,
                   idfconfig,
                   metric_functions,
                   metric_functions_names):

        self.corpus = Corpus()

        idfformat = Config.code_config(idfconfig)

        Config.preprocessing_method_functions["tfidf"] = TFidf(
            self.train,
            idfformat)

        for k, qs in self.train.items():

            qs_q = []
            # print(qs)
            for qtext in qs:
                qformat = {}

                qformat[idfformat] = process_chain(qtext, idfformat)

                qs_q.append(
                    (qtext, qformat)
                )

            self.corpus.add(
                QA(
                    [Question(
                        qtext,
                        qformat
                    ) for qtext, qformat in qs_q]
                    , Answer(k)))

        metrics = []
        i = 0
        for mf in metric_functions:
            metrics.append(Metric(idfformat, mf, name=metric_functions_names[i]))
            i += 1

        return self._evaluate(self.corpus.queryGroup, metrics)

    def evaluate(self,metrics, decide=None):
        return self._evaluate(self.corpus.query,metrics)

    def evaluateGroup(self,metrics):
        return self._evaluate(self.corpus.queryGroup,metrics)

    def _evaluate(self, query_func, metrics, decide = None):

        queries = []
        for ans_nr, qtext in self.dev.items():
            qformat = {}

            for m in metrics:

                qformat[m.format] = process_chain(qtext, m.format)

            queries.append( (
                Query(question=
                      Question(qtext,qformat),
                  metrics=metrics,
                  n=1),ans_nr ) )

        answ = []

        mscores= {}
        s = {}
        for m in metrics:
            mscores[m] = []
            s[m]=0

        c=0

        #print(len(queries))
        #print(len(self.corpus.qa_corpus))

        b = True
        for qq, ans in queries:
            rs = query_func(qq)

            #print(rs.rankings)

            if b:
                max = {}
                min = {}
                for m, hp in rs.rankings:
                    max[m] = 0
                    min[m] = 1
                b = False

            for m, hp in rs.rankings:
                mscores[m].append(hp[0].qa.ans.nr)


                if hp[0].qa.ans.nr == ans:
                    if hp[0].score <= 1:
                        s[m] += 1
                    #print(hp[0].score)
                    max[m] = max[m] if hp[0].score < max[m] else hp[0].score
                else:
                    min[m] = min[m] if hp[0].score > min[m] else hp[0].score
                #print("############")
                #print(hp[0].score)
                #print("query:" + qq.question.text)
                #print("processed" + str(qq.question.format[m.format]))
                #print("obtained: " + hp[0].q.text)
                #print("processed" + str(hp[0].q.format[m.format]))
                
            answ.append(
                ans
            )


        #for m in max.keys():
        #    print("max: " + str(max[m]) + " " + m.name)
        #    print("min: " + str(min[m]) + " " + m.name)
        #    print(s[m]/len(queries))
        return mscores, answ


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

    @staticmethod
    def loadCorpus(filename: str, configuration):

        corpus = Corpus()

        kb = extract(filename, validate=False)

        Config.preprocessing_method_functions["tfidf"] = TFidf(
            kb,
            configuration,
            runtime=True)

        for k, qa in kb.items():

            qs = qa[0]
            a = qa[1]

            questions = []

            for qtext in qs:
                qformat = {configuration: process_chain(qtext, configuration)}

                questions.append(
                    Question(qtext, qformat)
                )

            corpus.add(
                QA(questions
                   , Answer(k, a)))

        return corpus

