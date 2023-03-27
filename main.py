import nltk

from textblob import TextBlob
from newspaper import Article

url='https://www.aajtak.in/crime/news/story/husband-brought-two-men-to-my-room-showed-adult-films-tsty-1643710-2023-02-25'
article=Article(url)

article.download()
article.parse()
article.nlp()

text=article.text
print(text)

blob=TextBlob(text)
sentiment=blob.sentiment.polarity # -1 to 1
print(sentiment)