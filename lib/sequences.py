#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = list()

    for i in range(length):
        if len(fib_list) > 1:
            new_num = fib_list[i - 2] + fib_list[i - 1]
            fib_list.append(new_num)
        else:
            fib_list.append(i)
    print(fib_list)
