# -*- coding: utf-8 -*-
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
import numpy.random as npr
import statsmodels.api as sm

bank=pd.read_csv('bank_notes.csv')
aup=bank.forged.value_counts()[0]/bank.shape[0]
#Ans:0.5553935860058309

bank_std=(bank-bank.mean())/bank.std()
X=bank_std.drop('forged',axis=1)
y=bank.forged
maxindex=X.corrwith(y).idxmax()
#'kurtosis'

X.insert(0,'intercept',1)
train_size = 1000
np.random.seed(123)
train_select = np.random.permutation(range(len(y)))
X_train = X.iloc[train_select[:train_size],:].reset_index(drop=True)
X_test = X.iloc[train_select[train_size:],:].reset_index(drop=True)
y_train = y[train_select[:train_size]].reset_index(drop=True)
y_test = y[train_select[train_size:]].reset_index(drop=True)

logit1 = sm.Logit(y_train,X_train.variance).fit()
logit2 = sm.Logit(y_train,X_train.skewness).fit()
logit3 = sm.Logit(y_train,X_train['kurtosis']).fit()
logit4 = sm.Logit(y_train,X_train.entropy).fit()
# entropy seems to be the most important variable;

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train) 

logreg_test_pred = logreg.predict(X_test)
# Mis-classification
logreg_cross = pd.crosstab(logreg_test_pred,y_test)
(logreg_cross.iloc[0,1]+logreg_cross.iloc[1,0])/np.sum(logreg_cross.values)
