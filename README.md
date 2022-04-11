## What is NLP?
_Natural Language Processing_ is an area of computer science and artificial intelligence concerned with interactions
between computers and human (natural) languages, in particular how to program computers to process and analyze large 
amount of natural language data.

## Python File Modes
* `r` - opens a file for reading. (default)
* `w` - opens a file for writing. creates a new file if it does not exist or truncates the file if it exits.
* `x` - opens a file for exclusive creation. If the file already exists, the operation fails.
* `a` - opens a file for appending at the end of the file without truncating it, creates a new file if it does not exist
* `t` - opens in text mode. (default)
* `b` - opens in binary mode.
* `+` - opens a file for updating (reading and writing)

## Working with PDF files
* We can use the `PyPDF2` library to read in text data from a PDF file.
* Some PDFs are created through scanning, instead of being exported from a text editor like Word
* These scanned PDF are more like image files, making it much harder to extract the text.

## Identifiers and Characters in Patterns in Regular Expressions
Characters such as a digit or a single string have different codes that represent them. You can use these to build up a 
pattern string. Notice how these make heavy use of the backwards slash \ . Because of this when defining a pattern string
for regular expression we use the format `r"mypattern"`. Placing the `r` in front of the string allows python to understand
that the `\` in the pattern string are not meant to be escape slashes.

* \d - a digit
* \w - alphanumeric
* \s - White space
* \D - a non digit
* \W - non-alphanumeric
* \S - non-whitespace
* `+` - Occurs one or more time
* {3} - Occurs exactly 3 times
* {2, 4} - Occurs 2 to 4 times
* {3,} - Occurs 3 or more
* \* - Occurs zero or more times
* ? - Once or none

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

## Part of Speech Tagging (POS)
After Tokenization, spacy can **parse** and **tag** a given `Doc` object. This is where the trained pipeline and its
statistical models come in, which enable spacy to **make predictions** of which tag or label most likely applies in this 
context. A trained component includes binary data that is produced by showing a system enough examples for it to make
predictions that generalize across the language, for example, a word following "the" in English is most likely a noun.

## Named Entity Recognition
Named-entity recognition (NER) seeks to locate and classify named entity mentions in unstructured text into pre-defined 
categories such as the person names, organizations, locations, medical codes, time expressions, quantities, monetary values,
percentages, etc.

## Sentence Segmentation
A `Doc` object's sentences are available via the `Doc.sents` property. To view a `Doc`'s sentences, you can iterate over 
the `Doc.sents`, a generator that yields `Span` objects. We can also check whether a `Doc` has sentence boundaries by calling
`Doc.has_annotation` with the attribute name "SENT_START".

## Machine Learning Overview
Machine Learning is a method of data analysis that automates analytical model building. \
Using algorithms that iteratively learn from data, machine learning allows computers to find hidden insights without being 
explicitly programmed where to look. \
Supervised learning algorithms are trained using labeled examples, such as an input where the desired output is known. \
The learning algorithm receives a set of inputs along with the corresponding correct outputs, and the algorithm learns by 
comparing its actual output with correct outputs to find errors. It then modifies the model accordingly. \
Supervised learning is commonly used in applications where historical data predicts likely future events.

### Machine Learning Process:
1. `Data Acquisition`: get your data, Customers, Sensors and etc.
2. `Data Cleaning`: Clean and Format your data using Scikit Learn and Vectorization.
3. `Test Data & Training Data`: on Training data we are going to have the model to learn from training data, or we can call 
fitting the model and on Test data we are going to take the model that we are training and test it against the test data.
4. `Model Deployment`

## Classification Matrics
The key classification metrics we need to understand are:
* Accuracy
* Recall
* Precision
* F1-Score

Typically, in any classification task your model can only achieve two results:
1. Either your model was **correct** in its prediction.
2. Or your model was **incorrect** in its prediction.

Fortunately incorrect vs correct expands to situation where you have multiple classes. \
We repeat the process of Model Evaluation for all the texts in our x test data. At the end we will have a count of correct
matches and a count of incorrect matches. The key realization we need to make, is that in the real world, not all incorrect
or correct matches hold equal value.

### Accuracy:
* Accuracy in classification problem is the number of correct predictions made by the model divided by the total number of 
predictions.
* Accuracy is useful when target classes are well-balanced.
* Accuracy is not a good choice with unbalanced classes.

### Recall:
Ability of a model to find all the relevent cases within a dataset. \
The precise definition of recall is the number of true positive divided by the number of true positive plus the number of
false negatives.

### Precision:
Ability of classification model to identify only the relevent data points. Precision is defined as the number of true
positives, divided by the number of true plus the number of false positives.

### Recall & Precision:
While recall expresses the ability to find all relevant instances in a dataset, precision expresses the proportion of the
data points our model says was relevant actually were relevant.

### F1-Score:
In case where we want to find an optimal blend of precision and recall we can combine the two matrices using what is called
the F1-Score. \
The F1 score is the hormonic mean of precision and recall taking both matrices into account in the following equation

`F1 = 2 * precision * recall / precision + recall`

The reason that we are using hormonic mean instead of simple average because it punishes extreme values. \
A classifier with a precision of 1.0 and a recall of 0.0 has simple average of 0.5 but an F1 score of 0.

## Confusion Matrix
A way to view various metrics of classification is the confusion Matrix. \
In a classification problem, during the testing phase you will have two categories:
1. True Condition
2. Predicted Condition

The main point to remember with the confusion matrix and the various calculated matrices is that they are all fundamentally 
ways of camparing the predicted values vs the true values. We can use a confusion matrix to evaluate our model. 

Basic Terminology:
* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

Accuracy: (TP + TN) / total \
Misclassification/Error rate: (FP + FN) / total

## Scikit-Learn
`Estimator parameters`: All the parameters of an estimator(model) can be set when it is instantiated, and have suitable 
default values. \
Once we have our model created with our parameters, it is time to fit our model on some data, but we should split this data
into training set and testing set. \
Now the model has been fit and trained on the training dataset, the model is ready to predict lables or values on the
testing set.

## Text Feature Extraction
Most classic machine learning algorithms can't take in raw text, instad we need to perform a feature "extraction" from the 
raw text in order to pass numerical features to the machine learning algorithm.

* `Term frequency tf(t, d)`: is the raw count of a term in a document, i.e. the number of times that term t occurs in 
document d. However, Term frequency alone isn't enough for a thorough feature analysis of the text.

An inverse document frequency factor is incorprated which diminishes the weight of terms that occur very frequently in
the document set and increases the weight of terms that occur rarely.

* `TF-IDF = term frequency * (1 / document frequency)`
* `TF-IDF = term frequency * inverse document frequency`

TF-IDF allows us to understand the context of words across an entire of documents, instead of just its relative importance 
in a single document.

### Count Vectorization:
It is used to transform a given text into a vector on the basis of frequency of each word that occurs in the entire text.

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

## Topic Modeling 
Topic Modeling allows us to efficiently analyze large volumes of text by clustring documents into topics.

## Latent Dirichlet Allocation (LDA)
Assumptions of LDA for topic modeling:
* Documents with similar topics use similar groups of words.
* Latent topics can then be found by searching for groups of words that frequently occur together in documents across the 
corpus.
* Documents are probability distributions over latent topics
* Topics themselves are probability distributions over words.

Documents are probability distributions over latent topics. \
Topic themselves are probability distributions over words. \
LDA represents documents as mixture of topics that spit out words with certain probabilities.

It assumes that documents are produced in the following fashion:
* Decide one the number of words N the document will have.
* Choose a topic mixture of the document 

Two important notes:
1. The user must decide on the amount of topics present in the document.
2. The user must interpret what the topics are.

## References
[Spacy usage fact figures](https://spacy.io/usage/facts-figures) \
[SRF time code](https://strftime.org/) \
[Spacy Visualizers](https://spacy.io/usage/visualizers)