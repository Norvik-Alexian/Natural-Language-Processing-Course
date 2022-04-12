# Topic Modeling 
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

## Non-Negative Matrix Factorization
Non-negative Matrix Factorization is an unsupervised learning algorithm that simultaneously performs dimensionality reduction
and clustring.

* Input: Non-Negative data matrix(A), number of basis vectors(k), initial values for factors W and H.
* Objective Function: Some measure of reconstruction error between A and the approximation WH.
* Expectation: maximization optimisation to refine W and H in order to minimise the objective function. Common approach is to 
iterate between two multiplicative update rules convergence.
* Basis vectors: the topics (clusters) in the data.
* Coefficient matrix: the membership weights for documents relative to each topic (cluster).

This is how it works:
1. Construct vector space model for documents resulting in a term-document matrix A.
2. Apply TF-IDF term weight normalisation to A
3. Normalize TF-IDF vectors to unit length.
4. Initialise factors using NNDSVD on A.
5. Apply projected Gradient NMF to A.

Just like LDA, we will need to select the number of expected topics beforehand (the value of k). \
Also just like LDA, we will have to interpret the topics based off the coefficient values of the words per topic.
