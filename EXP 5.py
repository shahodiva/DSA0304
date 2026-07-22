from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "runner", "running", "studies"]

print("Original Word --> Stemmed Word")

for word in words:
    print(word, "-->", ps.stem(word))