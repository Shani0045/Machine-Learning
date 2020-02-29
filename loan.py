import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as ms
plt.style.use("ggplot")
dt=pd.read_csv("F:/Project/Loan-Prediction-Dataset-master/train.csv")
print(dt.head())
sns.countplot(dt.Loan_Status)
plt.show()

#plt.title("Checking for Null Values")
ms.matrix(dt,color=(0.00,0.00,0.00),fontsize=9)
plt.show()

sns.countplot(dt.Gender)
plt.show()

sns.countplot(dt.Married)
plt.show()

sns.countplot(dt.Married,hue=dt.Loan_Status)
plt.show()

sns.countplot(dt.Gender,hue=dt.Loan_Status)
plt.show()

plt.figure(figsize=(12,7))
plt.title("Correlation Matrix")
sns.heatmap(dt.corr(),annot=True,linewidths=1)
plt.show()

dt.drop(["Loan_ID"],axis=1,inplace=True)
dt.Dependents=dt.Dependents.fillna(dt.Dependents.mode()[0])
dt.Gender=dt.Gender.fillna("Male")
dt.Married=dt.Married.fillna("Yes")
dt["Self_Employed"]=dt["Self_Employed"].fillna("No")
dt.LoanAmount=dt.LoanAmount.fillna(dt.LoanAmount.mean())
dt.Loan_Amount_Term=dt.Loan_Amount_Term.fillna(dt.Loan_Amount_Term.mean())
dt.Credit_History=dt.Credit_History.fillna(1)

#plt.title("Checking for Null Values")
ms.matrix(dt,color=(0.00,0.00,0.00),fontsize=9)
plt.show()

from sklearn.preprocessing import LabelEncoder
names=["Gender","Dependents","Married","Education","Self_Employed","Property_Area","Loan_Status"]
for i in names:
    le=LabelEncoder()
    dt[i]=le.fit_transform(dt[i])
    
plt.figure(figsize=(12,7))
sns.heatmap(dt.corr(),annot=True,linewidths=1)
plt.show()

x=dt.drop("Loan_Status",axis=1)
y=dt["Loan_Status"]

dt[["Dependents","LoanAmount","CoapplicantIncome","Loan_Amount_Term","Credit_History"]]=dt[["Dependents","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History"]].astype("int32")

print(dt.head())
dt.LoanAmount=dt.LoanAmount.replace(0,dt.LoanAmount.mean())
x=dt.drop("Loan_Status",axis=1)
y=dt["Loan_Status"]

from imblearn.over_sampling import RandomOverSampler
nm=RandomOverSampler()

x_res,y_res=nm.fit_sample(x,y)

from sklearn.model_selection import train_test_split

x_tr,x_ts,y_tr,y_ts=train_test_split(x_res,y_res,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
m=RandomForestClassifier(n_estimators=100,criterion="gini",random_state=0)
m.fit(x_tr,y_tr)

pred=m.predict(x_ts)
from sklearn.metrics import accuracy_score
m.score(x_ts,y_ts)

from sklearn.metrics import confusion_matrix,classification_report,precision_score,f1_score,accuracy_score
print("Classification Report of Model :\n\n",classification_report(y_ts,pred))

print("\n\n","Accuracy Score of Model  is : " ,round(m.score(x_ts,y_ts),2)*100,"%")

plt.figure(figsize=(10,6))

plt.title("Confusion Matrix")
sns.heatmap(confusion_matrix(y_ts,pred),annot=True,linewidths=1,linecolor="black")
plt.show()
