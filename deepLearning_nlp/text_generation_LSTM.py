import spacy
import random
import numpy as np

from pickle import dump, load
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, LSTM, Embedding
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

# for i in sequences[0]:
#     print(f'{i}: {tokenizer.index_word[i]}')

# print(tokenizer.word_counts)    # counts how many times the token showed up in the text

vocabulary_size = len(tokenizer.word_counts)

# print(vocabulary_size)

sequences = np.array(sequences)

X = sequences[:, :-1]
y = sequences[:, -1]

y = to_categorical(y, num_classes=vocabulary_size+1)
seq_len = X.shape[1]

# print(X.shape)


def create_model(vocabulary_size: int, seq_len: int):
    model = Sequential()
    model.add(Embedding(vocabulary_size, seq_len, input_length=seq_len))
    model.add(LSTM(150, return_sequences=True))
    model.add(LSTM(150))
    model.add(Dense(150, activation='relu'))
    model.add(Dense(vocabulary_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.summary()

    return model

model = create_model(vocabulary_size+1, seq_len)

# model.fit(X, y, batch_size=128, epochs=5, verbose=1)
# model.save('./models/text_generator_model.h5')

# dump(tokenizer, open('tokenizer/my_simpleTokenizer', mode='wb'))


def generate_text(model, tokenizer, seq_len, seed_text, num_gen_word):
    output_text = []
    input_text = seed_text

    for i in range(num_gen_word):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')
        pred_word_ind = model.predict_classes(pad_encoded, verbose=0)[0]
        pred_word = tokenizer.index_word[pred_word_ind]
        input_text += ' ' + pred_word
        output_text.append(pred_word)

    return ' '.join(output_text)

random.seed(101)
random_pick = random.randint(0, len(text_sequence))
random_seed_text = text_sequence[random_pick]

model = load_model('./models/text_generator_model.h5')
tokenizer = load(open('./tokenizer/my_simpleTokenizer', 'rb'))
seed_text = ' '.join(random_seed_text)

generated_text = generate_text(model, tokenizer, seq_len, seed_text, num_gen_word=25)
