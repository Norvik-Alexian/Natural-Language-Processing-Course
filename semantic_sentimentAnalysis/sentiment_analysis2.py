import numpy as np
import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews.tsv', sep='\t')

# print(df.head())
# print(df.isnull().sum())

df.dropna(inplace=True)

blanks = []
for i, lb, rv in df.itertuples():
    if type(rv) == str and rv.isspace():
        blanks.append(i)

# print(blanks)

df.drop(blanks, inplace=True)

# print(df['label'].value_counts())

sid = SentimentIntensityAnalyzer()

df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
df['compound'] = df['scores'].apply(lambda d: d['compound'])
df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')

# print(df.head())

accuracy = accuracy_score(df['label'], df['comp_score'])
accuracy2 = classification_report(df['label'], df['comp_score'])
accuracy3 = confusion_matrix(df['lablel'], df['comp_score'])

print(accuracy)