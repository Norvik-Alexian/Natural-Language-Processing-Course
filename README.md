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

## What is NLP?
_Natural Language Processing_ is an area of computer science and artificial intelligence concerned with interactions
between computers and human (natural) languages, in particular how to program computers to process and analyze large 
amount of natural language data.

## Tokenization
Tokenization is the process of breaking up the original text into component pieces (tokens).\
Tokens are the basic building blocks of a Doc object - everything that helps us understand the meaning of the text is
derived from tokens and their relationship to one another.

* `prefix`: characters at the beginning.
* `suffix`: characters at the end.
* `Infix`: characters in between.
* `Exception`: Special-case rule to split a string into several tokens or prevent a token from being split when punctuation
rules are applied.

## References
[Spacy usage fact figures](https://spacy.io/usage/facts-figures) \
[SRF time code](https://strftime.org/) \
[Spacy Visualizers](https://spacy.io/usage/visualizers)