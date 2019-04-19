import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer



def myVectorAnalysis(a,b):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([str(a),str(b)])
    c = ((tfidf * tfidf.T).A)
    ret = (c[0][1])
    return ret

a1 = "James Dixon Swan (born 28 April 1956), better known as Jimmy Barnes, is a Scottish-born Australian rock singer-songwriter. His career both as a solo performer and as the lead vocalist with the rock band Cold Chisel has made him one of the most popular and best-selling Australian music artists of all time. The combination of 14 Australian Top 40 albums for Cold Chisel and 13 charting solo albums, including nine No. 1s, gives Barnes the highest number of hit albums of any Australian artist."
b1 = "Alice and Bob are two commonly used placeholder names. They are used for archetypal characters in fields such as cryptography, game theory and physics. The names are used for convenience; for example, Alice sends a message to Bob encrypted with his public key is easier to follow than Party A sends a message to Party B encrypted by Party B's public key. Following the alphabet, the specific names have evolved into common parlance within these fields—helping technical topics to be explained in a more understandable fashion.",

c1 = myVectorAnalysis(a1,b1)
print(c1)