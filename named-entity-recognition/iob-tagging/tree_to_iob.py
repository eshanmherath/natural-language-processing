import nltk
from nltk.chunk import tree2conlltags

sentence = 'Elon and Hawking met at SpaceX last Tuesday to discuss Artificial Intelligence'

try:
    tokenized_sentence = nltk.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(tokenized_sentence)
    named_entity_tree = nltk.ne_chunk(tagged_sentence)
    iob_tagged = tree2conlltags(named_entity_tree)
    for i in iob_tagged:
        print(i)
except Exception as e:
    print(e)

