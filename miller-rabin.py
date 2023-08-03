#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random
import sys

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)

    try:
        num_to_check = int(sys.argv[1])
        if num_to_check <= 0:
            print("only positive integer.")
            sys.exit(1)

        if miller_rabin(num_to_check):
            print(f"{num_to_check} is probably a prime number.")
        else:
            print(f"{num_to_check} is not a prime number.")

    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
