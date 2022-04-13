import numpy as np

from sklearn.datasets import load_iris
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

iris = load_iris()

# print(type(iris))
# print(iris.DESCR)   # Description of the dataset.

X = iris.data
y = iris.target

y = to_categorical(y)

# print(y)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

scaler_object = MinMaxScaler()

scaler_object.fit(x_train)

scaled_X_train = scaler_object.transform(x_train)
scaled_X_test = scaler_object.transform(x_test)

# print(scaled_X_train)

model = Sequential()

model.add(Dense(8, input_dim=4, activation='relu',))
model.add(Dense(8, input_dim=4, activation='relu',))
model.add(Dense(3, activation='softmax',))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

model.fit(scaled_X_train, y_train, epochs=150, verbose=2)

prediction = model.predict(scaled_X_test)
classes_X = y_test.argmax(axis=1)

# print(classes_X)

model.save('./models/keras_model.h5')

my_model = load_model('./models/keras_model.h5')

accuracy1 = classification_report(y_test.argmax(axis=1), prediction)
accuracy2 = confusion_matrix(y_test.argmax(axis=1), prediction)
accuracy3 = accuracy_score(y_test.argmax(axis=1), prediction)
