import nltk

sentence = 'Elon and Hawking met at SpaceX last Tuesday to discuss Artificial Intelligence'

try:
    tokenized_sentence = nltk.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(tokenized_sentence)
    named_entity = nltk.ne_chunk(tagged_sentence)
    print(named_entity)
    named_entity.draw()
except Exception as e:
    print(e)


