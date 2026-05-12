import re
from collections import OrderedDict, defaultdict

def preprocess_text(text):
    text = text.lower()
    
    tokens = re.findall(r'\w+|[^\w\s]', text)
    
    return tokens

sample_text = """GeeksforGeeks is a fantastic resource for geeks 
who are looking to enhance their programming skills, 
and if you're a geek who wants to become an expert programmer, 
then GeeksforGeeks is definitely the go-to place for geeks like you."""

word_tokens = preprocess_text(sample_text)
print("Word-level tokens:")
print(word_tokens)
print(f"Total unique tokens: {len(set(word_tokens))}")