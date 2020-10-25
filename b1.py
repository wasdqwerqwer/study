train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

train_y = train[""] # 목표 값을 train_y에 넣는다
del train[""] # 전체 데이터에서 목표값 삭제
train_x = train # 목표값이 삭제된 전체 데이터를 대입

test_y = test[""]
del test[""]
test_x = test

#////////////////////////////////////////////////////////////////

df = pd.read_csv('bank_marketing_simple.csv', sep=';')

pd.get_dummies(df,columns=[])


del df['']

print(df.columnstolist())
