
-------*******----------
DESCRIPTION:

Our package is deployed live at: https://cse6242-project20.herokuapp.com

This project intends to find relevant images to text using Natural Language
Processing Techniques. There are two ways to interact with the app:

1. Read through a pre-cleaned book as it generates images along the way.

2. Add your text to the text box which generates a relevant image and shows the
entire process of finding images, generating tags and scoring each one.


In detail this project does the following:
a) Applies a NLP algorithm TF-IDF (Text Frequency Inverse Document Frequency,
IDF using Brown Corpus) to find the most important keywords in the text.
b) Searches for images using those keywords.
c) Uses Google Cloud Machine Learning to find labels for the images found.
d) Utilizes Spacy to find the semantic match between the word vectors of keywords
and labels providet a score to each image.
e) Returns the image with the best score.



-------*******----------
INSTALLATION:
Note: We suggest using a OSX or Linux due to heroku/Windows setup requirements

1. Download and extract the zip file

2. The python requirements and dependencies
are present in the requirements.txt file.
command:
pip3 install -r requirements.txt

3. To download the nltk requirements, open the python shell and run the following to open the nltk downloader:
>>>import nltk
>>>nltk.download()

This will open the downloader where you can select the appropriate libraries to
download.

The nltk libraries to download are:
punkt
stopwords
averaged_perceptron_tagger

These names can also be found in nltk.txt


4. In addition, to run the code locally you will need to install the heroku
Command-Line-Interface

Installation instructions can be found here:
https://devcenter.heroku.com/articles/heroku-cli

Detailed instructions for setting up heroku can be found here:
https://devcenter.heroku.com/articles/getting-started-with-python

5. You will need to create a new Heroku account if you don't already have one.
Create a free instance with:

heroku create example_name


6. A Google Cloud Console Account will need to be created along with an API key.
Instructions for that can be found here:
https://cloud.google.com/vision/docs/libraries#client-libraries-install-python

Once Google Cloud has been installed and an API key generated, save the file
somewhere secure and run the following command:

6.5 

OSX/Linux:
	export GOOGLE_APPLICATION_CREDENTIALS='path-to-your-key'
Windows:
	set GOOGLE_APPLICATION_CREDENTIALS='path-to-your-key'

-------*******----------
EXECUTION:
You can run the web app locally now using the 'heroku local' command. This
starts a local host(localhost:5000) server to interact with the web app.

If you'd like to deploy your site use the following command:

git push heroku master

