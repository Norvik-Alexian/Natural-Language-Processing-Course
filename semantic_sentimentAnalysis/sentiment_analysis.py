import nltk
import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

doc = 'This is a good movie'
# print(sid.polarity_scores(doc))

doc2 = 'This was the best, most awesome movie EVER MADE!!'
# print(sid.polarity_scores(doc2))

doc3 = 'This was the WORST movie that has ever disgraced the screen'
# print(sid.polarity_scores(doc3))

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/amazonreviews.tsv', sep='\t')

# print(df.head())
# print(df['label'].value_counts())
# print(df.isnull().sum())

print(sid.polarity_scores(df.iloc[0]['review']))

# Add new columns to the dataset
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
df['compound'] = df['scores'].apply(lambda d: d['compound'])
df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')

print(df.head())

accuracy = accuracy_score(df['label'], df['comp_score'])
accuracy_2 = classification_report(df['label'], df['comp_score'])
accuracy_3 = confusion_matrix(df['label'], df['comp_score'])

print(accuracy_3)