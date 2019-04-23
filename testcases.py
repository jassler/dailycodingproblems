# Last argument is the expected result, everything before that the given input

problem_001 = [
    [[1, 19, 39, 40], 20, True],
    [[1, 19, 39, 40], 40, True],
    [[1, 19, 39, 40], 41, True],
    [[1, 19, 39, 40], 58, True],
    [[1, 19, 39, 40], 59, True],
    [[1, 19, 39, 40], 79, True],
    [[1, 19, 39, 40], 80, False],
    [[], 0, False],
    [[1], 1, False],
    [[-2, -4, 3, 5], -1, True],
    [[-2, -4, 3, 5], 0, False],
    [[1, 19, 39, 40, 12, 49, 49, 192, -20, 1294, -1294, 4821, 201, 4832, 1249, 12, -421], 5000, False]
]

problem_002 = [
    [[1, 2, 3, 4, 5], [120, 60, 40, 30, 24]],
    [[3, 2, 1], [2, 3, 6]],
    [[], []],
    [[1], [1]],
    [[40, 0, 40], [0, 1600, 0]]
]

# expects following objects in solution
# [0] => Node class with attributes left, right and val
# [1] => serialize
# [2] => deserialize
problem_003 = [
    "eval", [
        "Node", "Node class with init parameters 'val' (any type), 'left' (optional Node object), 'right' (optional Node object)",
        "serialize", "Serialize function that accepts a Node object as a paramater and turns it into a string",
        "deserialize", "Deserialize function that turns a passed in string into a  object. deserialize(serialize(node)) should produce the same object"
    ],
    ["Node('root').val", "root"],
    ["Node('root', Node('left', Node('left.left')), Node('right')).left.left.val", "left.left"],
    ["deserialize(serialize(Node('root', Node('left', Node('left.left')), Node('right')))).left.left.val", "left.left"]
]

problem_004 = [
    [[3, 4, -1, 1], 2],
    [[1, 2, 0], 3],
    [[x for x in range(0, 200) if x != 119], 119]
]

### not sure how to test problem set 5 ###

### not sure how to test problem set 6 ###

problem_007 = [
    ['111', 3],
    ['666', 1],
    ['1234568129', 6],
    ['11111111', 34],
    ['53215923932149324932142010', 216]
]

### not sure how to test problem set 8 ###

problem_009 = [
    [[2, 4, 6, 2, 5], 13],
    [[5, 1, 1, 5], 10],
    [[0, -30, -10, -5], -5]
]

### problem set 10... what? ###

problem_011 = [
    [['dog', 'deer', 'deal'], 'de', ['deer', 'deal']],
    [['frog', 'fridge', 'fafra', 'mutton'], 'fr', ['frog', 'fridge']]
]

# N number of steps, X number of steps that can be taken at once
problem_012 = [
    [4, [1, 2], 5],
    [6, [1, 3, 5], 8] # not sure
]

problem_013 = [
    ['abcba', 2, 'bcb'],
    ['annatawa', 2, 'anna']
]

problem_014 = [
    [3.141]
]
