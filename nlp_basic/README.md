# Natural Language Processing Basics

## What is Spacy?
* Open Source Natural Language Processing Library
* Designed to effectively handle NLP tasks with the most efficient implementation of common algorithms.

## Spacy basics
* Spacy works with Pipeline object.
* the `nlp()` function from Spacy automatically takes raw text and performs a series of operations to tag, parse,
and describe the text data.
* To download the "en_core_web_sm" model from spacy we need to run `python -m spacy download en_core_web_sm` command
in our terminal.
* The very first step in processing any text is to split up all the component parts, that is the word and punctuation into
tokens, and these tokens are annotated inside the dock object to contain descriptive information.
* `span`: span is a slice of a stock object in the form some start vs stop.

## What is NLTK?
NLTK - Natural Language Toolkit is a very popular open source. It also provides many functionalities, but includes less
efficient implementations.

## NLTK vs Spacy
For many common NLP tasks, Spacy is much faster and more efficient, at the cost of the user not being able to choose 
algorithmic implementations.

However, Spacy does not include pre-created models for some applications, such as sentiment analysis, which is typically 
easier to perform with NLTK.

## Tokenization
Tokenization is the process of breaking up the original text into component pieces (tokens).\
Tokens are the basic building blocks of a Doc object - everything that helps us understand the meaning of the text is
derived from tokens and their relationship to one another.

* `prefix`: characters at the beginning.
* `suffix`: characters at the end.
* `Infix`: characters in between.
* `Exception`: Special-case rule to split a string into several tokens or prevent a token from being split when punctuation
rules are applied.

## Steamming
Stemming is a somewhat crude method for cataloging related words, it essentially chops off letters from the end until
the stem is reached. This works fairly well in most cases, but unfortunatly English has many exceptions where a more
sophisticated process is required.

One of the most common and effective stemming tools is `Porter's Algorithm`. The algorithm employs five phases of word
reduction, each with its own set of mapping rules. \
In the first phase, simple suffix mapping rules are defined.

Snowball is the name of a stemming language also developed by Martin Porter. The algorithm used here is more accurately
called the "English Stemmer" or "Porter2 Stemmer". It offers a slight imporvment over the original Porter Stemmer, both 
in logic and speed.

## Lemmatization
In contrast to stemming, lemmatization looks beyond word reduction, and considers as language's full vocabulary to apply
a morphological analysis to words. \
The lemma of 'was' is 'be' and the lemma of 'mice' is 'mouse'.

Lemmatization is typically seen as much more informative than simple stemming, which is why Spacy has opted to only have 
Lemmatization available instead of Stemming.

Lemmatization looks at surrounding text to determine a given word's part of speech, it does not categorize phrases.

## Stop Words
Words like "a" and "the" appear so frequently that they don't require tagging as thoroughly as nouns, verbs and modifiers.
We call these `stop words`, and they can be filtered from the text to be processed. \
Spacy holds a built-in list of some 326 English stop words.

## Vocabulary and Matching
We can think of this as a powerful version of Regular Expression where we actually take parts of speech into account for
our pattern search.
