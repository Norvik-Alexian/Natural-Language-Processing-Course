import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"I am a runner running in a race because I love to run since I ran today")


def show_lemmas(text):
    for token in text:
        print(f"{token.text:{12}} {token.pos_:{6}} {token.lemma:<{12}} {token.lemma_}")


show_lemmas(doc)