import time
n = 50
## ------ 1 ------ ##

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

t = time.time()
#print(fibo(n))
#print(time.time() - t)

## ------ 2 ------ ##

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

t = time.time()
print(fibo(n))
print(time.time() - t)

## ------ 3 ------ ##

d = [0] * 100

d[1] = 1
d[2] = 1

t = time.time()
for i in range(3, n + 1):
    d[i] = d[i - 1]  + d[i - 2]
print(d[n])
print(time.time() - t)