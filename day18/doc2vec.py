from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

data = ["This is the first document",
        "This is the second document",
        "This is the third document",
        "This is the fourth document"]

tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()),tags=[str(i)])for i, doc in enumerate(data)]

model = Doc2Vec(vector_size=20,min_count=2,epochs=50)
model.build_vocab(tagged_data)
model.train(tagged_data,total_examples=model.corpus_count,epochs=model.epochs)

document_vectors = [model.infer_vector(word_tokenize(doc.lower())) for doc in data]

for i,doc in enumerate(data):
    print("Document",i+1,":",doc)
    print("Vector:",document_vectors[i])
    print()