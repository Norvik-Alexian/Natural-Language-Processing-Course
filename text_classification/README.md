# Text Classification

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