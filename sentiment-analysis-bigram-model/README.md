##The rt-polarity.pos and rt-polarity.neg contains positive and negative sentiments on movies.

Using these two files as training data, we will use a bigram model together with python nltk to classify following two
sentiment as positive or negative.

    COMMENT_1 = "Happy and enjoyable movie."
    COMMENT_2 = "But for me I cannot support this movie due to the bad behavior from Paul."

Results will show

##Analyzing Comment [Happy and enjoyable movie.]
    Comment 1 bigram probability on positive corpora : 1.47313652007e-10
    Comment 1 bigram probability on negative corpora : 1.08696787469e-11

##Analyzing Comment [But for me I cannot support this movie due to the bad behavior from Paul.]
    Comment 2 bigram probability on positive corpora : 6.04594904834e-28
    Comment 2 bigram probability on negative corpora : 2.7989106931e-26

By observing the probabilities we can classify COMMENT_1 as a positive sentiment and COMMENT_2 as a negative sentiment.