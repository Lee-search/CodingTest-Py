array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        # Pivot 보다 큰 데이터를 찾을 떄 까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # Pivot 보다 작은 데이터를 찾을 떄 까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체,
        # 아니라면 작은 데이터와 큰 데이터 교체
        if left > right:
           array[right], array[pivot] =  array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)