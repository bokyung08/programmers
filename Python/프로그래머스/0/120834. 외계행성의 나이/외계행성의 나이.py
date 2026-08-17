def solution(age):
    aage = list(str(age))
    dic = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', 
           '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    my_str = ""
    for char in aage:
        my_str += dic[char]
    
    return my_str