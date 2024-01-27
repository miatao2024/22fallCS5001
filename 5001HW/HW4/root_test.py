'''
    CS5001, Mohammad Toutiaee
    Homework 4, 11/29/2022
    Fall 2022
    Minjia Tao
'''

from root import root

num_total_test = 0    #counts of how many tests were run 
num_fail = 0         #counts of how many tests failed

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

default_accuracy = 0.001

tests = [
    [2, 4, 2.0, default_accuracy],
    [3, 27.0, 2.9999, 0.01],
    [100, 1, 1.0, default_accuracy],
    [5, 32, 2.0, default_accuracy],
    [2, -1, -1, default_accuracy]
]


def run_test(test):
    act = root(test[0], test[1], test[3]);
    exp = test[2]
    if abs(exp - act) > test[3]:
        print(f'test {WARNING}failed{ENDC} on root({test[0]}, {test[1]}, {test[3]})')
        print(f'Expected:{exp}, Actual:{act}\n')
        return False
    else:
        print(f'test {OKGREEN}passed{ENDC} on root({test[0]}, {test[1]}, {test[3]})')
        print(f'Expected:{exp}, Actual:{act}\n')  
        return True


def main():
    num_total_test = len(tests)
    num_fail = 0
    for test in tests:
        if not run_test(test):
            num_fail += 1
    print(f'Executed tests: {num_total_test}, Failed: {num_fail}')


if __name__ == '__main__':
    main()
