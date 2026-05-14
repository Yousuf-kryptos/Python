# # Text Normalization

# import re
# import nltk
# from nltk.corpus import stopwords

# # 1. Convert to Lowercase

# string = "       Python 3.0, released in 2008, was a major revision of the language that is not " \
# "completely backward compatible and much Python 2 code does not run unmodified on Python 3." \
# " With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older " \
# "versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows)."

# lower_string = string.lower()
# # print(lower_string)

# # 2. Remove Numbers

# no_number_string = re.sub(r'\d+','',lower_string)
# # print(no_number_string)

# # 3. Removing Punctuations

# no_punc = re.sub(r'[^\w\s]','',no_number_string)
# # print(no_punc)

# # 4.Removing White Spaces

# no_wspace = no_punc.strip()
# # print(no_space)

# # 5. Removing Stopwords
# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))
# print(stop_words)

# # list of strings
# lst_strings = [no_wspace][0].split()
# print(lst_strings)

# no_stopwords = ""
# for i in lst_strings:
#     if i not in stop_words:
#         no_stopwords += i+' '

# # Removing last white space
# no_stopwords = no_stopwords[:-1]
# print(no_stopwords)

# Punctuation Removal

import re
import nltk
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer

# nltk.download('punkt')

# text = "This is a sample sentence, showing off the stop words filtration."

# tokens = word_tokenize(text)
# print(tokens)

# no_punc =[re.sub(r'[^\w\s]','',token) for token in tokens if re.sub(r'[^\w\s]','',token)]
# print(no_punc)

tokenizer = RegexpTokenizer(r'\w+')

text = "This is another example! Notice: it removes punctuation."
tokens = tokenizer.tokenize(text)
print(tokens)