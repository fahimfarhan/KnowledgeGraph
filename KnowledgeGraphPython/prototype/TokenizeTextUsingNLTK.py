from nltk.tokenize import sent_tokenize, word_tokenize

mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext))
print("######\n")
print(word_tokenize(mytext))
