# Part of Speech Tagging and Named Entity Recognition

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
