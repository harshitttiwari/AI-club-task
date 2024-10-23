# -*- coding: utf-8 -*-
"""Problem Statement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pQQgbNtNXOdTmNCauccAspPGPTPYEr-8
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris() # loading the dataset
iris.data #Measurements of the Iris flowers
iris.target # It is the list of the names of the features in the datase
iris.target_names
iris.feature_names
iris # to show the data, target (Features)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)
print(x_train)
# print(x_train)
# print(x_train)
# print(x_train)

from sklearn.preprocessing import StandardScaler # using the feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train) # fitting the dataset
x_test = sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
rg=LogisticRegression(random_state=0)
rg.fit(x_train, y_train)

#  feature values
new_flower = np.array([[5.0, 3.5, 1.5, 0.2]])

# Standardize the features using the scaler
new_flower_scaled = sc.transform(new_flower)

# Make a prediction
predicted_class = rg.predict(new_flower_scaled)

# Print the predicted class
print(f"Predicted class: {iris.target_names[predicted_class][0]}")

y_pred = rg.predict(x_test) # Use the fitted Logistic Regression model (rg) for prediction
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))
"""0: Represents Iris setosa
1: Represents Iris versicolor
2: Represents Iris virginica"""

from sklearn.metrics import accuracy_score,confusion_matrix #we mainly use that to get the accuracy od the model
acc=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
print("Accuracy Score ",acc)
print("Classification Report\n",cm)

import seaborn as sns
# In that we are Create the heatmap
plt.figure(figsize=(8,6))
heatmap = sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')

#  Here we are Adding the  title and labels
plt.title('Confusion Matrix for Iris Flower Classification')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')

# Now we are adding the colorbar and its label
colorbar = heatmap.collections[0].colorbar
colorbar.set_label('Darker Blue = More Predictions\nLighter Blue = Fewer Predictions')

# PLoting
plt.show()