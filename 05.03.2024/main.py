a=2
n=int(input())
m=[True]*(n+1)
m[0] = m[1] = False
for i in range(2, n+1):
    if m[i]:
        if a<=i<=n:
            print(i, end = ' ')
            for k in range(i**2, n+1, i):
                m[k] = False
