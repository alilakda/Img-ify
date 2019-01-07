from flask import Flask, render_template, request
import sys
import json
import NLTK_Web as nk
import spacy
import string
# from sematch.semantic.similarity import WordNetSimilarity
# import NLTK_Implementation_TextboxInput as nk
from os import listdir
from os.path import isfile, join

WANTED = string.printable[:-5]

def descape(s, w=WANTED):
	return "".join(c for c in s if c in w)

def findSim(keywordList, labelList):
	if(len(keywordList) == 0):
		return 0

	nlp = spacy.load('en_core_web_sm')

	keywords = " ".join(keywordList)
	labels = " ".join(labelList)

	keywords =  nlp(keywords)
	labels =  nlp(labels)
	maxScores = []
	for key in keywords:
		maxVal = 0
		for label in labels:
			val = key.similarity(label)
			maxVal = max(maxVal,val)
		maxScores.append(maxVal)
	return sum(maxScores)/len(maxScores)

def detect_labels_uri(uri):
	"""Detects labels in the file located in Google Cloud Storage or on the
	Web."""
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	image.source.image_uri = uri

	response = client.label_detection(image=image)
	labels = response.label_annotations
	# print('Labels:')

	# for label in labels:
	#     print(label.description)
	label_list = []
	for label in labels:
		if len(label_list) <= 2:
			label_list.append(label.description)

	return(label_list)
	# print(label_list)


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
# def student():
#    return render_template('student.html')

@app.route('/loading', methods = ['POST'])
def loading():
	output = {}
	output['text'] = json.dumps(request.form['input'])[1:-1]
	output['url'] = json.dumps(request.form['url'])[1:-1]
	return render_template('loading.html', result = output)

@app.route('/result', methods = ['POST', 'GET'])
def result():
	output = {}
	if(request.method == 'POST'):
		result = request.form

		# cleanedInput = result['input'].replace('\n', ' ')
		# cleanedInput = cleanedInput.replace('\r', ' ')
		# cleanedInput = cleanedInput.replace('\t', ' ')
		cleanedInput = descape(result['input'])
		print('CLEANING INPUT', cleanedInput)

		output['text'] = json.dumps(cleanedInput)[1:-1]

		keywords = nk.getKeywords(output['text'])

		clean_keywords = []
		for word in keywords:
			clean_keywords.append(word.replace(',', ' '))

		keywords = clean_keywords
		# clean_keywords = []
		# for phrase in keywords:
		# 	clean_keywords.append(descape(phrase))
		
		# keywords = clean_keywords
		# print('KEYWORDS', keywords)

		numTerms = 10
		output["keywords"] = ""
		if (numTerms > len(keywords)):
			numKeys = range(len(keywords))
		else:
			numKeys = range(numTerms)
		for i in numKeys:
			output['keywords'] = output['keywords'] + json.dumps(keywords[i]) + " "


		# if(len(keywords) > 1):
		# 	output['keywords'] = json.dumps(keywords[0] + " " + keywords[1] + " " + keywords[2])[1:-1]
		# else:
		# 	output['keywords'] = json.dumps(keywords[0])[1:-1]

		output['imageList'], output['imageLinks'] = nk.getImages(keywords)
		# sys.stdout.close()

		output['scores'] = []
		output['labels'] = []
		if(len(output['imageLinks']) > 0):
			maxSim = 0
			bestImage = output['imageLinks'][0]
			for image in output['imageLinks']:
				labels = []
				labels = detect_labels_uri(image)
				output['labels'].append(labels)
				sim = findSim(keywords, labels)
				output['scores'].append(sim)
				if(sim > maxSim):
					maxSim = sim
					bestImage = image

			output['best'] = bestImage
		else:
			output['best'] = '//:0'

	return render_template("result.html",result = output)

paraPerPage = 1

@app.route('/book', methods = ['POST', 'GET'])
def book():
	fullBook = []
	fullBook = nk.getBook(request.args.get('bookNum'))
	output = {}
	output['first'] = 0
	print('fullbook', fullBook[0])
	page = int(request.args.get('page'))
	if(page == 0):
		index = 0
		output['page'] = index + paraPerPage
		output['first'] = 1
	elif(request.args.get('dir') != None):
		direction = request.args.get('dir')
		if(direction == 'next'):
			index = page
			output['page'] = index + paraPerPage
		elif(direction == 'prev'):
			index = page - paraPerPage
			output['page'] = index
		else:
			print('ERROR: dir passed back from book.html incorrectly')
	else:
		print('ERROR: bad parameters from book.html - page is not 0 and no direction specified')

	if(index < 0):
		print('ERROR: somehow index is less than 0 - probably bad parameters from book.html')

	output['maxPage'] = len(fullBook)
	output['bookNum'] = request.args.get('bookNum')
	output['bestLinks'] = []
	output['paragraphs'] = []
	bestLinks = []
	paragraphs = []

	for i in range(paraPerPage):
		print('Starting para ' + str(i))
		imageLinks = []
		keywords = nk.getKeywords(fullBook[index + i])
		output['paragraphs'].append(fullBook[index + i])
		paragraphs.append(fullBook[index + i])
		imageList, imageLinks = nk.getImages(keywords)

		if(len(imageLinks) > 0):
			#find best image
			maxSim = 0
			bestImage = imageLinks[0]
			for image in imageLinks:
				labels = []
				labels = detect_labels_uri(image)
				sim = findSim(keywords, labels)
				if(sim > maxSim):
					maxSim = sim
					bestImage = image

			output['bestLinks'].append(bestImage)
			bestLinks.append(bestImage)
		else:
			output['bestLinks'].append('//:0')
			bestLinks.append('//:0')

		print('Ending para ' + str(i))


	return render_template('book.html', 
		paragraphs = map(json.dumps, paragraphs),
		bestLinks = map(json.dumps, bestLinks),
		result = output)

if __name__ == '__main__':
   app.run(debug = True)
