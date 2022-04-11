import spacy

from scipy import spatial

nlp = spacy.load('en_core_web_lg')

doc = nlp(u"lion").vector.shape

tokens = nlp(u"lion cat pet")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# print(nlp.vocab.vectors.shape)

tokens = nlp(u"dog cat nargle")

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)

cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)

king = nlp.vocab['king'].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector

# king - man + woman --> NEW_VECTOR similar queen, princess, highness
new_vector = king - man + woman

computed_similarities = []

# For all words in my vocab
for word in nlp.vocab:
    if word.has_vector and word.is_lower and word.is_alpha:
        similarity = cosine_similarity(new_vector, word.vector)
        computed_similarities.append((word, similarity))

computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])

print([item[0].text for item in computed_similarities[:10]])
