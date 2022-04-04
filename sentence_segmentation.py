import spacy

from spacy.language import Language
from spacy.pipeline import SentenceSegmenter

nlp = spacy.load("en_core_web_sm")

doc = nlp(u"This is the first sentence. This is another sentence. This is the last sentence.")

# for sent in doc.sents:
#     print(sent)

# print(type(list(doc.sents)[0]))

doc2 = nlp(u'"Manegment is doing the right things; leadership is doing the right things." - Peter Drucker')

# print(doc2.text)

# for sent in doc2.sents:
#     print(sent)
#     print('\n')


# Add segmentation rule:
@Language.component('component')
def set_custom_boundries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i + 1].is_sent_start = True
        # print(f'{token} - {token.i}')

    return doc

nlp.add_pipe('component', before='parser')

# print(nlp.pipe_names)

doc4 = nlp(u'"Manegment is doing the right things; leadership is doing the right things." - Peter Drucker')

# for sent in doc4.sents:
#     print(sent)


# Change the segmentation rule:
def split_on_newlines(doc):
    start = 0
    seen_newline = False

    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True

    yield doc[start:]

sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)

nlp.add_pipe(sbd)

doc = nlp(u"This is the first sentence. This is another sentence.\n\nThis is \nthe last sentence.")

for sentence in doc.sents:
    print(sentence)
