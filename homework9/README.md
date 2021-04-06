# 프로그래머스 문제풀이

## 2xn 타일링
[2xn 타일링 포스팅](https://yunpc.github.io/2021/04/06/2Tiling/)
---

### 소스 코드

```python
def solution(n):
    answer = 0

    fn, fn_1 = 0, 1
    for i in range(n+1):
        fn, fn_1 = fn_1, fn+fn_1
        fn %= 1000000007
        fn_1 %= 1000000007

    return fn % 1000000007

print(solution(4))
```

### Output
```
5
```



## 도둑질
[도둑질 포스팅](https://yunpc.github.io/2021/04/06/Stolen/)
---

### 소스 코드

```python
def solution(money):
    dp1 = [0] * (len(money)-1)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])
    
    return max(dp1[-1], dp2[-1])

print(solution([1, 2, 3, 1]))
```

### Output
```
4
```