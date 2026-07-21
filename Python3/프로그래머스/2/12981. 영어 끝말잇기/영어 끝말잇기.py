def solution(n, words): 
    used=set()
    for idx, word in enumerate(words):
        if idx>0 and words[idx -1][-1] != word[0]: 
            return[idx%n+1, idx//n+1]
        if word in used: 
            return[idx%n+1, idx//n+1]
        used.add(word)
    return [0,0]