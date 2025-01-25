import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')

stemmer = PorterStemmer()

sentence_break = """
After the dark comes the sunshine . A new day comes with new promises. Spread love and peace
"""
stemming_portion ="""
The use of technology has dramatically changed how we communicate. 
Some people find its usefulness in connecting with others, while others argue about its uselessness in fostering meaningful relationships. 
Still, the user experience varies depending on how one chooses to use it.
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

#Stemming the word is the process to reduce the words to their root
# Below is the snippet for stemming the words
stemmed_portion = [stemmer.stem(word) for word in words]

# here we have done tagging part of speech , also known as pos tagging, where the text is tagged according to speech.
tagged_words = nltk.pos_tag(words)
print(tagged_words)

