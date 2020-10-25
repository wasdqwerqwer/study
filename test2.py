a = int (input("최대 판매량:"))
b = int (input("평균 판매량"))
c = int (input("최대 리드:"))
d = int (input("평균 리드:"))
e = a * c - b * d
f = e / b
round (f, 1)
print(e)
print(f)