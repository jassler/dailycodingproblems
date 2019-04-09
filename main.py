import os
import builtins
import argparse
from sys import argv, path
from importlib import import_module

import testmain

parser = argparse.ArgumentParser(description='Test and benchmark daily problems')
parser.add_argument('-t', action='store_true', help='Test problem set')
parser.add_argument('-b', action='store_true', help='Benchmark problem set')
parser.add_argument('problems', metavar='n', type=int, nargs='+', help='Problem number to test or benchmark')

args = parser.parse_args()

testing = args.t
benchmark = args.b

def handle_flag(folder: str, testtype: str):
    '''testtype should be either test or benchmark'''

    if testtype == 'test':
        casemodule = 'testcases'
        evalutae = testmain.test
    
    elif testtype == 'benchmark':
        casemodule = 'testbenchmarks'
        evalutae = testmain.benchmark
    
    else:
        print('Unrecognized flag option "{}"'.format(testtype))
        return
    
    cases = getattr(__import__(casemodule), folder, [])
    if len(cases) == 0:
        print('No {} cases under the name of {}. Add tests to testcases.py'.format(testtype, folder))
        return
    
    had_tests = False
    for file in os.listdir(folder):
        if file.endswith('.py'):
            module = import_module('{}.{}'.format(folder, file[:-3]))
            for _, f in getattr(module, '__dict__').items():
                
                if callable(f) and getattr(f, testtype, True):
                    had_tests = True
                    evalutae(f, cases)
    
    if not had_tests:
        print('No functions found to {}'.format(testtype))

for number in args.problems:
    folder = 'problem_{:03d}'.format(number)
    if not os.path.isdir(folder):
        print('Problem {} does not exist'.format(folder))
        exit(1)

    path.insert(0, folder)

    ### TEST ###
    if testing:
        handle_flag(folder, 'test')

    ### BENCHMARK ###
    if benchmark:
        handle_flag(folder, 'benchmark')