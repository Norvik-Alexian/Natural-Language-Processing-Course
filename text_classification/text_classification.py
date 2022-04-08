import numpy as np
import pandas as pd

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews.tsv', sep='\t')

# print(df.head())
# print(len(df))
# print(df['review'][0])
# print(df.isnull().sum())

df.dropna(inplace=True)

# print(df.isnull().sum())
# print(len(df))

blanks = []

# (index, label, review text)
for i, lb, rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)

df.drop(blanks, inplace=True)

# print(len(df))

X = df['review']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

text_clf.fit(x_train, y_train)

prediction = text_clf.predict(x_test)

accuracy_check1 = confusion_matrix(y_test, prediction)
accuracy_check2 = classification_report(y_test, prediction)
accuracy_check3 = accuracy_score(y_test, prediction)

print(accuracy_check3)