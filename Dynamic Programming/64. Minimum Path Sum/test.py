dp1 = [[1] * (3 + 1) for r in range(3 + 1)]
dp1[3 -1][3] = 0

dp2 = [[1] * (3 + 1) ] * (3 + 1)
dp2[3 -1][3] = 0


dp4 = [[1  for c in range(3 + 1)] for r in range(3 + 1)]
dp4[3 -1][3] = 0

print(dp1)
print("--------")
print(dp2)

print("--------")
print(dp4)