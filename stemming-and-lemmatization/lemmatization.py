__author__ = 'eshan'

''' following two lines are needed only if the machine on which the code is running doesnt have nltk corpora '''
# import nltk
# nltk.download()

''' lemmatization using part of speech tag '''

from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print('Lemmatization with PoS\n=====================')
print('studying -> '  + lemmatizer.lemmatize('studying', 'v'))
print('studying -> '  + lemmatizer.lemmatize('studying', 'n'))
