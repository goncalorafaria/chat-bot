import nltk
import xml.etree.ElementTree as ET
import string
import pickle

from numpy import random



# Get questions from XML
def processKnowledgeBase(filename, validate = True):
    random.seed(97031)

    tree = ET.parse(filename)
    root = tree.getroot()
    questions = {}

    for documento in root.findall('documento'):
        faq_list = documento.find('faq_list')
        for faq in faq_list.findall('faq'):
            perguntas = faq.find('perguntas')
            for pergunta in perguntas.iter('pergunta'):

                stripedq = pergunta.text.strip()

                if not (len(stripedq) == 0):

                    # print(stripedq)
                    # print(stripedq + "###")
                    # 535
                    repetidos = {'275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286',
                                 '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298',
                                 '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310',
                                 '311', '312', '313', '314', '315', '448', '449', '450', '451', '452', '453', '454',
                                 '455', '456', '457', '458', '467', '468', '469', '470', '471', '472', '473', '474',
                                 '519', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '530',
                                 '531', '532', '609', '610'}

                    dup = { "122":27, "189": 201 }

                    if faq.find('resposta').attrib['id'] not in repetidos:

                        #ansfilt[faq.find('resposta').attrib['id']] = faq.find('resposta').text.strip()

                        if faq.find('resposta').attrib['id'] in dup.keys():
                            key = dup[faq.find('resposta').attrib['id']]
                        else:
                            key = faq.find('resposta').attrib['id']


                        if key in questions:
                            questions[key][0].append(stripedq)
                        else:
                            questions[key] = ([stripedq], faq.find('resposta').text.strip())


    #for i in ansfilt.keys():
    #    for j in ansfilt.keys():

    #        if i != j :
    #            if ansfilt[i] == ansfilt[j] :
    #                print( i + " - " + j)

    if validate :
        train = {}
        dev = {}

        for ans, qs in questions.items():
            qs = qs[0]
            if len(qs) > 1 :
                dev[ans] = qs[0]
                train[ans] = qs[1:]

        return train, dev
    else:
        return questions

def get_fromfile(fname):
    with open(fname, 'r') as file:
        stopwords = [line.split('\n')[0] for line in file.readlines()]
    return stopwords

stopwords_list = {
    'nltk': nltk.corpus.stopwords.words('portuguese'),
    'minimal': get_fromfile("./data/stops.txt")
}

#["a", "que", "de", "por", "para", "à", "é", "e", "com", "da", "do",
# "o", "ou", "em", "um", "uma"]  # get_fromfile("data/stops.txt")

# Preprocessing functions

def removePunctuation(text):
    #print(text)
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
