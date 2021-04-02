# 프로그래머스 문제풀이

## 징검다리

---

### 소스 코드

```python
def solution(distance, rocks, n):
    
    def isFeasable(distance, rocks, n, k):
        cnt = 0
        pos = 0
        total = len(rocks)
        for rock in rocks:
            if rock - pos >= k:
                cnt += 1
                pos = rock

        if total-cnt <= n:
            return True

        return False

    answer = 0
    l = 0
    r = distance
    rocks.sort()
    while l < r:
        mid = (l+r) // 2
        if(isFeasable(distance, rocks, n, mid)):
            answer = mid
            l = mid+1
        else:
            r = mid
            
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
```

### Output
```
4
```

돌들의 위치를 정렬하고 거리의 최솟값을 k로 잡아 몇 개의 돌들을 지우는지 이분탐색으로 검색하여 최대값을 찾아냈습니다.
