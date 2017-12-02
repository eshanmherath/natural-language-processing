# Simple python implementation of creating a pandas data frame with word vectors

import pandas as pd
from collections import Counter

sayings = [
    "Rose is a rose is a rose is a rose.",
    "We are going to need a bigger boat.",
    "Huston, we have a problem"
]

unique_words = set()
for saying in sayings:
    unique_words |= set(saying.split())

all_rows = {}
row_number = 0
for saying in sayings:
    word_vector = {}
    frequencies = Counter(saying.split())
    for word in unique_words:
        if word in frequencies.keys():
            word_vector[word] = frequencies[word]
        else:
            word_vector[word] = 0
    all_rows[row_number] = word_vector
    row_number += 1

data_frame = pd.DataFrame.from_dict(all_rows, orient='index')
print(data_frame)
