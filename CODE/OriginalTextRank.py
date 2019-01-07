from nltk import sent_tokenize, word_tokenize, pos_tag
import numpy as np
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from rake_nltk import Rake
from google_images_download import google_images_download as google
'''
sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
textO="We worked on; but the water increasing in the hold, it was apparent that the ship would founder; and though the storm began to abate a little, yet it was not possible she could swim till we might run into any port; so the master continued firing guns for help; and a light ship, who had rid it out just ahead of us, ventured a boat out to help us. It was with the utmost hazard the boat came near us; but it was impossible for us to get on board, or for the boat to lie near the ship’s side, till at last the men rowing very heartily, and venturing their lives to save ours, our men cast them a rope over the stern with a buoy to it, and then veered it out a great length, which they, after much labour and hazard, took hold of, and we hauled them close under our stern, and got all into their boat. It was to no purpose for them or us, after we were in the boat, to think of reaching their own ship; so all agreed to let her drive, and only to pull her in towards shore as much as we could; and our master promised them, that if the boat was staved upon shore, he would make it good to their master: so partly rowing and partly driving, our boat went away to the northward, sloping towards the shore almost as far as Winterton Ness"

textA = "Why, they rub an old tin lamp or an iron ring, and then the genies come tearing in, with the thunder and lightning a-ripping around and the smoke a-rolling, and everything they're told to do they up and do it.  They don't think nothing of pulling a shot-tower up by the roots, and belting a Sunday-school superintendent over the head with itóor any other man."
textB = "We played robber now and then about a month, and then I resigned. All the boys did. We hadn't robbed nobody, hadn't killed any people, but only just pretended. We used to hop out of the woods and go charging down on hog-drivers and women in carts taking garden stuff to market, but we never hived any of them. Tom Sawyer called the hogs 'ingots, and he called the turnips and stuff 'julery, and we would go to the cave and powwow over what we had done, and how many people we had killed and marked. But I couldn't see no profit in it. One time Tom sent a boy to run about town with a blazing stick, which he called a slogan (which was the sign for the Gang to get together), and then he said he had got secret news by his spies that next day a whole parcel of Spanish merchants and rich A-rabs was going to camp in Cave Hollow with two hundred elephants, and six hundred camels, and over a thousand 'sumter mules, all loaded down with di'monds, and they didn't have only a guard of four hundred soldiers, and so we would lay in ambuscade, as he called it, and kill the lot and scoop the things. He said we must slick up our swords and guns, and get ready. He never could go after even a turnip-cart but he must have the swords and guns all scoured up for it, though they was only lath and broomsticks, and you might scour at them till you rotted, and then they warn't worth a mouthful of ashes more than what they was before. I didn't believe we could lick such a crowd of Spaniards and A-rabs, but I wanted to see the camels and elephants, so I was on hand next day, Saturday, in the ambuscade; and when we got the word we rushed out of the woods and down the hill. But there warn't no Spaniards and A-rabs, and there warn't no camels nor no elephants. It warn't anything but a Sunday-school picnic, and only a primerclass at that. We busted it up, and chased the children up the hollow; but we never got anything but some doughnuts and jam, though Ben Rogers got a rag doll, and Jo Harper got a hymn-book and a tract; and then the teacher charged in, and made us drop everything and cut. I didn't see no di'monds, and I told Tom Sawyer so. He said there was loads of them there, anyway; and he said there was A-rabs there, too, and elephants and things. I said, why couldn't we see them, then? He said if I warn't so ignorant, but had read a book called Don Quixote, I would know without asking. He said it was all done by enchantment. He said there was hundreds of soldiers there, and elephants and treasure, and so on, but we had enemies which he called magicians; and they had turned the whole thing into an infant Sunday-school, just out of spite. I said, all right; then the thing for us to do was to go for the magicians. Tom Sawyer said I was a numskull."
textC = "Once upon a midnight dreary, while I pondered, weak and weary,Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door."
textD = "After this he pressed me earnestly, and in the most affectionate manner, not to play the young man, nor to precipitate myself into miseries which nature, and the station of life I was born in, seemed to have provided against; that I was under no necessity of seeking my bread; that he would do well for me, and endeavour to enter me fairly into the station of life which he had just been recommending to me; and that if I was not very easy and happy in the world, it must be my mere fate or fault that must hinder it; and that he should have nothing to answer for, having thus discharged his duty in warning me against measures which he knew would be to my hurt; in a word, that as he would do very kind things for me if I would stay and settle at home as he directed, so he would not have so much hand in my misfortunes as to give me any encouragement to go away; and to close all, he told me I had my elder brother for an example, to whom he had used the same earnest persuasions to keep him from going into the Low Country wars, but could not prevail, his young desires prompting him to run into the army, where he was killed; and though he said he would not cease to pray for me, yet he would venture to say to me, that if I did take this foolish step, God would not bless me, and I should have leisure hereafter to reflect upon having neglected his counsel when there might be none to assist in my recovery."
textE = "I observed in this last part of his discourse, which was truly prophetic, though I suppose my father did not know it to be so himself - I say, I observed the tears run down his face very plentifully, especially when he spoke of my brother who was killed: and that when he spoke of my having leisure to repent, and none to assist me, he was so moved that he broke off the discourse, and told me his heart was so full he could say no more to me."
textF = " few miles south of Soledad, the Salinas River drops in close to the hillsidebank   and   runs   deep   and   green.   The   water   is   warm   too,   for   it   has   slipped     twinkling over the yellow sands in the sunlight before reaching the narrow pool.     On one side of the river the golden foothill slopes curve up to the strong and     rocky Gabilan Mountains, but on the valley side the water is lined with trees—     willows fresh and green with every spring, carrying in their lower leaf junctures     the   debris   of   the   winter’s   flooding;   and   sycamores   with   mottled,   white,     recumbent limbs and branches that arch over the pool. On the sandy bank under     the trees the leaves lie deep and so crisp that a lizard makes a great skittering if     he runs among them. Rabbits come out of the brush to sit on the sand in the     evening, and the damp flats are covered with the night tracks of ‘coons, and     with the spreadpads of dogs from the ranches, and with the split-wedge tracks of     deer that come to drink in the dark.    There is a path through the willows and among the sycamores, a path beaten     hard by boys coming down from the ranches to swim in the deep pool, and     beaten hard by tramps who come wearily down from the highway in the evening     to jungle-up near water. In front of the low horizontal limb of a giant sycamore     there is an ash pile made by many fires; the limb is worn smooth by men who     have sat on it."
textG =  '“Up north?” “In Weed.” “Oh, sure. I remember. In Weed.” “That ranch we’re goin’ to is right down there about a quarter mile. We’re gonna go in an’ see the boss. Now, look—I’ll give him the work tickets, but you ain’t gonna say a word. You jus’ stand there and don’t say nothing. If he finds out what a crazy bastard you are, we won’t get no job, but if he sees ya work before he hears ya talk, we’re set. Ya got that?” “Sure, George. Sure I got it.” “O.K. Now when we go in to see the boss, what you gonna do?” “I . . . . I . . . .” Lennie thought. His face grew tight with thought. “I . . . . ain’t gonna say nothin’. Jus’ gonna stan’ there.” “Good boy. That’s swell. You say that over two, three times so you sure won’t forget it.” Lennie droned to himself softly, “I ain’t gonna say nothin’ . . . . I ain’t gonna say nothin’ . . . . I ain’t gonna say nothin’.” “O.K.,” said George. “An’ you ain’t gonna do no bad things like you done in Weed, neither.”  Lennie looked puzzled. “Like I done in Weed?” “Oh, so ya forgot that too, did ya? Well, I ain’t gonna remind ya, fear ya do it A light of understanding broke on Lennie’s face. “They run us outa Weed,” he exploded triumphantly. “Run us out, hell,” said George disgustedly. “We run. They was lookin’ for us, but they didn’t catch us.”'

text = textG

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
        score[i]=round((1-d)+d*s,2)
        if ((score[i]-original)>0.001):
            check=1
# print(score)
# print(count)
keydict = dict(zip(distinct_words, score))
# print(keydict)
keywords_desc = sorted(keydict.items(), key=lambda x: -x[1])
rankedPhrases, values = zip(*keywords_desc)
#print(rankedPhrases)
#print()
print("rank keywords: ", keywords_desc[:10])
print()
# print (np.matrix(graph))
# print (distinct_words)

r = Rake()
r.extract_keywords_from_text(text)
rankedPhrases = r.get_ranked_phrases()
rankedPhrasesScores = r.get_ranked_phrases_with_scores()
#print("ranked phrases with scores: ", rankedPhrasesScores[:10])
#print(rankedPhrases[:15])

newlyScoredList = []
for item in rankedPhrasesScores:
    #print(item[1])
    #print(item)
    maxScore = 0
    totalScore = 0
    sumScore = 0
    wordList = item[1].split(" ")
    for word in wordList:
        try:
            sumScore += item[0]*keydict[word]
            totalScore += keydict[word]
            if keydict[word] > maxScore:
                maxScore = keydict[word]
        except:
            continue
    avgScore = totalScore/len(wordList)
    #print("max: ",maxScore, " average: ", avgScore)
    maxCompositeScore = round(maxScore + item[0]/len(wordList),2)
    avgCompositeScore = round(avgScore + item[0]/len(wordList),2)
    newlyScoredList.append((item[1], round(item[0],2), round(maxCompositeScore,2), round(avgCompositeScore,2), round(sumScore/len(wordList),2)))
#print(newlyScoredList[:10])
rankedPhrasesMax = sorted(newlyScoredList, key = lambda tup: tup[2], reverse = True)
rankedPhrasesAvg = sorted(newlyScoredList, key = lambda tup: tup[3], reverse = True)
rankedPhrasesMult = sorted(newlyScoredList, key = lambda tup: tup[4], reverse = True)
print("Orig scores: ", rankedPhrases[:10])
print()
print("Mult scores: ", rankedPhrasesMult[:10])
print()
print("Avg scores: ", rankedPhrasesAvg[:10])
print()
print("Max scores: ", rankedPhrasesMax[:10])

'''
#IMAGE SEARCH FOR RAKE ALGORITHM
response = google.googleimagesdownload()
keywords = str(rankedPhrases[0])+" OR "+str(rankedPhrases[1])+" OR "+str(rankedPhrases[2]) + " OR " + str(rankedPhrases[3]) + " OR " str(rankedPhrases[4])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphNormOR", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

'''
#IMAGE SEARCH FOR MAX COMPOSITE SCORE
response = google.googleimagesdownload()
keywords = str(rankedPhrasesMax[0][0])+" OR "+str(rankedPhrasesMax[1][0])+" OR "+str(rankedPhrasesMax[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphMaxOR", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR AVG COMPOSITE SCORE
response = google.googleimagesdownload()
keywords = str(rankedPhrasesAvg[0][0])+" OR "+str(rankedPhrasesAvg[1][0])+" OR "+str(rankedPhrasesAvg[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphAvgOR", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR MULT COMPOSITE SCORE
response = google.googleimagesdownload()
keywords = str(rankedPhrasesMult[0][0])+" OR "+str(rankedPhrasesMult[1][0])+" OR "+str(rankedPhrasesMult[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphMultOR", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR RAKE ALGORITHM no OR
response = google.googleimagesdownload()
keywords = str(rankedPhrases[0])+" "+str(rankedPhrases[1])+" "+str(rankedPhrases[2])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphNorm", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR MAX COMPOSITE SCORE no OR
response = google.googleimagesdownload()
keywords = str(rankedPhrasesMax[0][0])+" "+str(rankedPhrasesMax[1][0])+" "+str(rankedPhrasesMax[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphMax", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR AVG COMPOSITE SCORE no OR
response = google.googleimagesdownload()
keywords = str(rankedPhrasesAvg[0][0])+" "+str(rankedPhrasesAvg[1][0])+" "+str(rankedPhrasesAvg[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphAvg", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)

#IMAGE SEARCH FOR MULT COMPOSITE SCORE no OR
response = google.googleimagesdownload()
keywords = str(rankedPhrasesMult[0][0])+" "+str(rankedPhrasesMult[1][0])+" "+str(rankedPhrasesMult[2][0])
#print(keywords)
arguments = {"keywords": keywords, "limit": 15, "output_directory": "ImageDump" ,"image_directory": "paragraphMult", "usage_rights": "labeled-for-reuse", "safe_search": "sa", "size": "large"}
image_path = response.download(arguments)