import nltk
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

with open('questions.txt') as f:
    lines = f.readlines()


text = "".join(lines)
text = text.lower()

regex = re.compile('[^a-zA-ZçÇãâáàêéíìõôóòú-]')

text = regex.sub(' ',text)
text = re.sub(r'\s\s+',' ',text)

pf = open('processed_questions1.txt','w')
pf.write(str(text))
pf.close()

'''
wordcloud = WordCloud(font_path = r'Montserrat-Black.otf',                            
                            background_color = 'white',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func
                            ).generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
'''
    


