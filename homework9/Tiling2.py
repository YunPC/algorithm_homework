def solution(n):
    answer = 0

    fn, fn_1 = 0, 1
    for i in range(n+1):
        fn, fn_1 = fn_1, fn+fn_1
        fn %= 1000000007
        fn_1 %= 1000000007

    return fn % 1000000007

print(solution(4))
