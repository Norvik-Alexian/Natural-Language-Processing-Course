import spacy

from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

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

# show_ents(doc3)

# Adding new entity
ORG = doc.vocab.strings[u"ORG"]
new_ent = Span(doc3, 0, 1, label=ORG)
doc3.ents = list(doc3.ents) + [new_ent]

# show_ents(doc3)

doc4 = nlp(u"Our company created a brand new vaccum cleaner."
           u"This new vaccum-cleaner is the best in show.")

# show_ents(doc4)

matcher = PhraseMatcher(nlp.vocab)
phrase_list = ['vaccum cleaner', 'vaccum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('newproduct', [*phrase_patterns])
found_matches = matcher(doc4)

# print(found_matches)

PROD = doc4.vocab.strings[u'PRODUCT']
new_ents = [Span(doc4, match[1], match[2], label=PROD) for match in found_matches]
doc4.ents = list(doc4.ents) + new_ents

# show_ents(doc4)

doc5 = nlp(u"Originally I paid $29.95 for this car toy, but now it is mark down for 10 dollars.")

print(len([ent for ent in doc5.ents if ent.label_ == 'MONEY']))