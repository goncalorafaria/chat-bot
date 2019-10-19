from core.qa import Question
from abc import ABC, abstractmethod
import numpy as np

class Metric(ABC):

    def measure(self,
                question1: Question,
                question2: Question) -> float:
        pass
    
    
class Jaccard(Metric):
    
    def measure(self,
                question1: Question,
                question2: Question) -> float:
        
        Q1andQ2, Q1orQ2 = andOrCount(question1,question2)
        
        return Q1andQ2/Q1orQ2
    

class Dice(Metric):
    
    def measure(self,
                question1: Question,
                question2: Question) -> float:
        
        Q1andQ2, Q1orQ2 = andOrCount(question1,question2)
        
        return (2*Q1andQ2)/(Q1andQ2+Q1orQ2)
        

class MED(Metric):
    
    def measure(self,
                question1: Question,
                question2: Question) -> float:
    
        wordList1 = question1.textList
        wordList2 = question2.textList
            
        Q1Len = len(wordList1)
        Q2Len = len(wordList2)
        
        if Q1Len == 0:
            return Q2Len
        if Q2Len == 0:
            return Q1Len
        
        shape = (Q1Len+1,Q2Len+1)
        
        medMatrix = np.array(shape)
        
        medMatrix[:,0] = np.arange(shape[0])
        medMatrix[0,:] = np.arange(shape[1])
        
        for i in range(1,shape[0]):
            for j in range(1,shape[1]):
                if wordList1[i-1].Equals(wordList2[j-1]):
                    medMatrix[i,j] = medMatrix[i-1,j-1]
                else:
                    medMatrix[i,j] = min(medMatrix[i-1,j],medMatrix[i-1,j-1],medMatrix[i,j-1]) + 1
        
        return medMatrix[Q1Len,Q2Len]

q1 = Question("quanto custa isso?")
q2 = Question("quanto é aquilo?")

jaccard = Jaccard.measure(q1,q2)
dice = Dice.measure(q1,q2)
med = MED.measure(q1,q2)

print('Question 1: ', q1.text)   
print('Question 2: ', q2.text)
print('Jaccard Distance: ', jaccard)
print('Dice Distance: ', dice)
print('MED Distance: ', med)

def andOrCount(self,
                question1: Question,
                question2: Question) -> tuple:
    Q1andQ2 = 0 #contador and
        
    wordList1 = question1.textList
    wordList2 = question2.textList
    
    Q1Len = len(wordList1)
    Q2Len = len(wordList2)

    
    for word in wordList1:
        if word in wordList2:
            Q1andQ2 +=1
    
    Q1orQ2 = Q1Len + Q2Len - Q1andQ2
    
    return (Q1andQ2,Q1orQ2)