count = 0

A = 'aaabbcccccca'

result = A[0]


for i in A:
    if i == result[-1]:
        count+=1
    else:
        result += str(count) + i
        count = 1
result +=str(count)

print(result)