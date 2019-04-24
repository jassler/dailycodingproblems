

def find_int_sorted(input: list):
    inp = sorted(input)
    prev = inp[0]
    for n in inp[1:]:
        if n - 1 > prev and prev > 0:
            return prev + 1
        prev = n
    return prev + 1

def find_singlepass(input: list):
    res = [False] * (max(input) + 1)
    
    for n in input:
        if n > 0:
            res[n] = True
    
    res[0] = True
    for i, b in enumerate(res):
        if not b:
            return i
    return len(input)