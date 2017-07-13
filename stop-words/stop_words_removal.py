__author__ = 'eshan'

from sklearn.feature_extraction.text import CountVectorizer

corpus = ['Superman is the best superhero ever and is in justice league and he is the golden standard']

vectorizer1 = CountVectorizer()
vectorizer1.fit_transform(corpus)

vocabulary = vectorizer1.vocabulary_
print("Bag of words with stop words : " + str(len(vocabulary)))
print(vocabulary)

vectorizer2 = CountVectorizer(stop_words='english')
vectorizer2.fit_transform(corpus)

vocabulary = vectorizer2.vocabulary_
print("\nBag of words with stop words removed : " + str(len(vocabulary)))
print(vocabulary)