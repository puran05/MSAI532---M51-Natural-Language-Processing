import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

sentence_break = """
I am the sentence . This sentence will be broken. THis is the third part of the sentence
"""

sentences = sent_tokenize(sentence_break)
for sentence in sentences :
    print(f"{sentence}")