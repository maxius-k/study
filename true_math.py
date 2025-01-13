from math import inf

def divide(first, second):
    int_first = int(first)
    int_second = int(second)
    if int_second == 0:
        print(inf)
    else:
        print(int_first / int_second)
