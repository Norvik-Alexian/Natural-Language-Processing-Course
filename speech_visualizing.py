import spacy

from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

displacy.render(doc, style='dep', jupyter=False)

options = {'distance': 110, 'compact': 'True', 'color': 'blue', 'bg': 'lightblue', 'font': 'Times'}
# displacy.serve(doc, style='dep', options=options)

doc2 = nlp(u"This is a sentence. This is another sentence, possibly longer than the other.")

spans = list(doc2.sents)

displacy.serve(spans, style='dep', options=options)