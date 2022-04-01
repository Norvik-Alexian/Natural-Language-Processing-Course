import spacy

from spacy.tokens import Span

nlp = spacy.load('en_core_web_sm')


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(f'{ent.text} - {ent.label_} {spacy.explain(ent.label_)}')
    else:
        print('No entities found.')


doc = nlp(u"Hi how are you?")
doc2 = nlp(u"May I go to Washington DC next May to see Washington Monument?")
doc3 = nlp(u"Tesla to build U.K. factory for $6 million")

show_ents(doc3)

# Adding new entity
ORG = doc.vocab.strings[u"ORG"]
new_ent = Span(doc3, 0, 1, label=ORG)
doc3.ents = list(doc3.ents) + [new_ent]

show_ents(doc3)