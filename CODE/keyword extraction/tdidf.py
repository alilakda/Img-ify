import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown
import math
sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
text="Why, they rub an old tin lamp or an iron ring, and then the genies come tearing in, with the thunder and lightning a-ripping around and the smoke a-rolling, and everything they're told to do they up and do it.  They don't think nothing of pulling a shot-tower up by the roots, and belting a Sunday-school superintendent over the head with itóor any other man."


sentences=sent_tokenizer.tokenize(text)
# print (sentences)
words=[]
word_tokenizer = TreebankWordTokenizer()
for s in sentences:
    word_in_sentence=word_tokenizer.tokenize(s)
    for w in word_in_sentence:
        words.append(w)

# do NOT stem.
# from nltk.stem.porter import PorterStemmer
# porter_stemmer = PorterStemmer()
# stem_tokens=[porter_stemmer.stem(t) for t in words]
# print (stem_tokens)

lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(t) for t in words]
stopwords = stopwords.words('english')
tokens = [token for token in tokens if token not in stopwords]
tokens = [token for token in tokens if token.isalnum()]
# print(tokens)
tf = dict(FreqDist(tokens))

file_ids=brown.fileids()
idf={}
for key in tf:
    count = len([f for f in file_ids if key in brown.words(fileids=[f])])
    idf[key] = math.log(len(file_ids) / 1+count)
# print (idf)

score={}
for key in tf:
    score[key]=tf[key]*idf[key]

keywords_desc = sorted(score.items(), key=lambda x: -x[1])
terms, scores = zip(*keywords_desc)
print(terms[:10])
