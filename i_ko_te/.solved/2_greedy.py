num = list(map(int, list(input())))

total = num[0]
for n in num[1:]:
    if n == 0 or n == 1 or total == 0:
        total += n
    else:
        total *= n

print(total)