for i in range(10):
    N = int(input())    # dump 횟수
    boxes = list(map(int, input().split())) # 상자 100개

    ans = 0
    for _ in range(N):
        high, low = boxes.index(max(boxes)), boxes.index(min(boxes))
        if boxes[high] == boxes[low]:
            break
        if boxes[high] == boxes[low] + 1:
            ans += 1
            break

        boxes[high] -= 1
        boxes[low] += 1

    high, low = boxes.index(max(boxes)), boxes.index(min(boxes))
    ans = boxes[high] - boxes[low]

    print('#' + str(i) + ' ' + str(ans))