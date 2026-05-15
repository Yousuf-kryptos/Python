# Term Frequency - Inverse Document Frequency (TF-IDF)

from sklearn.feature_extraction.text import TfidfVectorizer

# Collect strings from documents and create a corpus
d0 = 'Geeks for geeks'
d1 = 'Geeks'
d2 = 'r2j'
string = [d0, d1, d2]

# Get TF-IDF Values

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(string)

# Display IDF Values
print('\nIDF Values:')

for ele1,ele2 in zip(tfidf.get_feature_names_out(),tfidf.idf_):
    print(ele1, ':', ele2)

print("\nWord Indexes:\n")
print(tfidf.vocabulary_)
print("\nTf-IDF values:")
print(result)
print("\n TF-IDF values in matrix form:")
print(result.toarray())