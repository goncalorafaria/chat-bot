import nltk
import xml.etree.ElementTree as ET
from runtime.config import Config
import string


# Get questions from XML
def processKnowledgeBase(filename):

    tree = ET.parse('../data/KB.xml')
    root = tree.getroot()
    questions = {}
    for documento in root.findall('documento'):
        faq_list = documento.find('faq_list')
        for faq in faq_list.findall('faq'):
            perguntas = faq.find('perguntas')
            for pergunta in perguntas.iter('pergunta'):

                if faq.find('resposta').attrib['id'] in questions:
                    questions[faq.find('resposta').attrib['id']].append(pergunta.text)
                else:
                    questions[faq.find('resposta').attrib['id']] = [pergunta.text]

    return questions


def process_chain( text , coded_config ):

    stream = text
    for i in range(len(coded_config)):
        if int(coded_config[i]) == 1 :
            stream = Config.preprocessing_method_functions[
                Config.preprocessing_methods[i]
            ](stream)

    return stream

stopwords_list = {
    'nltk': nltk.corpus.stopwords.words('portuguese'),
    'minimal': ['a', 'o', 'um', 'uns', 'aos', 'os', 'as', 'num', 'numa', 'que', 'de', 'para', 'quê', 'e', 'em']
}


# Preprocessing functions


def removePunctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def removeNumbers(text):
    return text.translate(str.maketrans('', '', string.digits))


def lowerCase(text):
    return text.lower()


def tokenize(doc):
    return {k: nltk.tokenize.word_tokenize(v.text) for k, v in doc.items()}


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
