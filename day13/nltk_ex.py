# import nltk

# print(nltk.__version__)
# nltk.download('all')

# Tokenization
# from nltk import word_tokenize, sent_tokenize
# text = "GeeksforGeeks is a great learning platform.\
#     It is one of the best for Computer Science students."
# print(word_tokenize(text))
# print(sent_tokenize(text))

# # Stemming
# from nltk.stem import PorterStemmer

# porter = PorterStemmer()
# print(porter.stem("play"))
# print(porter.stem("played"))
# print(porter.stem("playing"))                # Reduce to play which has meaning
# print(porter.stem("plays"))
# print(porter.stem("communication"))          # Reduce to commmun which is meaningless

# # Lemmatization
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("play",'v'))
# print(lemmatizer.lemmatize("played",'v'))
# print(lemmatizer.lemmatize("plays",'v'))
# print(lemmatizer.lemmatize("playing",'v'))
# print(lemmatizer.lemmatize("communication",'v'))

# # Part of Speech Tagging
# from nltk import pos_tag, word_tokenize

# text = "GeeksforGeeks is a Computer Science platform."
# tokens = word_tokenize(text)
# tags = tokens_tag = pos_tag(tokens)
# print(tags)

# Named Entity Recognition
from nltk import word_tokenize,pos_tag,ne_chunk
# import nltk

# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')

text = "Barack Obama was born in Hawaii in 1961."

tokens = word_tokenize(text)
tags = pos_tag(tokens)

entities = ne_chunk(tags)
print(entities)