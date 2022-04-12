# Semantics and Sentiment Analysis

## Sementics and Word Vectors
_**Word2vec**_ is a two-layer neural net that process the text. Its input is a text corpus and its output is a set of vectors:
feature vectors for words in that corpus. \
The purpose and usefulness of Word2vec is to group the vectors of similar words together in vectorspace. That is, it detects
similarities mathematically.

Word2vec creates vectors that are distributed numerical representations of word features, features such as the context of 
individual words. It does so without human intervention

Given enough data, usage and contexts, Word2vec can make highly accurate guesses about a word's meaning based on past 
appearances.

Word2vec trains words against other words that neighbour them in the input corpus. It does so in one of two ways, either 
using context to predict a target word known as continuous bag of words (CBOW), or using a word to predict a target context,
which is called skip-gram.

## Sentiment Analysis
VADER (Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to 
both polarity (positive/negative) and intensity (strength) of emotion.

Sentiment Analysis on raw text is always challenging however, due to variety of possible factors:
* Positive and Negative sentiment in the same text data.
* Sarcasm using positive words in a negative way.