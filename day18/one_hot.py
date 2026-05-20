import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    'Employee id': [10, 20, 15, 25, 30],
    'Gender': ['M', 'F', 'F', 'M', 'F'],
    'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice']
}

# Using Pandas

df = pd.DataFrame(data)
print(f"Original Data:\n{df}\n")

df_pandas_encoded = pd.get_dummies(df,columns=['Gender','Remarks'],drop_first=True)
print(f"One-hot Encoded data using Pandas:\n{df_pandas_encoded}\n")

# Using Scikit Learn
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
encoder = OneHotEncoder(sparse_output=False)

one_hot_encoded = encoder.fit_transform(df[categorical_columns])
one_hot_df = pd.DataFrame(one_hot_encoded,columns=encoder.get_feature_names_out(categorical_columns))

df_encoded = pd.concat([df,one_hot_df],axis=1)
df_encoded = df_encoded.drop(categorical_columns,axis=1)

print(f"One-Hot Encoded Data using Scikit Learn:\n{df_encoded}\n")