import os
import builtins
from sys import argv, path
from importlib import import_module

import testmain

usage = '{} [test|benchmark] <problem number>\n'.format(argv[0])
if len(argv) < 2:
    print(usage)
    exit(1)

testing = argv[1].lower() == 'test'
benchmark = argv[1].lower() == 'benchmark'

if (testing or benchmark) and len(argv) < 3:
    print(usage)
    exit(1)

try:
    number = int(argv[-1])
    folder = 'problem_{:03d}'.format(number)
    if not os.path.isdir(folder):
        print('Problem {} does not exist'.format(folder))
        print(usage)
        exit(1)
    
    path.insert(0, folder)

    ### TEST ###
    if testing:
        cases = getattr(__import__('testcases'), folder, [])

        had_tests = False
        for file in os.listdir(folder):
            if file.endswith('.py'):
                module = import_module('{}.{}'.format(folder, file[:-3]))
                for _, f in getattr(module, '__dict__').items():
                    
                    if callable(f):
                        had_tests = True
                        testmain.test(f, cases)
        
        if not had_tests:
            print('No functions found to test')
            exit(2)
        
        exit(0)
    
    ### BENCHMARK ###
    if benchmark:
        cases = getattr(__import__('testbenchmarks'), folder, [])

        had_benchmarks = False
        for file in os.listdir(folder):
            if file.endswith('.py'):
                module = import_module('{}.{}'.format(folder, file[:-3]))
                for _, f in getattr(module, '__dict__').items():
                    
                    if callable(f):
                        had_benchmarks = True
                        testmain.benchmark(f, cases)
        
        if not had_benchmarks:
            print('No functions found to benchmark')
            exit(2)
        exit(0)

except ValueError as e:
    print(usage)
    print('Invalid problem "{}", only enter number'.format(argv[-1]))
    exit(1)