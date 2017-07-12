__author__ = 'eshan'

# ## Tasks ###

# read xml
# get sentences (and make lower case)
# tokenize
# remove stop words
# convert all unique words in to dictionary form
# find term frequencies

# take a random sentence from the same corpus
# make lower case
# tokenize
# remove stop words
# convert all unique words in to dictionary form
# find term frequencies (using the above term frequencies)
# calculate sentence unigram probability


print("\nText processing\n")

# Read xml file
import xml.etree.ElementTree as ET

tree = ET.parse("mov_copora.xml")
root = tree.getroot()

print("Parsing mov_copora.xml\n")
print("Number of Documents : " + str(len(root)))

words = []
sentences = []
filtered_dictionary_words = []

# Get the text for each entry, convert to lower case and tokenize in to sentences)
from nltk.tokenize import sent_tokenize

for i in range(len(root)):
    text = root[i][1].text
    sent = sent_tokenize(text.lower())
    for j in sent:
        if j not in sentences:
            sentences.append(j)

print("All together there are " + str(len(sentences)) + " sentences")

# Iterate through each sentence, tokenize in to words
from nltk.tokenize import word_tokenize

for i in sentences:
    word_tokens = word_tokenize(i)
    for j in word_tokens:
        words.append(j)

# removing stop words
from nltk.corpus import stopwords

stopwords_in_english = stopwords.words('english')
filtered_words = [word for word in words if word not in stopwords_in_english]

# conversion to dictionary form
from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()

for i in filtered_words:
    filtered_dictionary_words.append(lem.lemmatize(i))

print("All together there are " + str(len(words)) + " words")
print("All together there are " + str(len(filtered_words)) + " filtered words")
print("All together there are " + str(len(filtered_dictionary_words)) + " dictionary format words")

from nltk.probability import FreqDist

unigram_counts = FreqDist(filtered_words)


# print frequency counts for each word (FreqDist's freq function gives the probablity. Therefore no need to divide by total number of words)
#for i in unigram_counts:
#    print(i + "\t\t--> " + str(unigram_counts.freq(i)))


print("\nPart 2 - Calculating the unigram probability for a selected sentence")
selected_sentence = sentences[5].lower()

# tokenize
selected_word_tokens = word_tokenize(selected_sentence)

# remove stopwords
selected_filtered_words = [word for word in selected_word_tokens if word not in stopwords_in_english]

# covert to dictionary form
select_filtered_dictionary_words = []
for i in selected_filtered_words:
    select_filtered_dictionary_words.append(lem.lemmatize(i))

# calculating unigram probability
unigram_probablity = 1
for word in select_filtered_dictionary_words:
    term_probability = unigram_counts.freq(word)
    unigram_probablity = unigram_probablity * term_probability

print("\nThe unigram probability of the sentence '" + selected_sentence + "' is : " + str(unigram_probablity) )
