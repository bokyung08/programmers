from itertools import permutations 
def is_prime(n):
    if n<2: 
        return False 
    i=2
    while i * i<=n: 
        if n % i ==0: 
            return False
        i+=1
    return True
def solution(numbers):
    nums=set()
    for r in range(1, len(numbers)+1): 
        for p in permutations(numbers, r): 
            nums.add(int("".join(p)))
    answer=0 
    for n in nums: 
        if is_prime(n): 
            answer+=1
    return answer