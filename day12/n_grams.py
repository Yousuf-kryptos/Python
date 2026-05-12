def n_grams(text,n):
    tokens = text.split()
    ngrams = tuple(tokens[i:i+n] for i in range(len(tokens)-n+1))
    return ngrams

text = "This is a statement"

unigram = n_grams(text,1)
bigram = n_grams(text,2)
trigram = n_grams(text,3)

print("Unigrams: ",unigram)
print("Bigrams: ",bigram)
print("Trigrams: ",trigram)