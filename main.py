import sys

from operations.basic import add, subtract, multiply, divide
from operations.advanced import power, root, mod
from operations.scientific import factorial, exponential, logarithm

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Enter --help to get the functions.')
    else:
        if sys.argv[1] == '--help':
            print('========= Command structure =========')
            print('function <param1> <param2> <param3> ...')
            print('add:\t\t\t number number')
            print('subtract:\t\t minuend subtrahend')
            print('multiply:\t\t number number')
            print('divide:\t\t\t dividend divisor')
            print('mod:\t\t\t number number')
            print('power:\t\t\t base exponent')
            print('root:\t\t\t number')
            print('factorial:\t\t number')
            print('exponential:\t\t number')
            print('logarithm:\t\t number base')
        elif sys.argv[1] == 'add':
            if len(sys.argv) == 4:
                add(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'subtract':
            if len(sys.argv) == 4:
                subtract(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'multiply':
            if len(sys.argv) == 4:
                multiply(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'divide':
            if len(sys.argv) == 4:
                divide(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'power':
            if len(sys.argv) == 4:
                power(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'root':
            if len(sys.argv) == 3:
                root(float(sys.argv[2]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'mod':
            if len(sys.argv) == 4:
                mod(int(sys.argv[2]), int(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'factorial':
            if len(sys.argv) == 3:
                factorial(float(sys.argv[2]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'exponential':
            if len(sys.argv) == 3:
                exponential(float(sys.argv[2]))
            else:
                print('[!] Wrong number of parameters entered.')
        elif sys.argv[1] == 'logarithm':
            if len(sys.argv) == 4:
                logarithm(float(sys.argv[2]), float(sys.argv[3]))
            else:
                print('[!] Wrong number of parameters entered.')
        else:
            print('[!] Unknown operation entered.')