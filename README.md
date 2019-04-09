# Daily-Coding-Problems

This repository aims to solve questions asked from the daily-coding-problem website: <https://www.dailycodingproblem.com/>

Parts of this README have been auto-generated. If new problems are added or the command line arguments change, run `ptyhon update_readme.py` (Python version 3) to update this README.

## Usage (`*`)

```text
usage: main.py [-h] [-t] [-b] n [n ...]

Test and benchmark daily problems

positional arguments:
  n           Problem number to test or benchmark

optional arguments:
  -h, --help  show this help message and exit
  -t          Test problem set
  -b          Benchmark problem set
```

## Adding your own source code

By default **every** function in **every** python file inside a problem-folder will be tested or benchmarked if not explicitly told not to do so. The parameters a function will receive for each problem set can be extracted from the file `testcases.py`.

Test cases can look as follows:

```python
problem_001 = [
    [[1, 19, 39, 40], 20, True],
    [[1, 19, 39, 40], 79, True],
    [[1, 19, 39, 40], 80, False],
    [[], 0, False],
    [[1], 1, False],
    [[1, 19, 39, 40, 12, 49, 49, 192, -20, 1294, -1294, 4821, 201, 4832, 1249, 12, -421], 5000, False]
]
```

Here, there are 6 different tests, one for each row. The last argument (in this case either `True` or `False`) describes the expected value to be returned. The first two arguments for each test (eg. `[1, 19, 39, 40]` and `20`) is the given input.

If we were to write a function for this problem set, given its explicit types it should look as follows:

```python
def my_result(input_1: list, input_2: int) -> bool:
    # calculate calculate calculate...
    return True
```

### Ignoring functions

If a function should not be tested or benchmarked, add an attribute `'test'` and / or `'benchmark'` respectively and set it to `False`.

```python
def do_not_test_me():
    pass
setattr(do_not_test_me, 'test', False)

def do_not_benchmark_me():
    pass
setattr(do_not_benchmark_me, 'benchmark', False)

def ignore_me_completely():
    pass
setattr(ignore_me_completely, 'test', False)
setattr(ignore_me_completely, 'benchmark', False)
```

## Questions (`*`)

### Problem #1 [Easy]

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

*Bonus*: Can you do this in one pass?

### Problem #2 [Hard]

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

*Follow-up*: what if you can't use division?

### Problem #3 [Medium]

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

### Problem #4 [Hard]

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

### Problem #5 [Medium]

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`.

### Problem #6 [Hard]

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields, it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

### Problem #7 [Medium]

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

### Problem #8 [Easy]

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```text
  0
 / \
1   0
   / \
  1   0
 / \
1   1
```

### Problem #9 [Hard]

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

*Follow-up*: Can you do this in O(N) time and constant space?

### Problem #10 [Medium]

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

### Problem #11 [Medium]

Implement an autocomplete system. That is, given a query string `s` and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

### Problem #12 [Hard]

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

### Problem #13 [Hard]

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

### Problem #14 [Medium]

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
