from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

text = "Natural Language Processing is amazing"

tokens = tokenizer.tokenize(text)
print("Tokens:")
print(tokens)

encoding = tokenizer.encode(text)
print("Token ID's:")
print(encoding)

id2tokens = tokenizer.convert_ids_to_tokens(encoding)
print("Tokens:",id2tokens)