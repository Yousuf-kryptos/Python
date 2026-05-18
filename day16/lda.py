import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.corpora import Dictionary
import pyLDAvis.gensim_models

nltk.download('stopwords')
nltk.download('punkt')

documents = [
    "I love machine learning and artificial intelligence",
    "Python is used for data science and machine learning",
    "Football and cricket are popular sports",
    "Messi is a famous football player",
    "Data science uses Python and AI"
]

stop_words = set(stopwords.words('english'))

processed_doc = []

for doc in documents:
    tokens = word_tokenize(doc)
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]
    processed_doc.append(filtered_words)

print(processed_doc)

dictionary = Dictionary(processed_doc)

corpus = [dictionary.doc2bow(doc) for doc in processed_doc]

print(corpus)

from gensim.models import LdaModel

lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=2,
    random_state=42,
    passes=10
)

topics = lda_model.print_topics(num_words=5)

for topic in topics:
    print(topic)

new_doc = "Python is important for AI"

new_tokens = word_tokenize(new_doc)

new_bow = dictionary.doc2bow(new_tokens)

print(lda_model.get_document_topics(new_bow))

vis = pyLDAvis.gensim_models.prepare(
    lda_model,
    corpus,
    dictionary
)

pyLDAvis.save_html(vis,"lda_visualization.html")

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from gensim.corpora import Dictionary
# import pyLDAvis.gensim_models

# documents = [
#     "Apple releases new iPhone",
#     "Samsung launches new mobile",
#     "Cricket world cup starts",
#     "Virat Kohli scores century"
# ]

# stop_words = set(stopwords.words('english'))

# processed = []
# for doc in documents:
#     tokens = word_tokenize(doc)
#     filtered = [word for word in tokens if word.isalpha() and word not in stop_words]

#     processed.append(filtered)

# print(processed)

# dictionary = Dictionary(processed)

# corpus = [dictionary.doc2bow(doc) for doc in processed]

# print(corpus)

# from gensim.models import LdaModel

# lda_model = LdaModel(
#     corpus=corpus,
#     id2word=dictionary,
#     num_topics=2,
#     random_state=42,
#     passes=10
# )

# topics = lda_model.print_topics(num_words=5)

# for topic in topics:
#     print(topic)

# vis = pyLDAvis.gensim_models.prepare(
#     lda_model,
#     corpus,
#     dictionary
# )

# pyLDAvis.save_html(vis,"lda.html")