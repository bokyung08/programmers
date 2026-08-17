def solution(want, number, discount):
    answer = []
    cnt = 0 
    for idx, num in enumerate(number): 
        for i in range(num): 
            answer.append(want[idx])
    answer.sort()

    for i in range(len(discount)-len(answer)+1): 
        current_discount = discount[i: i+len(answer)]
        #print(current_discount)
        if answer==sorted(current_discount): 
            cnt +=1
    return cnt