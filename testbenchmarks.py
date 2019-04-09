# Layout: first argument is title of benchmark, second is number of times it should run, then parameters to pass to function
problem_001 = [
    ['Short input | True  value', 10^8, [5, 10, 16, 20], 26],
    ['Short input | False value', 10^8, [5, 10, 16, 20], 27],
    ['Long  input | True  value', 10, [x * 2 for x in range(-10000, 10000)], 10002],
    ['Long  input | False value', 10, [x * 2 for x in range(-10000, 10000)], 1],
]