# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:09:10 2025

@author: Swapnil Mishra
"""


# import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

import newspaper
from newspaper import Article

# Support on different languages
newspaper.languages()

# Data Extraction from Times of India e-portal
url = "https://gadgetsnow.indiatimes.com/gn-advertorial/powerful-smart-and-future-ready-reasons-samsung-galaxy-book4-series-is-being-touted-as-the-smartest-year-end-tech-upgrade/articleshow/116702162.cms?_gl=1*6zywid*_ga*MjA0NTc2MTMwNy4xNzM2MDg3OTky*_ga_FCN624MN68*MTczNjA4Nzk5MS4xLjEuMTczNjA4Nzk5NS41Ni4wLjA."



# If no language is specified, Newspaper library will attempt to auto-detect a language.

# Scrap data from a given URL Download the content
article_name = Article(url, language="en")

article_name.download() 
# Parse the content from the html document
article_name.parse() 

# HTML content extracted
article_name.html

# Keyword extraction wrapper
article_name.nlp()

print("Article Title:") 
print(article_name.title) # prints the title of the article
print("\n") 

print("Article Text:") 
print(article_name.text) # prints the entire text of the article
print("\n") 

print("Article Summary:") 
print(article_name.summary) # prints the summary of the article
print("\n") 

print("Article Keywords:")
print(article_name.keywords) # prints the keywords of the article


# Write the extracted data into text file
file1 = open("News1.txt", "w+")
file1.write("Title:\n")
file1.write(article_name.title)

file1.write("\n\nArticle Text:\n")
file1.write(article_name.text)

file1.write("\n\nArticle Summary:\n")
file1.write(article_name.summary)

file1.write("\n\n\nArticle Keywords:\n")
keywords = '\n'.join(article_name.keywords)

file1.write(keywords)
file1.close()

# Read the text from the file
with open("News1.txt", "r") as file2:
    text = file2.read()
    
TOInews = re.sub("[^A-Za-z" "]+", " ", text).lower()

# Tokenize
TOInews_tokens = TOInews.split(" ")

with open("C:/Users/Swapnil Mishra/Stop_Words/stopwords.txt", "r") as sw:
    stop_words = sw.read()
    
stop_words = stop_words.split("\n")

# Cleaned tokens
tokens = [w for w in TOInews_tokens if not w in stop_words]

from collections import Counter
tokens_frequencies = Counter(tokens)

# Sorting
tokens_frequencies = sorted(tokens_frequencies.items(), key = lambda x: x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in tokens_frequencies]))
words = list(reversed([i[0] for i in tokens_frequencies]))

# Barplot of top 10 

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = ['red','green','black','yellow','blue','pink','violet'])

plt.xticks(list(range(0, 11), ), words[0:11])
plt.xlabel("Tokens")
plt.ylabel("Count")
plt.show()
##########


# Joinining all the tokens into single paragraph 
cleanstrng = " ".join(words)

wordcloud_ip = WordCloud(background_color = 'White',
                      width = 2800, height = 2400).generate(cleanstrng)
plt.axis("off")
plt.imshow(wordcloud_ip)


# positive words
with open("C:/Users/Swapnil Mishra/positive_words/positive-words.txt", "r") as pos:
  poswords = pos.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
pos_tokens = " ".join ([w for w in words if w in poswords])

wordcloud_positive = WordCloud(background_color = 'White', width = 1800,
                               height = 1400).generate(pos_tokens)
plt.figure(2)
plt.axis("off")
plt.imshow(wordcloud_positive)


# Negative words
with open("C:/Users/Swapnil Mishra/negative_words/negative-words.txt", "r") as neg:
  negwords = neg.read().split("\n")

# Negative word cloud
# Choosing the only words which are present in negwords
neg_tokens = " ".join ([w for w in words if w in negwords])

wordcloud_negative = WordCloud(background_color = 'black', width = 1800,
                               height=1400).generate(neg_tokens)
plt.figure(3)
plt.axis("off")
plt.imshow(wordcloud_negative)


'''Bi-gram Wordcloud'''
# Word cloud with 2 words together being repeated
import nltk
nltk.download('punkt')

# Generate 2 work tokens
bigrams_list = list(nltk.bigrams(words))

dictionary2 = [' '.join(tup) for tup in bigrams_list]

# Using count vectorizer to view the frequency of bigrams
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(ngram_range = (2, 2))
bag_of_words = vectorizer.fit_transform(dictionary2)
vectorizer.vocabulary_

sum_words = bag_of_words.sum(axis = 0)
words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)

words_dict = dict(words_freq[:100])


wordcloud_2 = WordCloud(background_color = 'white', width = 1800, height = 1400)
plt.figure(4)                     
wordcloud_2.generate_from_frequencies(words_dict)
plt.imshow(wordcloud_2)



''' Emotion Mining'''



import text2emotion as te
import pandas as pd

text = "I was asked to sign a third party contract a week out from stay. If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury."
te.get_emotion(text)


# Analyze emotions in the text
emotions = te.get_emotion(text)

# Display results
print("Emotion Analysis Results:")
for emotion, value in emotions.items():
    print(f"{emotion}: {value}")

# Capturing the Emotions from Tokens
emosion = te.get_emotion('work')
emosion

emosion = te.get_emotion('worst')
emosion

emosion = te.get_emotion('proper')
emosion


# Capture Emotions for the News article
emosions = []

# Capture the emotions on the tokens
for i in words:
    emosions_r = te.get_emotion(i)
    emosions.append(emosions_r)

# Call to the function

emosions = pd.DataFrame(emosions)
emosions

tokens_df = pd.DataFrame(tokens, columns=['words'])

emp_emotions = pd.concat([tokens_df, emosions], axis = 1)
emp_emotions.columns

emp_emotions[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].sum().plot.bar()

