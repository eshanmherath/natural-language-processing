__author__ = 'eshan'

import io

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer

POSITIVE_FILE = "rt-polarity.pos"
NEGATIVE_FILE = "rt-polarity.neg"
TOKENIZER = WordPunctTokenizer()
LEMMATIZER = WordNetLemmatizer()
ENGLISH_STOP_WORDS = set(stopwords.words('english'))


def get_tokens(l):
    tokens = TOKENIZER.tokenize(l)
    return [token.lower() for token in tokens]


def get_lemma(word1):
    return LEMMATIZER.lemmatize(word1)


def remove_stop_words(words):
    return [w for w in words if w not in ENGLISH_STOP_WORDS]


def get_unigram_counts(file_name):
    total_words_in_corpora = 0
    word_counts = {}
    with io.open(file_name, encoding='utf-8', errors='ignore') as f:
        for line in f:
            words_of_line = get_tokens(line)
            filtered_words = remove_stop_words(words_of_line)
            for word in filtered_words:
                processed_word = get_lemma(word)
                total_words_in_corpora += 1
                if processed_word not in word_counts.keys():
                    word_counts[processed_word]=1
                else:
                    current_count = word_counts[processed_word]
                    word_counts[processed_word] = current_count+1
    return [total_words_in_corpora, word_counts]


def get_bigram_probability(comment, total_words, word_counts):
    comment_tokens = get_tokens(comment)
    comment_words = remove_stop_words(comment_tokens)
    probability = 1
    for w in comment_words:
        lem = get_lemma(w)
        if lem is not '.':
            if lem not in word_counts.keys():
                print("Error : The analyzer hasn't seen the word " + lem + " during training")
            else:
                probability *= word_counts[lem]*1.0/total_words
    return probability

print("Sentiment Analyzer Creation Started\n")

[total_words_in_positive_corpora, positive_word_counts] = get_unigram_counts(POSITIVE_FILE)
[total_words_in_negative_corpora, negative_word_counts] = get_unigram_counts(NEGATIVE_FILE)

print("Sentiment Analyzer Creation Completed\n")

COMMENT_1 = "Happy and enjoyable movie."
COMMENT_2 = "But for me I cannot support this movie due to the bad behavior from Paul."

print("Analyzing Comment [" + COMMENT_1 + "]")
comment_1_positive_probability = get_bigram_probability(COMMENT_1, total_words_in_positive_corpora, positive_word_counts)
comment_1_negative_probability = get_bigram_probability(COMMENT_1, total_words_in_negative_corpora, negative_word_counts)

print("Comment 1 bigram probability on positive corpora : " + str(comment_1_positive_probability))
print("Comment 1 bigram probability on negative corpora : " + str(comment_1_negative_probability))

print("\nAnalyzing Comment [" + COMMENT_2 + "]")
comment_2_positive_probability = get_bigram_probability(COMMENT_2, total_words_in_positive_corpora, positive_word_counts)
comment_2_negative_probability = get_bigram_probability(COMMENT_2, total_words_in_negative_corpora, negative_word_counts)

print("Comment 2 bigram probability on positive corpora : " + str(comment_2_positive_probability))
print("Comment 2 bigram probability on negative corpora : " + str(comment_2_negative_probability))
