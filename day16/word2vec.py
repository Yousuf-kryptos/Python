from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize

documents = [
    "I Love NLP",
    "python is very Powerful",
    "Gensim helps in Word2Vec"
]

tokens = []
for doc in documents:
    token = word_tokenize(doc)

    tokens.append(token)

print(tokens)

# Continuous Bag Of Words (CBOW)
model1 = Word2Vec(
    tokens,
    vector_size=50,
    window=2,
    min_count=1,
    sg=0                 # sg = 0 -> CBOW, sg = 1 -> SkipGram
)

# SkipGrams Model

model2 = Word2Vec(
    tokens,
    vector_size=50,
    window=2,
    min_count=1,
    sg=2                 # sg = 0 -> CBOW, sg = 1 -> SkipGram
)

print(model1.wv["python"])
print(model2.wv["python"])
print(model1.wv.most_similar('python'))
print(model2.wv.most_similar('python'))