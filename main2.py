import numpy as np
import streamlit as st
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

st.header('MACHINE LEARNING 20-22 Aug 2024 - Regression')
st.write('😊 by Nattacha S.')

fig,ax=subplots()
ax.scatter(x,y)
ax.scatter(x,y_pred)
st.pyplot(fig)

x=4*np.random.rand(100)
y=np.sin(2*x + 1) +0.1*np.random.randn(100)

st.sidebar.title('Classifiers')
classifier = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM','Decision Tree', 'Random Forest', 'Neural Network'))


if classifier == 'KNN':
  knn = KNeighborsRegressor(n_neighbors=5)
  knn.fit(x.reshape(-1,1), y)
  y_pred = knn.predict(x.reshape(-1,1))
  plt.scatter(x, y)
  plt.scatter(x, y_pred)

if classifier == 'SVM':
  svm = SVR()
  svm.fit(x.reshape(-1,1), y)
  y_pred = svm.predict(x.reshape(-1,1))
  plt.scatter(x, y)
  plt.scatter(x, y_pred)


if classifier == 'Decision Tree':
  dt = DecisionTreeRegressor()
  dt.fit(x.reshape(-1,1), y)
  y_pred = dt.predict(x.reshape(-1,1))
  plt.scatter(x, y)
  plt.scatter(x, y_pred)

if classifier == 'Neural Network':
  nn = MLPRegressor()
  nn.fit(x.reshape(-1,1), y)
  y_pred = nn.predict(x.reshape(-1,1))
  plt.scatter(x, y)
  plt.scatter(x, y_pred)

if classifier == 'Random Forest':
  rf = RandomForestRegressor()
  rf.fit(x.reshape(-1,1), y)
  y_pred = rf.predict(x.reshape(-1,1))
  plt.scatter(x, y)
  plt.scatter(x, y_pred)
