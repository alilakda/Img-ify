from rake import Rake
# from nltk.corpus import stopwords
# from nltk.tokenize import TreebankWordTokenizer
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
text="We worked on; but the water increasing in the hold, it was apparent that the ship would founder; and though the storm began to abate a little, yet it was not possible she could swim till we might run into any port; so the master continued firing guns for help; and a light ship, who had rid it out just ahead of us, ventured a boat out to help us. It was with the utmost hazard the boat came near us; but it was impossible for us to get on board, or for the boat to lie near the ship’s side, till at last the men rowing very heartily, and venturing their lives to save ours, our men cast them a rope over the stern with a buoy to it, and then veered it out a great length, which they, after much labour and hazard, took hold of, and we hauled them close under our stern, and got all into their boat. It was to no purpose for them or us, after we were in the boat, to think of reaching their own ship; so all agreed to let her drive, and only to pull her in towards shore as much as we could; and our master promised them, that if the boat was staved upon shore, he would make it good to their master: so partly rowing and partly driving, our boat went away to the northward, sloping towards the shore almost as far as Winterton Ness"

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
r.extract_keywords_from_text(text)
l=r.get_ranked_phrases()[:10] # To get keyword phrases ranked highest to lowest.
print(l)
# tag = "clump of bushes had a secret"
# keywords_words=[]
# word_tokenizer = TreebankWordTokenizer()


# #extract words from keywords
# for phrase in r.get_ranked_phrases():
#     word_in_sentence=word_tokenizer.tokenize(phrase)
#     for w in word_in_sentence:
#         keywords_words.append(w)

# lemmatizer = WordNetLemmatizer()
# keywords_words = [lemmatizer.lemmatize(t) for t in keywords_words]
# stopwords = stopwords.words('english')
# keywords_words = [token for token in keywords_words if token not in stopwords]

# #extract words from tag
# words=[]
# word_in_sentence=word_tokenizer.tokenize(tag)
# for w in word_in_sentence:
#     words.append(w)

# tag_words = [lemmatizer.lemmatize(t) for t in words]
# tag_words = [token for token in tag_words if token not in stopwords]

# #match
# match_words=[]
# for word in tag_words:
#     for syn in wordnet.synsets(word):
#         synonyms=[]
#         for l in syn.lemmas():
#             synonyms.append(l.name())
#         for w in synonyms:
#             if w in keywords_words and w not in match_words:
#                 match_words.append(w)

# score_by_tag=len(match_words)/len(tag_words)
# score_by_keywords=len(match_words)/len(keywords_words)

# print(score_by_keywords,score_by_tag)

