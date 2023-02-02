import sys
input = sys.stdin.readline
history = list(map(int, input().split()))

# 첫번쨰 단계를 미리 구한 뒤
if history[0] + 1 == history[1]:
    ascending = True
elif history[0] - 1 == history[1]:
    ascending = False
else:
    print('mixed')
    exit()

for i in range(1, len(history) - 1):
    if history[i] + 1 == history[i + 1]:
        if not ascending:
            print('mixed')
            exit()
    elif history[i] - 1 == history[i + 1]:
        if ascending:
            print('mixed')
            exit()

print('ascending' if ascending else 'descending')