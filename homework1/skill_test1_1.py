def solution(n):
    digits = []

    while n > 0:
        digits.append(n%10)
        n //= 10

    digits.sort()

    answer = 0

    for i, digit in enumerate(digits):
        answer += digit * 10**(i)
        
    return answer