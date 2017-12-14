import time
import nltk

sentence = 'Elon Musk is sending his Tesla Roadster to an orbit around Mars'
nltk.download()
try:
    tokenized_sentence = nltk.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(tokenized_sentence)

    named_entity = nltk.ne_chunk(tagged_sentence)
    named_entity.draw()

    time.sleep(1)

except Exception as e:
    print(e)

