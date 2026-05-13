from collections import Counter

vocab = {
    'low': 5,
    'lower': 2,
    'n e w e s t': 6,
    'w i d e s t': 3
}

def get_pairs(vocab):
    pairs = Counter()
    
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[(symbols[i],symbols[i+1])] += freq
    return pairs

def merge_vocab(vocab,pair):
    new_vocab = {}
    old = ' '.join(pair)
    new = ''.join(pair)
    for word, freq in vocab.items():
        new_word = word.replace(old,new)
        new_vocab[new_word] = freq
    return new_vocab

num_merges = 5

for _ in range(num_merges):
    pairs = get_pairs(vocab)
    if not pairs: break
    most_common = pairs.most_common(1)[0][0]
    vocab = merge_vocab(vocab,most_common)
    print(f"Merged : {most_common}-> {''.join(most_common)}")

print("Final Vacabulary")
for word in vocab:
    print(word)