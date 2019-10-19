from typing import List
import re 
import nltk
import mmap

class Question(object):
    _filePath = '../files/stopwords.txt'
    
    def __init__(self, textform: str):
        self.text = textform
        self.text = self.text.lower()
        self.textList = [] #this is what should be used by other classes
        self.wordFreq = {}
        
        self._preProcess()
        
        
    def _preProcess(self):
        #remove non word characters and multiple spaces
        self.textList = re.sub("[^\w]", " ",  self.text).split()
        '''
        for i in range(len(self.textList)):                                                                   
            self.textList[i] = re.sub(r'[^\w]',' ', self.textList[i])
            self.textList[i] = re.sub(r'[\s+]',' ', self.textList[i])   
        '''
        #remove stop words
        with open(self._filePath) as stopwords:
            finder = mmap.mmap(stopwords.fileno(), 0, access=mmap.ACCESS_READ)
            for word in self.textList:
                if finder.find(word.encode()) != -1:
                    self.textList.remove(word)
        
        #get frequency of each word            
        tokens = nltk.word_tokenize(self.text)
        for token in tokens:
            if token not in self.wordFreq.keys():
                self.wordFreq[token] = 1
            else:
                self.wordFreq[token] += 1
        
    
    def to_string(self):
        string = ''
        nWords = len(self.textList)
        for i, word in enumerate(self.textList):      
            string+=word
            if(i!=nWords-1):
                string+=' '
        print(string)


class Answer(object):
    def __init__(self,
                 textform: str):
        self.text = textform

    def get(self) -> str:
        return self.text


class QA(object):

    def __init__(self,
                 questions: List[Question],
                 answer: Answer):

        self.questions = questions
        self.answer = answer
