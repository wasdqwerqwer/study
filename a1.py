import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import seaborn as sns


le = LabelEncoder()
df = pd.read_csv('telecom_churn.csv')
df.dropna(inplace = True)
df['gender'] = le.fit_transform(df['gender'])
df['SeniorCitizen'] = le.fit_transform(df['SeniorCitizen'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['tenure'] = le.fit_transform(df['tenure'])
df['PhoneService'] = le.fit_transform(df['PhoneService'])
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])
df['InternetService'] = le.fit_transform(df['InternetService'])
df['OnlineSecurity'] = le.fit_transform(df['OnlineSecurity'])
df['OnlineBackup'] = le.fit_transform(df['OnlineBackup'])
df['DeviceProtection'] = le.fit_transform(df['DeviceProtection'])
df['TechSupport'] = le.fit_transform(df['TechSupport'])
df['StreamingTV'] = le.fit_transform(df['StreamingTV'])
df['StreamingMovies'] = le.fit_transform(df['StreamingMovies'])
df['Contract'] = le.fit_transform(df['Contract'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])
df['Churn'] = le.fit_transform(df['Churn'])

Logistic = LogisticRegression(solver='newton-cg')
Logistic.fit(df[['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']], df['Churn'])


test = pd.read_csv('telecom_churn_test.csv')
test.dropna(inplace = True)

test['gender'] = le.fit_transform(test['gender'])
test['SeniorCitizen'] = le.fit_transform(test['SeniorCitizen'])
test['Partner'] = le.fit_transform(test['Partner'])
test['Dependents'] = le.fit_transform(test['Dependents'])
test['tenure'] = le.fit_transform(test['tenure'])
test['PhoneService'] = le.fit_transform(test['PhoneService'])
test['MultipleLines'] = le.fit_transform(test['MultipleLines'])
test['InternetService'] = le.fit_transform(test['InternetService'])
test['OnlineSecurity'] = le.fit_transform(test['OnlineSecurity'])
test['OnlineBackup'] = le.fit_transform(test['OnlineBackup'])
test['DeviceProtection'] = le.fit_transform(test['DeviceProtection'])
test['TechSupport'] = le.fit_transform(test['TechSupport'])
test['StreamingTV'] = le.fit_transform(test['StreamingTV'])
test['StreamingMovies'] = le.fit_transform(test['StreamingMovies'])
test['Contract'] = le.fit_transform(test['Contract'])
test['PaperlessBilling'] = le.fit_transform(test['PaperlessBilling'])
test['PaymentMethod'] = le.fit_transform(test['PaymentMethod'])
test['Churn'] = le.fit_transform(test['Churn'])

score = Logistic.score(test[['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']], test['Churn'])

print(score)

plt.show()