# # Name Entity Recognition

# import spacy
# from spacy import displacy

# nlp = spacy.load("en_core_web_sm")


# content = "Elon Musk founded SpaceX in California in 2002."

# doc = nlp(content)
# displacy.render(doc,style="ent")

# for ent in doc.ents:
#     print(ent.text,ent.label_)

# # Lemmatization using SpaCy

# import spacy

# nlp = spacy.load("en_core_web_sm")

# text = "The boys are running and studying in schools."

# doc = nlp(text)

# for tokens in doc:
#     print(tokens.text,"--->",tokens.lemma_)

# Text Classification in SpaCy

import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cricket match was exciting and India won the game."

doc = nlp(text)

sports_words = ["football","cricket","match","game"]

if any(word.text.lower() in sports_words for word in doc):
    print("Category: Sports")

else:
    print("Category: Other")