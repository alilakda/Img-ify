from nltk.corpus import wordnet
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

keywords=['bag','cat','gold','shore']
tag = "it was a bag of gold cats"

word_tokenizer = TreebankWordTokenizer()
words=[]
word_in_sentence=word_tokenizer.tokenize(tag)
for w in word_in_sentence:
    words.append(w)
keywords_words=[]
for k in keywords:
    print(len(k))
    word_in_keyword=word_tokenizer.tokenize(k)
    for w in k:
        keywords_words.append(w)

print(keywords_words)

lemmatizer = WordNetLemmatizer()
tag_words = [lemmatizer.lemmatize(t) for t in words]
stopwords = stopwords.words('english')
tag_words = [token for token in tag_words if token not in stopwords]

print (tag_words)
match_words=[]
for word in tag_words:
    for syn in wordnet.synsets(word):
        synonyms=[]
        for l in syn.lemmas():
            synonyms.append(l.name())
        for w in synonyms:
            if w in keywords and w not in match_words:
                match_words.append(w)
print(match_words)

score_by_tag=len(match_words)/len(tag_words)
score_by_keywords=len(match_words)/len(keywords)

print(score_by_keywords,score_by_tag)
