import spacy
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer


def read_file(filepath: str):
    with open(filepath) as file:
        str_text = file.read()

    return str_text

# print(read_file('files/moby_dick_four_chapters.txt'))

nlp = spacy.load('en_core_web_sm', disable=['parser', 'tagger', 'ner'])

nlp.max_length = 1198623


def separate_punctuation(doc_text: str):
    """
    :param doc_text: raw text
    :return: list of tokens without any punctations.
    """
    return [token.text.lower() for token in nlp(doc_text) if token.text not in '\n\n \n\n\n!"-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n ']


doc = read_file('files/moby_dick_four_chapters.txt')
tokens = separate_punctuation(doc)

# print(len(tokens))

train_len = 25 + 1
text_sequence = []

for i in range(train_len, len(tokens)):
    seq = tokens[i - train_len: i]
    text_sequence.append(seq)

# print(type(text_sequence))
# print(text_sequence[0])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_sequence)

sequences = tokenizer.texts_to_sequences(text_sequence)

# print(sequences[1])
# print(tokenizer.index_word)

for i in sequences[0]:
    print(f'{i}: {tokenizer.index_word[i]}')

# print(tokenizer.word_counts)    # counts how many times the token showed up in the text

vocabulary_size = len(tokenizer.word_counts)

# print(vocabulary_size)

sequences = np.array(sequences)

print(sequences)