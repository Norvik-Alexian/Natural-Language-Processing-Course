import spacy

nlp = spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))

print(nlp.vocab['mystery'].is_stop) # check if token is stop word

nlp.Defaults.stop_words.add('btw')  # add custome word to the stop words set
nlp.vocab['btw'].is_stop = True

print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))

nlp.Defaults.stop_words.remove('somewhere') # remove token from stop word set
nlp.vocab['somewhere'].is_stop = False

print(nlp.Defaults.stop_words)

