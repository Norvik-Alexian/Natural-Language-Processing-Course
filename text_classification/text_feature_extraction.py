import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/smsspamcollection.tsv', sep='\t')

# print(df.head())
# print(df.isnull().sum())

df['label'].value_counts()

X = df['message']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

count_vect = CountVectorizer()

# fit the vectorizer to the data:
# count_vect.fit(x_train)
# x_train_count = count_vect.transform(x_train)
x_train_counts = count_vect.fit_transform(x_train)

# Transform the original text message to vector:
