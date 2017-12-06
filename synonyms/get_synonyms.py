from nltk.corpus import wordnet

synonyms = wordnet.synsets("happy")

first_synonym = synonyms[0].definition()
example_for_first_synonym = synonyms[0].examples()

print(first_synonym)

print(example_for_first_synonym)