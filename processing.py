import os
#os.chdir(r"C:\\Users\\cam\\Documents\\MECD-1\\Lingua_Natural\\MP1\\chat-bot") 
#os.getcwd()
import numpy as np
import nltk
import xml.etree.ElementTree as ET
from ..core.qa import Question
import string
    

# Get questions from XML
tree = ET.parse('KB.xml')
root = tree.getroot()
questions = {}
for documento in root.findall('documento'):
    faq_list = documento.find('faq_list')
    for faq in faq_list.findall('faq'):
        perguntas = faq.find('perguntas')
        for pergunta in perguntas.iter('pergunta'):
            questions[faq.find('resposta').attrib['id']] =Question(pergunta.text)

minimal = ['a','o','um','uns','aos','os','as','num','numa','que','de','para','quê','e','em']


stopwords_list = {
    'nltk':nltk.corpus.stopwords.words('portuguese'),
    'minimal':minimal
}

# Preprocessing functions 

def removePunctuation(doc):
    return {k: v.text.translate(str.maketrans('','',string.punctuation)) for k, v in doc.items()}

def removeNumbers(doc):
    return {k: v.text.translate(str.maketrans('','',string.digits)) for k, v in doc.items()}

def lowerCase(doc):
    return {k: v.text.lower() for k, v in doc.items()}

def tokenize(doc):
    return {k: nltk.tokenize.word_tokenize(v.text) for k, v in doc.items()}

def stem(doc,is_tokenized):
    if not is_tokenized:
        doc = tokenize(doc)
    stemmer = nltk.stem.RSLPStemmer()
    return {k: [stemmer.stem(token) for token in v] for k, v in doc.items()}