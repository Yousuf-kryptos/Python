# import gensim

# print(gensim.__version__)

# import gensim.downloader as api

# info_datasets = api.info()

# print(info_datasets)
# dataset_info = api.info("text8")
# dataset = api.load("text8")
# word2vec_model = api.load('word2vec-google-news-300')

# Preprocess the Dataset

# Text Preprocessing

import gensim
import os
from gensim.utils import simple_preprocess
from gensim import corpora

doc = open("sample_data.txt",encoding= "utf-8")
tokenized = []
for sentence in doc.read().split('.'):
    tokenized.append(simple_preprocess(sentence,deacc=True))
print(tokenized)

# Creating dictionary using preprocessed data
my_dict = corpora.Dictionary(tokenized)
print(my_dict)

my_dict.save("my_dict.dict")
load_dict = corpora.Dictionary.load('my_dict.dict')

from gensim.test.utils import get_tmpfile

tmp_fname = get_tmpfile("dictionary")
my_dict.save_as_text(tmp_fname)
load_dict = corpora.Dictionary.load_from_text(tmp_fname)