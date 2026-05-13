# # Tokenization using SpaCy
# import spacy

# nlp = spacy.blank("en")

# doc = nlp("GeeksforGeeks is a one stop\
# learning destination for geeks")

# for token in doc:
#     print(token)

# # Tokenization with Part of speech and lemmatization in SpaCy

# import spacy

# nlp = spacy.load("en_core_web_sm")

# doc = nlp("If you want to be an excellent programmer \
# , be consistent to practice daily on GFG.")

# for token in doc:
#     print(token,"|",spacy.explain(token.pos_),"|",token.lemma_)

# # Display Pipeline Components

# import spacy

# nlp = spacy.load("en_core_web_sm")
# print(nlp.pipe_names)

import spacy

nlp = spacy.load("en_core_web_sm")
text = "SpaCy is a popular natural language processing library."
doc = nlp(text)

print("Original :",text)
print("POS Tagging Result:")
for token in doc:
    print(f"{token.text}:{spacy.explain(token.pos_)}")