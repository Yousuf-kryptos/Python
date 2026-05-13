# # Stopword Removal

# # Using NLTK

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# nltk.download('punkt')

# text = "This is a sample sentence showing stopword removal."

# stop_words = set(stopwords.words('English'))
# tokens = word_tokenize(text.lower())

# filtered_result = [word for word in tokens if word not in stop_words]

# print("Original: ",tokens)
# print("Filtered: ",filtered_result)

# # Using SpaCy

# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("The researchers are developing advanced algorithms.")

# filter = [token.text for token in doc if not token.is_stop]

# print("Filter: ",filter)

# Using gensim

from gensim.parsing.preprocessing import remove_stopwords

new_text = "The majestic mountains provide a breathtaking view."

filter_text = remove_stopwords(new_text)

print("Original: ",new_text)
print("Filter: ",filter_text)