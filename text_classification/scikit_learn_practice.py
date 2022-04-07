import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn.svm import SVC
from sklearn import metrics
# from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data_file = pd.read_csv('../../UPDATED_NLP_COURSE/TextFiles/smsspamcollection.tsv', sep='\t')

# print(data_file.head())   # show the first 5 rows
# print(data_file.isnull().sum())   # show empty values in the dataset
# print(len(data_file))     # length of the dataset
# print(data_file['label'].unique())    # unique values of label column
# print(data_file['label'].value_counts())  # amount of unique values in the dataset

plt.xscale('log')
bins = 1.15 ** (np.arange(0, 50))
plt.hist(data_file[data_file['label'] == 'ham']['length'], bins=bins, alpha=0.8)
plt.hist(data_file[data_file['label'] == 'spam']['length'], bins=bins, alpha=0.8)
plt.legend(('ham', 'spam'))
plt.show()

# X feature data
X = data_file[['length', 'punct']]

# y is our label
y = data_file['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# print(x_train.shape)
# print(x_test.shape)

logistic_regression_model = LogisticRegression(solver='lbfgs')

logistic_regression_model.fit(x_train, y_train)
predictions = logistic_regression_model.predict(x_test)

# print(predictions)
# print(metrics.confusion_matrix(y_test, predictions))

# show the accuracy of the model using confusion matrix
dataframe = pd.DataFrame(metrics.confusion_matrix(y_test, predictions), index=['ham', 'spam'], columns=['ham', 'spam'])

# print(dataframe)

# show the accuracy of the model using classification report
accuracy = metrics.classification_report(y_test, predictions)

