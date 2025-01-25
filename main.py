import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download("stopwords")

sentence_break = """
After the dark comes the sunshine . A new day comes with new promises. Spread love and peace
"""
# This is the part to break the sentences
# sentences = sent_tokenize(sentence_break)
# for sentence in sentences :
#     print(f"{sentence}")

# Below breaks the sentence in to the words
words = word_tokenize(sentence_break)
# for word in words :
#     print(f"{word}")

#Here we are filtering the stop words, stop words is imported then checked as per the array if,stop words is equal to our word it doesnt
#get added to the array. If there is no stop word, then it gets added to the array.
stop_words = set(stopwords.words("english"))

filtered_words = []

for word in words:
    if word.casefold() not in stop_words:
        filtered_words.append(word)

print(filtered_words)
