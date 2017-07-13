__author__ = 'eshan'

''' following two lines are needed only if the machine on which the code is running doesnt have nltk corpora '''
# import nltk
# nltk.download()

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print('Stemming\n=========')
print('running -> '  + stemmer.stem('running'))
print('laughing -> '  + stemmer.stem('laughing'))
print('ate -> '  + stemmer.stem('ate'))
print('beautiful -> '  + stemmer.stem('beautiful'))
print('might -> '  + stemmer.stem('might'))