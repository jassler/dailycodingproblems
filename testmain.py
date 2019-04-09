import os, sys, time

if sys.platform.lower() == "win32":
    os.system('color')

class style():
    BLACK = lambda x: '\033[30m' + str(x) + style.RESET('')
    RED = lambda x: '\033[31m' + str(x) + style.RESET('')
    GREEN = lambda x: '\033[32m' + str(x) + style.RESET('')
    YELLOW = lambda x: '\033[33m' + str(x) + style.RESET('')
    BLUE = lambda x: '\033[34m' + str(x) + style.RESET('')
    MAGENTA = lambda x: '\033[35m' + str(x) + style.RESET('')
    CYAN = lambda x: '\033[36m' + str(x) + style.RESET('')
    WHITE = lambda x: '\033[37m' + str(x) + style.RESET('')
    UNDERLINE = lambda x: '\033[4m' + str(x) + style.RESET('')
    RESET = lambda x: '\033[0m' + str(x)

def test(function, cases: list):
    print(style.CYAN('=== Testing function {}.{} ==='.format(function.__module__, function.__name__)))

    if len(cases) == 0:
        print('Nothing to test (add test cases to testcases.py)')
        return

    # tests passed
    passed = 0

    # insert linebreak before error messages, if it's not at the beginning of a line
    line_beginning = True
    for args in cases:
        result = function(*args[:-1])

        if(args[-1] != result):
            # ERROR: Print error message
            if not line_beginning:
                print()
            print(style.RED('✘ Input was {}, expected {}, got {}'.format(str(args[:-1]), str(args[-1]), str(result))))
            line_beginning = True

        else:
            # TEST GOOD!
            line_beginning = False
            passed += 1
            print(style.GREEN('✓'), end='')
    
    if not line_beginning:
        print()
    
    score_style = style.GREEN
    if passed < len(cases) / 2:
        score_style = style.RED
    elif passed < len(cases):
        score_style = style.YELLOW
    print(score_style('Passed {} / {} tests ({:.0f}%)'.format(passed, len(cases), passed * 100 / len(cases))))

def benchmark(function, cases: list):
    print(style.CYAN('=== Benchmarking function {}.{} ==='.format(function.__module__, function.__name__)))

    if len(cases) == 0:
        print('No cases to benchmark (add input cases to testcases.py)')
        return

    for case in cases:
        # first argument is title, second is number of times to be run
        print('{}: running...'.format(case[0]), end='')
        sys.stdout.flush()

        arguments = case[2:]

        start = time.time()
        for _ in range(0, case[1]):
            function(*arguments)
        end = time.time()

        print('\r{}: {:.10f} seconds ({:.4} per run)'.format(case[0], end - start, (end-start) / case[1]))