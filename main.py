import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')
nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

sentence_break = """
After the dark comes the sunshine . A new day comes with new promises. Spreading loveful joyful and peaceful
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
# print(tagged_words)

#Lemattizing the words. This reduces the words but gives its meaning unlike Stemming
#delete this note, for self :- lematizing changes the joyful to joyful, 
lemattized_words = [lemmatizer.lemmatize(word) for word in words]
 
#Chunking indentifies phrases, to chunk a word we first tokenize it then add pos tag
#then we add the chunk grammer that defines hwo they need to be chunked
sample_quote = "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering. I sense much fear in you."
word1 = word_tokenize(sample_quote)
sample_quote_pos_tags = nltk.pos_tag(word1)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parse = nltk.RegexpParser(grammar)
tree =chunk_parse.parse(sample_quote_pos_tags)
# tree.draw()
