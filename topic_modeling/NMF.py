import pandas as pd

from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

npr = pd.read_csv('../UPDATED_NLP_COURSE/05-Topic-Modeling/npr.csv')

# print(npr.head())

tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = tfidf.fit_transform(npr['Article'])

nmf_model = NMF(n_components=7, random_state=42)

nmf_model.fit(dtm)

# print(tfidf.get_feature_names_out()[2300])

for index, topic in enumerate(nmf_model.components_, ):
    print(f'The top 15 words for topic # {index}')
    print(tfidf.get_feature_names_out()[i] for i in topic.argsort()[-15:])

topic_results = nmf_model.transform(dtm)

print(topic_results.argmax(axis=1))

npr['Topic'] = topic_results.argmax(axis=1)
mytopic_dict = {0: 'health', 1: 'election', 2: 'legis', 3: 'poli', 4: 'election', 5: 'music', 6: 'education'}
npr['Topic Labels'] = npr['Topic'].map(mytopic_dict)

print(npr.head())
