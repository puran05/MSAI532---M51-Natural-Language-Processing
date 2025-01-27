import nltk
from nltk.book import *
from nltk import FreqDist
from nltk.corpus import stopwords

frequency_distribution = FreqDist(text7)
print(frequency_distribution.most_common(60))

stop_words = set(stopwords.words("english"))

meaningful_words = [
    word for word in text7 if word.casefold() not in stop_words
 ]

# print(meaningful_words)

frequency_distribution =FreqDist(meaningful_words)
# print(frequency_distribution.most_common(20))

collocation_word = text7.collocations()
print(collocation_word)