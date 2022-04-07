import spacy

from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million."
          u"By contrast Sony only sold 8 thousand Walkman music players.")


options = {'ents': ['PRODUCT', 'ORG']}

for sent in doc.sents:
    displacy.serve(nlp(sent.text), style='ent', options=options)
