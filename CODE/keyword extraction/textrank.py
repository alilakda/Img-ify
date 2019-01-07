from nltk import sent_tokenize, word_tokenize, pos_tag
import numpy as np
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from google_images_download import google_images_download as google

sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
text="The lift rushed on at the speed of a rocket. Now it was beginning to climb. It was shooting up and up and up on a steep slanty course as if it were climbing a very steep hill. Then suddenly, as though it had come to the top of the hill and gone over a precipice, it dropped like a stone and Charlie felt his tummy coming right up into his throat, and Grandpa Joe shouted, 'Yippee! Here we go!' and Mrs Teavee cried out, 'The rope has broken! We're going to crash!' And Mr Wonka said, 'Calm yourself, my dear lady,' and patted her comfortingly on the arm. And then Grandpa Joe looked down at Charlie who was clinging to his legs, and he said, 'Are you all right, Charlie?' Charlie shouted, 'I love it! It's like being on a roller coaster!' And through the glass walls of the lift, as it rushed along, they caught sudden glimpses of strange and wonderful things going on in some of the other rooms:"

sentences=sent_tokenizer.tokenize(text)
# print (sentences)
words=[]
word_tokenizer = TreebankWordTokenizer()
for s in sentences:
    word_in_sentence=word_tokenizer.tokenize(s)
    for w in word_in_sentence:
        words.append(w)

stopwords = stopwords.words('english')
words = [word.lower() for word in words if word.lower() not in stopwords]
words = [word for word in words if word.isalnum()]
# print(words)

distinct_words=np.unique(words)
N=5
# print(distinct_words)
graph=[[0 for i in range(len(distinct_words))] for j in range(len(distinct_words))]
for i in range(len(distinct_words)):
    close_words=[]
    for index in np.where(np.array(words)==distinct_words[i])[0]:
        low=max(index-N,0)
        high=min(index+N,len(distinct_words))
        # print(words[low:high])
        for w in words[low:high]:
            if w not in close_words:
                close_words.append(w)
    # print(close_words)
    for j in range(0,len(distinct_words)):
        if distinct_words[j] in close_words:
            graph[i][j]=graph[j][i]=1
score=[0 for i in range(len(distinct_words))]
check=1
d=0.85
count=0
while (check and count<100):
    count+=1
    check=0
    for i in range(len(distinct_words)):
        original=score[i]
        s=0
        for index in np.where(np.array(graph[i])==1)[0]:
            s+=score[index]/(np.array(graph[index])==1).sum()
        score[i]=(1-d)+d*s
        if ((score[i]-original)>0.001):
            check=1
# print(score)
# print(count)
keydict = dict(zip(distinct_words, score))
# print(keydict)
keywords_desc = sorted(keydict.items(), key=lambda x: -x[1])
final, values = zip(*keywords_desc)
print(final[:15])

response = google.googleimagesdownload()
keys=""
for i in range (15):
    keys+=str(final[i])+" "
# paragraphKeywords.append((str(rankedPhrases[0]),str(rankedPhrases[1]),str(rankedPhrases[2])))
print(keys)
arguments = {"keywords": keys, "limit": 10, "image_directory": "paragraph1"}
image_path = response.download(arguments)
# print (np.matrix(graph))
# print (distinct_words)
