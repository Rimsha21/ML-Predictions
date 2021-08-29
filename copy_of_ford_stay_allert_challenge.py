# -*- coding: utf-8 -*-
"""Copy of Ford Stay Allert Challenge

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mUJFRNZ41q5dcd3FuZRvVDigJ_7bvTtv
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from google.colab import files
files = files.upload()

import io

train = pd.read_csv(io.BytesIO(files['fordTrain.csv']))

train.head()

from google.colab import files
files = files.upload()

import io

test = pd.read_csv(io.BytesIO(files['fordTest.csv']))

test.head()

train.columns

train['IsAlert'].value_counts()

train.isnull().sum()

train.info()

train.describe()

corrmat= train.corr()
corrmat


# In[22]:


#plotting heatmap of correlation
plt.figure(figsize=(30,20))
sns.heatmap(corrmat, annot=True)
plt.show()

train['V7'].value_counts()

train.drop(['V7','V9','V11'], axis=1, inplace=True)

train.columns

train.drop('TrialID', axis=1, inplace=True)

from sklearn.model_selection import train_test_split

x = train.drop(['IsAlert'], axis='columns')

y=train['IsAlert']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


from sklearn.linear_model import LogisticRegression

#initiate the model

logreg=LogisticRegression()

#fit the model with data

logreg.fit(x_train,y_train)

#predicting y_test

y_pred=logreg.predict(x_test)

#import metrics class

from sklearn import metrics

cnf_matrix=metrics.confusion_matrix(y_test,y_pred)

cnf_matrix

metrics.precision_score(y_test,y_pred)
metrics.recall_score(y_test,y_pred)

#randomeforestclassifier

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier()
rfc.fit(x_train,y_train)


y_pred=rfc.predict(x_test)

cnf_matrix1=metrics.confusion_matrix(y_pred,y_test)
print(y_test.value_counts())
print(cnf_matrix1)

import seaborn as sns 
sns.heatmap(cnf_matrix1,annot=True,fmt="d")

metrics.f1_score(y_test,y_pred)

report=metrics.classification_report(y_test,y_pred)
print(report)

from sklearn import tree


clf=tree.DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
cnf_matrix1=metrics.confusion_matrix(y_pred,y_test)
print(metrics.classification_report(y_test,y_pred))

test=test.drop(columns=["TrialID","V7","V9","P8","IsAlert","ObsNum"])
test.head()
