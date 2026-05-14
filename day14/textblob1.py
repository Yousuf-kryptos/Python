# # TextBlob
# # Sentiment Analysis in TextBlob

# from textblob import TextBlob

# text1 = "GFG is a good company and always value their employees."   # Positive Statement
# text2 = "I hate bugs in my code."                                    # Negative Statement
# text3 = "The sun rises in the east."                                 # Neutral Statement
# text4 = "I enjoy coding, but debugging can be frustrating."          # Mixed Statement

# pos_blob = TextBlob(text1)
# neg_blob = TextBlob(text2)
# neu_blob = TextBlob(text3)
# mix_blob = TextBlob(text4)

# sentiment1 = pos_blob.sentiment
# sentiment2 = neg_blob.sentiment
# sentiment3 = neu_blob.sentiment
# sentiment4 = mix_blob.sentiment

# print(sentiment1)
# print(sentiment2)
# print(sentiment3)
# print(sentiment4)

# # Tokenization in TextBlob

# from textblob import TextBlob

# text = "TextBlob is very amazing and simple to use. What a great tool!"

# blob = TextBlob(text)

# print("Words: ",blob.words)
# print("Sentences: ",blob.sentences)

# # Part of Speech (POS) in TextBlob

# from textblob import TextBlob

# text = "TextBlob is very amazing and simple to use. What a great tool!"

# blob = TextBlob(text)

# print("POS Tags: ",blob.tags)

# Noun Phrase Extraction in TextBlob

from textblob import TextBlob

text = "TextBlob is very amazing and simple to use. What a great tool!"

blob = TextBlob(text)

print("Noun Phrases: ",blob.noun_phrases)
print("Upper Case: ",blob.upper())
print("Lower Case: ",blob.lower())