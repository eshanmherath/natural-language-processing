import nltk
from nltk.chunk import conlltags2tree, tree2conlltags

sentence = 'Elon and Hawking met at SpaceX last Tuesday to discuss Artificial Intelligence'

try:
    tokenized_sentence = nltk.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(tokenized_sentence)
    named_entity_tree = nltk.ne_chunk(tagged_sentence)
    iob_tagged = tree2conlltags(named_entity_tree)
    ne_tree = conlltags2tree(iob_tagged)
    for i in ne_tree:
        print(i)
except Exception as e:
    print(e)

