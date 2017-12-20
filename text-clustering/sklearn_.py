articles = ["alfred, jacobs, m, 1977, 10, 18", "alex, granado, f, 1950, 12, 16",
                "anthony, smith, m, 1969, 1, 15", "antony, smith, m, 1969, 1, 15",
                "alfrad, jacobs, m, 1977, 10, 17"]

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(articles)
feature_names = vectorizer.get_feature_names()
dense = tfidf_matrix.todense()
denselist = dense.tolist()
print(denselist)
print(feature_names)

# import pandas as pd
# df = pd.DataFrame(denselist, columns=feature_names, index=characters)
# s = pd.Series(df.loc['Adam'])
# s[s > 0].sort_values(ascending=False)[:10]