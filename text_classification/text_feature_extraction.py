import numpy as np
import pandas as pd

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

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

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

# print(x_train_tfidf.shape)

vectorizer = TfidfVectorizer()
x_train_tfidf = vectorizer.fit_transform(x_train)

clf = LinearSVC()
clf.fit(x_train_tfidf, y_train)

text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

text_clf.fit(x_train, y_train)

predictins = text_clf.predict(x_test)
accuracy = confusion_matrix(y_test, predictins)

# print(accuracy)

accuracy = classification_report(y_test, predictins)

# print(accuracy)

accuracy = accuracy_score(y_test, predictins)

print(accuracy)
