import spacy

nlp = spacy.load('en_core_web_sm')

mystring = '"We\'re moving to L.A.!"'

doc = nlp(mystring)

for token in doc:
    print(token.text)

doc2 = nlp(u"We're here to help! Send Snail-mail, email support@oursite.com or visit us at https://www.google.com/!")

for token in doc2:
    print(token.text)

print(len(doc2))
print(len(doc2.vocab))

doc3 = nlp(u"Apple to build a Hong Kong factory for $6 million")

for token in doc3.ents:
    print(token)
    print(token.label_)
    print(str(spacy.explain(token.label_)), '\n')

doc4 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc4.noun_chunks:
    print(chunk)