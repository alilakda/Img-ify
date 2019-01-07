import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import TreebankWordTokenizer
# from rake_nltk import Rake
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
# from nltk.corpus import brown
import numpy as np
# from google_images_download_custom import googleimagesdownload as google
import google_images_download_custom as google
from wordlist import word_list

# class Wrapper:

'''
This function takes in a list of strings.  If a string is less than X words long,
it will be added to the end of the string before.
'''
def shortSticker(text):
	notParagraph = 3
	paragraphLength = 70
	iterator = 1
	while iterator < len(text):
		if len(text[iterator].split(" ")) < notParagraph:
			del(text[iterator])
		elif len(text[iterator].split(" ")) < paragraphLength:
			text[iterator-1] = text[iterator-1] + " " + text[iterator]
			del(text[iterator])
		else:
			iterator += 1
	return text


'''
This function opens the first book file and processes it into a list of paragraphs
'''
def getBook(bookNum):
	print('Get Book ' + str(bookNum))

	if(bookNum == "1"):
		path = "static/TheGiver.txt"
	elif(bookNum == "2"):
		path = "static/sherlock_holmes.txt"
	elif(bookNum == "3"):
		path = "static/charles_dickens.txt"
	elif(bookNum == "4"):
		path = "static/tom_sawyer.txt"
	elif(bookNum == "5"):
		path = "static/grimm'sfairytales.txt"
	elif(bookNum == "6"):
		path = "static/storiesfromtagore.txt"
	elif(bookNum == "7"):
		path = "static/thehollowland.txt"
	else:
		path = "static/grimm'sfairytales.txt"

	textFromPDF = open(path, "r", encoding="utf-8").read()

	print(type(textFromPDF))

	splitText = textFromPDF.split("\n""\n")

	#print("original # paragraphs: ", len(splitText))
	return shortSticker(splitText)


def getImages(rankedPhrases):
	print('Retrieving Image Links...')

	response = google.googleimagesdownload()
	keywords = ""
	for i in range (len(rankedPhrases)):
		keywords+=str(rankedPhrases[i])+" or "
	keywords=keywords.replace(",","")
	arguments = {"keywords": keywords, "limit": 5, "output_directory": "ImageDump" ,"image_directory": "paragraph0", 'print_urls':True}
	image_path, items = response.download(arguments)
	# if len(rankedPhrases) > 2:
	# 	response = google.googleimagesdownload()
	# 	keywords = str(rankedPhrases[0])+" "+str(rankedPhrases[1])+" "+str(rankedPhrases[2])
	# 	#paragraphKeywords.append((str(rankedPhrases[0]),str(rankedPhrases[1]),str(rankedPhrases[2])))
	# 	print('WORKkeywords', keywords)
	# 	arguments = {"keywords": keywords, "limit": 5, "output_directory": "ImageDump" ,"image_directory": "paragraph0", 'print_urls':True}
	# 	image_path, items = response.download(arguments)
	# 	print('I SHOULD BE HERE ONCE', items)
	# 	#paragraphCounter +=1
	# else:
	# 	response = google.googleimagesdownload()
	# 	keywords = str(rankedPhrases[0])
	# 	#paragraphKeywords.append((str(rankedPhrases[0])))
	# 	#print(keywords)
	# 	arguments = {"keywords": keywords, "limit": 5, "output_directory": "ImageDump" ,"image_directory": "paragraph0", 'print_urls':True}
	# 	image_path, items = response.download(arguments)
	# 	#paragraphCounter +=1

	image_links = []
	for x in items:
		image_links.append(x['image_link'])

	print('Found ' + str(len(image_links)) + ' Images!')
	return image_path, image_links
	#print("paragraph keywords: ", paragraphKeywords)

def getKeywords(text):
	print('Identifying Keywords...')
	sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
	sentences=sent_tokenizer.tokenize(text)

	words=[]
	word_tokenizer = TreebankWordTokenizer()
	for s in sentences:
		word_in_sentence=word_tokenizer.tokenize(s)
		for w in word_in_sentence:
			words.append(w)
	allowed_tags=['NN','NNS','NNP','NNPS']
	lemmatizer = WordNetLemmatizer()
	stopw = stopwords.words('english')
	tokens = [token for token in words if token not in stopw]
	tokens = [token for token in tokens if token.isalnum()]
	tagged = nltk.pos_tag(tokens)
	tokens = [t[0] for t in tagged if t[1] in allowed_tags]
	tf = dict(FreqDist(tokens))
	print("done tf")
	# file_ids=brown.fileids()
	# word_list={}
	# for f in file_ids:
	# 	word_list[f]=np.unique(brown.words(fileids=[f]))
	# print("read books")
	idf={}
	for key in tf:
		count = len([k for k in word_list.keys() if key in word_list[k]])
		idf[key] = np.log(len(word_list.keys()) / 1+count)
	# print (idf)
	print("done idf")

	score={}
	for key in tf:
		score[key]=tf[key]*idf[key]

	keywords_desc = sorted(score.items(), key=lambda x: -x[1])
	terms, scores = zip(*keywords_desc)
	# r = Rake()
	# r.extract_keywords_from_text(text)
	# rankedPhrases = r.get_ranked_phrases()
	# rankedPhrasesScores = r.get_ranked_phrases_with_scores()

	print('Keywords Found!')
	return terms[:10]
	#print("ranked phrases with scores: ", rankedPhrasesScores)
	#print(rankedPhrases)


#textB = "We played robber now and then about a month, and then I resigned. All the boys did. We hadnít robbed nobody, hadnít killed any people, but only just pretended. We used to hop out of the woods and go charging down on hog-drivers and women in carts taking garden stuff to market, but we never hived any of them. Tom Sawyer called the hogs ìingots,î and he called the turnips and stuff ìjulery,î and we would go to the cave and powwow over what we had done, and how many people we had killed and marked. But I couldnít see no profit in it. One time Tom sent a boy to run about town with a blazing stick, which he called a slogan (which was the sign for the Gang to get together), and then he said he had got secret news by his spies that next day a whole parcel of Spanish merchants and rich A-rabs was going to camp in Cave Hollow with two hundred elephants, and six hundred camels, and over a thousand ìsumterî mules, all loaded down with diímonds, and they didnít have only a guard of four hundred soldiers, and so we would lay in ambuscade, as he called it, and kill the lot and scoop the things. He said we must slick up our swords and guns, and get ready. He never could go after even a turnip-cart but he must have the swords and guns all scoured up for it, though they was only lath and broomsticks, and you might scour at them till you rotted, and then they warnít worth a mouthful of ashes more than what they was before. I didnít believe we could lick such a crowd of Spaniards and A-rabs, but I wanted to see the camels and elephants, so I was on hand next day, Saturday, in the ambuscade; and when we got the word we rushed out of the woods and down the hill. But there warnít no Spaniards and A-rabs, and there warnít no camels nor no elephants. It warnít anything but a Sunday-school picnic, and only a primerclass at that. We busted it up, and chased the children up the hollow; but we never got anything but some doughnuts and jam, though Ben Rogers got a rag doll, and Jo Harper got a hymn-book and a tract; and then the teacher charged in, and made us drop everything and cut. I didnít see no diímonds, and I told Tom Sawyer so. He said there was loads of them there, anyway; and he said there was A-rabs there, too, and elephants and things. I said, why couldnít we see them, then? He said if I warnít so ignorant, but had read a book called Don Quixote, I would know without asking. He said it was all done by enchantment. He said there was hundreds of soldiers there, and elephants and treasure, and so on, but we had enemies which he called magicians; and they had turned the whole thing into an infant Sunday-school, just out of spite. I said, all right; then the thing for us to do was to go for the magicians. Tom Sawyer said I was a numskull."
