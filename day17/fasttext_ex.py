from gensim.models import FastText
from gensim.test.utils import common_texts
import numpy as np

# Step 1 : Prepare Training corpus
corpus = common_texts
for sentence in corpus:
    print(sentence)

# Step 2: Train FastText Model
model = FastText(sentences=corpus, 
                 vector_size=100,
                 window=5,
                 min_count=1,
                 workers=4,
                 sg=1,
                 epochs=10)

print("\n FastText Model Trained Successfully")

# Step 3: Vocabulary
print("\n Vocabulary Words:")
print(list(model.wv.index_to_key))

# Step 4: Word Embedding
word = 'computer'

word_embedding = model.wv[word]

print(f"\n Embedding Word for {word} :")
print(word_embedding)

print(f"\n Vector Shape:{word_embedding.shape}")

# Step 5: Similar Words

similar_words = model.wv.most_similar(word)

print(f"\nMost Similar words for {word}: ")

for similar_words, similarity_score in similar_words:
    print(f"{similar_words}->{similarity_score:.3f}")

# Step 6: Similarity between two words

word1 ='computer'
word2 = 'system'

similarity = model.wv.similarity(word1,word2)

print(f"\n Similarity between {word1} and {word2}:")
print(similarity)

# Step 7: Save Model

model.save("fasttext_model.model")
print("Model Saved Successfully")

# Step 8: Load the saved Model
loaded_model = FastText.load("fasttext_model.model")
print("Loaded Successfully")

# Step 9: Test Loaded Model
print("\n Most Similar Word using Loaded Model:")

loaded_similar = loaded_model.wv.most_similar('computer')

for word,score in loaded_similar:
    print(f"{word}->{score:.3f}")

# Step 10: Out-of-vocabulary word

oov_word = "computers"

oov_vector = model.wv[oov_word]

print("\n Vector for unseen word {oov_word}:")
print(oov_vector[:10])

# Step 11: Analog
try:
    analog=model.wv.most_similar(
        positive =['computer','human'],
        negative=['interface'],
        topn=3
    )
    print("\n Analog Results:")

    for word, score in analog:
        print(f"{word}->{score}")
except KeyError:
    print("\n some analog does not found in vocabulary")

# Step 12: Sentence Vector
sentence = ['human', 'computer', 'interaction']

sentence_vector = np.mean([model.wv[word] for word in sentence if word in model.wv],
                          axis= 0)
print("\n Sentence Vector Shape:")
print(sentence_vector.shape)