import nltk
import xml.etree.ElementTree as ET
import string
import pickle
import sklearn
import scipy
from sklearn.decomposition import PCA


# Get questions from XML
def processKnowledgeBase(filename):

    with open("data/test_questions.pickle", "rb") as f:
        test_group = set(pickle.load(f))

    tree = ET.parse(filename)
    root = tree.getroot()
    questions = {}
    dev=[]
    for documento in root.findall('documento'):
        faq_list = documento.find('faq_list')
        for faq in faq_list.findall('faq'):
            perguntas = faq.find('perguntas')
            for pergunta in perguntas.iter('pergunta'):

                if pergunta.text is not "":
                    if pergunta.text not in test_group:
                        if faq.find('resposta').attrib['id'] in questions:
                            questions[faq.find('resposta').attrib['id']].append(pergunta.text)
                        else:
                            questions[faq.find('resposta').attrib['id']] = [pergunta.text]
                    else:
                        dev.append( (faq.find('resposta').attrib['id'], pergunta.text) )

    return questions, dev

def get_fromfile(fname):
    with open(fname, 'r') as file:
        stopwords = [line.split('\n')[0] for line in file.readlines()]
    return stopwords

stopwords_list = {
    'nltk': nltk.corpus.stopwords.words('portuguese'),
    'minimal': get_fromfile("data/stops.txt")
}



# Preprocessing functions


def removePunctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def removeNumbers(text):
    return text.translate(str.maketrans('', '', string.digits))


def lowerCase(text):
    return text.lower()


def tokenize(text):
    return nltk.tokenize.word_tokenize(text)


def stem(tokens):
    #if not is_tokenized:
    #    doc = tokenize(doc)
    stemmer = nltk.stem.RSLPStemmer()
    return [stemmer.stem(token) for token in tokens]


def removeStopwords(tokens, stopwords):
    #if not is_tokenized:
    #    doc = tokenize(doc)
    #stemmer = nltk.stem.RSLPStemmer()
    return [token for token in tokens if not token in stopwords]


class RemoveStopWords():

    def __init__(self,
                    stopwords):
        self.stopwords = stopwords

    def __call__(self, tokens):
        return [token for token in tokens if not token in self.stopwords]


class TFidf:
    def __init__(self,
                 train_question, lowercase, stopwords):
        self.vectorizer = sklearn.\
            feature_extraction.\
            text.\
            TfidfVectorizer(analyzer='word',
                            lowercase=lowercase,
                            stop_words=stopwords,
                            smooth_idf=True,
                            sublinear_tf=True,
                            max_features=5000)
        flat = []
        for qs in train_question.values():
            for quest in qs:
                flat.append(quest)
        X = self.vectorizer.fit_transform(flat)

        self.pca = PCA(n_components=600)
        self.pca.fit(X.toarray())

    def __call__(self, string):
        v = self.vectorizer.transform([" ".join(string)])
        return self.pca.transform(v.toarray())[0]
        #return v.toarray()[0]