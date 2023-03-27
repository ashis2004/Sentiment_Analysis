from textblob import TextBlob

with open('mytext.txt','r') as f:
    text=f.read()
blob=TextBlob(text)
sentment=blob.sentiment.polarity # -1 to 1
print(sentment)