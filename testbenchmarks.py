import random

def shuffled_list(l: list):
    random.shuffle(l)
    return l

# Layout: first argument is title of benchmark, second is number of times it should run, then parameters to pass to function
problem_001 = [
    ['Short input | True  result', 10**6, [5, 10, 16, 20], 26],
    ['Short input | False result', 10**6, [5, 10, 16, 20], 27],
    ['Long  input | True  result', 10**2, [x * 2 for x in range(-10000, 10000)], 10002],
    ['Long  input | False result', 10**2, [x * 2 for x in range(-10000, 10000)], 1],
]

problem_002 = [
    ['Short input, no zero  ', 10**6, [1, 2, 3, 4, 5]],
    ['Short input, with zero', 10**6, [7, 8, 9, 0, 3]],
    ['Long  input, no zero  ', 10**5, [x * 2 for x in range(1, 100)]]
]

problem_004 = [
    ['199 items, returns 119', 10**6, shuffled_list([x for x in range(0, 200) if x != 119])],
    ['200 items, returns 201', 10**6, shuffled_list([x for x in range(0, 200)])]
]