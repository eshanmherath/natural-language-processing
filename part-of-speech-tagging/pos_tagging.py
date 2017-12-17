from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


def tag(sentence):
    words = word_tokenize(sentence)
    words_with_tags = pos_tag(words)
    return words_with_tags

print(tag("I am superman"))