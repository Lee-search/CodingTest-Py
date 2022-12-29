N = int(input())

count = 0
for i in range(N + 1):      # H
    for j in range(60):     # M
        for k in range(60): # S
            if '3' in str(i) + str(j) +  str(k):
                count += 1
print(count)