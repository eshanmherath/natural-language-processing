import string
import collections

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint

import pandas as pd


def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tokens


def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    tfidf_model = vectorizer.fit_transform(texts)
    print(tfidf_model)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering


if __name__ == "__main__":
    # articles = [...]
    articles = ["alfred, jacobs, m, 1977, 10, 18", "alex, granado, f, 1950, 12, 16",
                "anthony, smith, m, 1969, 1, 15", "antony, smith, m, 1969, 1, 15",
                "alfrad, jacobs, m, 1977, 10, 17"]
    clusters = cluster_texts(articles, 3)
    pprint(dict(clusters))

