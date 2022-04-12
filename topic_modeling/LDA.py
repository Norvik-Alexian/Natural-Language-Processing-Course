import random
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

npr = pd.read_csv('../UPDATED_NLP_COURSE/05-Topic-Modeling/npr.csv')

# print(npr.head())
# print(npr['Article'][0])
# print(len(npr))

cv = CountVectorizer(max_df=0.9, min_df=2, stop_words='english')

dtm = cv.fit_transform(npr['Article'])

LDA = LatentDirichletAllocation(n_components=7, random_state=42)

LDA.fit(dtm)

# Grab the vocabulary of words:
# print(len(cv.get_feature_names_out()))
# print(cv.get_feature_names_out()[50000])

random_word_id = random.randint(0, 54777)
# print(cv.get_feature_names_out()[random_word_id])

# Grab the topics:
# print(LDA.n_components)
# print(type(LDA.n_components))

topic_results = LDA.transform(dtm)

# print(topic_results[0].argmax())

npr['topic'] = topic_results.argmax(axis=1)

# print(npr)