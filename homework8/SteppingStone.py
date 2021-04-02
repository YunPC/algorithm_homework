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