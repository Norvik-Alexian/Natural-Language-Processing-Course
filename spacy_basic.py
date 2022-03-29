import spacy

# load small version of english core language library
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Tesla is looking at buying U.S startup for $6 million')

for token in doc:
    print(token.text, token.pos, token.pos_, token.dep_)

pipeline = nlp.pipeline

doc2 = nlp(u'Tesla is not into startups anymore')

for token in doc2:
    print(token.text, token.pos, token.pos_, token.dep_)

doc3 = doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
                    the phrase "Life is what happens to us while we are making other plans" was written by \
                    cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

# span example
life_quote = doc3[17:31]

print(type(doc3))
print(type(life_quote))

doc4 = nlp(u'This is the first sentence. This is the second sentence. This is the third sentence.')

for sentence in doc4.sents:
    print(sentence)

print(doc4[6].is_sent_start)
print(doc4[8].is_sent_start)