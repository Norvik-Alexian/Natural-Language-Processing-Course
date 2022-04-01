import spacy

from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

# SolarPower
pattern1 = [{'LOWER': 'solarpower'}]

# Solar-power
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]

# Solar power
pattern3 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]

matcher.add('SolarPower', [pattern1, pattern2, pattern3])

doc = nlp(u"The Solar Power industry continues to grow as solarpower increases. Solar-power is amazing.")

found_matches = matcher(doc)

# print(found_matches)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] # get string representation
    span = doc[start: end]  # get the matched span
    # print(match_id, string_id, start, end, span.text)

matcher.remove('SolarPower')

# solarpower SolarPower
pattern1 = [{'LOWER': 'solarpower'}]

# solar.power
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LOWER': 'power'}]

matcher.add('SolarPower', [pattern1, pattern2])

doc2 = nlp(u"Solar--power is solarpower yay!")

found_matches = matcher(doc2)

# print(found_matches)

matcher = PhraseMatcher(nlp.vocab)

with open('UPDATED_NLP_COURSE/TextFiles/reaganomics.txt', encoding='utf-8', errors='ignore') as file:
    doc3 = nlp(file.read())

phrase_list = ['voodoo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']
phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('EconMatcher', [*phrase_patterns])
found_matches = matcher(doc3)

# print(found_matches)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]     # get string representation
    span = doc3[start:end]      # get the matched span
    print(match_id, string_id, start, end, span.text)
