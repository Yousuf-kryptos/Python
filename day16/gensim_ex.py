import gensim

# print(gensim.__version__)
# Step 1: Pre - Processing
from gensim.utils import simple_preprocess

documents = [
    "Artificial Intelligence and Machine Learning are transforming the world",
    "Python is widely used in Data Science and NLP",
    "Gensim is a powerful NLP library",
    "Football and Cricket are popular sports",
    "Messi is a famous football player"
]

tokens = [simple_preprocess(doc) for doc in documents]
print(tokens)

# Step 2: Create Dictionary and print tokens in tokens to id

from gensim.corpora import Dictionary

dictionary = Dictionary(tokens)

# print(dictionary)
print(dictionary.token2id)

# Step 3: Bag of Words

corpus = [dictionary.doc2bow(token) for token in tokens]

print(corpus)

# Step 4: TF-IDF

from gensim.models import TfidfModel

tfidf = TfidfModel(corpus)

tfidf_corpus = tfidf[corpus]

print(tfidf_corpus)

# Step 5: Word2Vec

from gensim.models import Word2Vec

model = Word2Vec(
    tokens,
    vector_size=50,
    window=3,
    min_count=1
)

print(model.wv['python'])
print(model.wv.most_similar('python'))
model.save('word2vec.model')

# Step 6: LDA Model

from gensim.models import LdaModel

lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=2,
    passes=10
)

topics = lda_model.print_topics()

for topic in topics:
    print(topic)

# Step 7: Doc2Vec

from gensim.models.doc2vec import Doc2Vec,TaggedDocument

tagged_data = []

for i, doc in enumerate(documents):
    tokens = simple_preprocess(doc)

    tagged_doc = TaggedDocument(
        words = tokens,
        tags = [str(i)]
    )

    tagged_data.append(tagged_doc)

print(tagged_data)

model = Doc2Vec(
    tagged_data,
    vector_size=50,
    window=2,
    min_count=1,
    epochs=100
)

vector = model.dv['0']

print(vector)

similar_docs = model.dv.most_similar('0')
print(similar_docs)

new_doc = "Python and AI are related"

tokens = simple_preprocess(new_doc)

new_vector = model.infer_vector(tokens)

print(new_vector)

# Step 8: Lemmatization and Stopwords

from gensim.parsing.preprocessing import remove_stopwords

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

processed_doc = []

for doc in documents:
    clean_text = remove_stopwords(doc)

    tokens = simple_preprocess(clean_text)

    lemmas = []

    for word in tokens:
        lemma = lemmatizer.lemmatize(word)
        lemmas.append(lemma)
    
    processed_doc.append(lemmas)

print(processed_doc)

# Step 9: LSI Model

from gensim.models import LsiModel

lsi_model = LsiModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics = 7, 
    decay = 0.5
    )

print(lsi_model.print_topics(-1))
