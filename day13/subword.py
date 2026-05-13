import re
from collections import defaultdict,OrderedDict

def preprocess_text(text):
    text = text.lower()

    tokens = re.findall(r"\w+|[^\w\s]",text)

    return tokens

sample_text = """GeeksforGeeks is a fantastic resource for geeks 
who are looking to enhance their programming skills, 
and if you're a geek who wants to become an expert programmer, 
then GeeksforGeeks is definitely the go-to place for geeks like you."""

word_tokens = preprocess_text(sample_text)
print("Word-Tokens:")
print(word_tokens)
print(f"Total Word Tokens:{len(set(word_tokens))}")

def create_char_vocabulary(tokens):
    char_vocab = defaultdict(int)

    for token in tokens:
        char_sequence = ' '.join(list(token))
        char_vocab[char_sequence] += 1
    
    return OrderedDict(sorted(char_vocab.items(),key = lambda x:x[1],reverse=True))

char_vocab = create_char_vocabulary(word_tokens)

for i,(char_seq,freq) in enumerate(char_vocab.items()):
    if i<10:
        print(f"{char_seq}:{freq}")
    else:
        break