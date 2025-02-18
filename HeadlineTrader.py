# -*- coding: utf-8 -*-


import pandas as pd

df= pd.read_csv('Stock_Dataa.csv',encoding='ISO-8859-1')

df.head()

train= df[df['Date']<= '20091231' ]
test=  df[df['Date']> '20091231']

print(df.shape)
print(train.shape)
print(test.shape)

data= train.iloc[:,2:27]
data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)


list1=[i for i in range(25)]
new_Index=[str(i) for i in list1]
data.columns= new_Index
data.head()

for index in new_Index:
    data[index]=data[index].str.lower()
data.head()

' '.join(str(x) for x in data.iloc[1,0:25])

headlines=[]
for row in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))

headlines[0]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

countvector= CountVectorizer(ngram_range=(2,2),binary=True)
traindataset= countvector.fit_transform(headlines) 

traindataset[0]

random_classifier= RandomForestClassifier(n_estimators=120,criterion='gini',max_depth=25,min_samples_split=5)
random_classifier.fit(traindataset,train['Label'])

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= random_classifier.predict(test_dataset)

print(traindataset.shape)
print(test_dataset.shape)

predictions

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

predictions_train= random_classifier.predict(traindataset)
matrix= confusion_matrix(train["Label"],predictions_train)
print(matrix)
score= accuracy_score(train["Label"],predictions_train)
print(score)
report= classification_report(train['Label'],predictions_train)
print(report)

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

tfidf= TfidfVectorizer(ngram_range=(2,2))
traindataset= tfidf.fit_transform(headlines)

random_classifier= RandomForestClassifier(n_estimators=100,criterion='gini',max_depth=15)
random_classifier.fit(traindataset,train['Label'])

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= tfidf.transform(test_transform)
predictions= random_classifier.predict(test_dataset)

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

from sklearn.naive_bayes import GaussianNB
naive= GaussianNB()

countvector= CountVectorizer(ngram_range=(2,2))
traindataset= countvector.fit_transform(headlines)

naive.fit(traindataset,train['Label'])

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= naive.predict(test_dataset)

predictions

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)



traindataset= tfidf.fit_transform(headlines)

naive.fit(traindataset,train['Label'])

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= naive.predict(test_dataset)

predictions

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)
