import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('bank_marketing_full.csv', sep=';')

df = pd.get_dummies(df,columns=['job','marital','education','default','housing', 'loan', 'contact', 'day', 'month', 'poutcome'])

print(df.columns.tolist())

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

train_y = train["y"]
del train["y"]
train_x = train

test_y = test["y"]
del test["y"]
test_x = test


Logistic = LogisticRegression(solver='newton-cg')
Logistic.fit(train_x, train_y)

score = Logistic.score(test_x, test_y)

print(score)