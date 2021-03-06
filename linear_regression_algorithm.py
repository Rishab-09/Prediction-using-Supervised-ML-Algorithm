# -*- coding: utf-8 -*-
"""Linear_Regression_Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10n4JAeL-kiIJlV3XC2_wBie8FH0bskhJ

<center><h1>The Spark Foundation

<center><h2>Predict the percentage of an student based on the no. of study hours.

<h3>ML Algorithm = Simple Linear Regression
<h3>Problem To Be Solved = What will be predicted score if a student studies for 9.25 hrs/ day?
"""

#importing all the libraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#importing and reaading the dataset
dataset = pd.read_csv("student_scores.csv")

#the first five values in the dataset
dataset.head()

#number of rows and columns
dataset.shape

dataset.describe()

dataset.info()

"""<h2>Visualization Of Data"""

#Hours Vs Percentage of Scores
plt.figure(figsize=(10,6))
plt.scatter(dataset['Hours'], dataset['Scores'], c='black')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.show()

plt.figure(figsize=(10,6))
plt.bar(dataset['Hours'], dataset['Scores'], color='blue')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')

plt.figure(figsize=(15,6))
sns.barplot(x='Hours', y='Scores', data=dataset)

plt.figure(figsize=(10,6))
sns.lineplot(data=dataset)

"""<h2>Train-Test separation of data"""

#X will take all the values except for the last column which is our dependent variable (target variable)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_

# Plotting for the test data
plt.figure(figsize=(10,6))
plt.scatter(X, y, c='coral')
plt.plot(X, line,c = 'black');
plt.show()

#Visualising the Training set results
plt.figure(figsize=(10,6))
plt.scatter(X_train, y_train, c='blue')
plt.plot(X_train, regressor.predict(X_train), c='black')
plt.title('Hours vs. Percentage (Training set)')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage')
plt.show()

#Predicting the Test set results

y_pred = regressor.predict(X_test)
print(y_pred)

#Visualising the Test set results
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'black')
plt.title('Hours vs. Percentage (Test set)')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage')
plt.show()

#Comparing the actual values with the predicted ones.
ds = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
ds

plt.figure(figsize=(8,5))
sns.heatmap(ds.corr())

"""<h2>Predicting the score if the student studies for 9.25 hours/day"""

dataset = np.array(9.25)
dataset = dataset.reshape(-1, 1)
pred = regressor.predict(dataset)
print("If the student studies for 9.25 hours/day, the score is {}.".format(pred))

"""<h2>Check the predicting score if the student studies for 6 hours/day"""

dataset = np.array(6)
dataset = dataset.reshape(-1, 1)
pred = regressor.predict(dataset)
print("If the student studies for 6 hours/day, the score is {}.".format(pred))

"""## Conclusion:
### We used a Linear Regression Model to predict the score of a student if he/she studies for 9.25 hours/day and the Predicted Score came out to be 92.91.
"""