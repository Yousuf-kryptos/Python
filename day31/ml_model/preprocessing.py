import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
 
df = pd.read_csv('adult.csv')
df.head()

df.replace("?", np.nan, inplace=True)      # Replace missing values with na
df.fillna(df.mode().iloc[0], inplace=True) # fill with most frequently occuring values

df.replace(['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 
            'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'],
            ['divorced','married','married','married','not married','not married', 'not married'], inplace=True)

category_col = ['workclass', 'race', 'education', 'marital-status', 'occupation',
                'relationship', 'gender', 'native-country', 'income']

label_encoder = preprocessing.LabelEncoder()

mapping_dict = {}

for col in category_col:
    df[col] = label_encoder.fit_transform(df[col]) # converting categories to numbers
    mapping_dict[col] = dict(enumerate(label_encoder.classes_)) # Store Mapping

print(mapping_dict)

df.drop(['fnlwgt', 'educational-num'], axis = 1, inplace=True) # Dropping unnecessary columns

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3,random_state=100)

dt_clf_gini = DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=5, min_samples_leaf=5)
dt_clf_gini.fit(X_train, y_train)

y_pred = dt_clf_gini.predict(X_test)
print("Accuracy: ",accuracy_score(y_test, y_pred))

with open("model.pkl","wb") as model_file:
    pickle.dump(dt_clf_gini, model_file)