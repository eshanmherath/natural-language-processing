__author__ = 'eshan'

from sklearn.feature_extraction.text import CountVectorizer

corpus = ['Superman is the best superhero ever and is in justice league',
          'Batman is a pretty awesome superhero and also a justice league member',
          'sky is blue and white']

vectorizer = CountVectorizer()

feature_vector = vectorizer.fit_transform(corpus).todense()
print(feature_vector)

vocabulary = vectorizer.vocabulary_
print(vocabulary)


'''The CountVectorizer class can produce a bag-of-words representation from a string or file.
By default, CountVectorizer converts the characters in the documents to lowercase, and tokenizes the documents.
The CountVectorizer class tokenizes using a regular expression that splits strings on whitespace and extracts sequences of
characters that are two or more characters in length. '''


from sklearn.metrics.pairwise import euclidean_distances

print('\nDistance Calculations\n=====================')

print("'Superman is the best superhero ever and is in justice league' and  'Batman is a pretty awesome superhero and also a justice league member'" )
print(euclidean_distances(feature_vector[0], feature_vector[1]))

print("'Superman is the best superhero ever and is in justice league' and  'sky is blue and white'" )
print(euclidean_distances(feature_vector[0], feature_vector[2]))
