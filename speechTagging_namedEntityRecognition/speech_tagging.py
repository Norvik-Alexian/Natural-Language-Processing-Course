import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

# for token in doc:
#     print(f'{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}')

doc = nlp(u"I read books on NLP")

word = doc[1]

token = word
# print(f'{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}')

doc = nlp(u"I read a book on NLP.")

word = doc[1]

token = word
# print(f'{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}')

doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

POS_count = doc.count_by(spacy.attrs.POS)

# print(POS_count)

# for k, v in sorted(POS_count.items(),):
#     print(f"{k}. {doc.vocab[k].text:{5}} {v}")

TAG_count = doc.count_by(spacy.attrs.TAG)

# for k, v in sorted(TAG_count.items(),):
#     print(f"{k}. {doc.vocab[k].text:{5}} {v}")

print(len(doc.vocab))