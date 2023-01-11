n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for target in m_list:
    value = binary_search(n_list, target, 0, n - 1)
    if not value:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# --> no yes yes