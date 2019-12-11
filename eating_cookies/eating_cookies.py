#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # Base cases
    # if there are invalid negative cookies, 0 ways
    if n < 0:
        return 0

    elif n == 1 or n == 0:
        return 1

    elif n == 2:
        return 2

    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


# Notes
# 4 cookies
# 3,1
# 2,2
# 2,1,1
# 1,3
# 1,2,1
# 1,1,2
# 1,1,1,1

# 5 cookies
# 3,2
# 3,1,1
# 2,3
# 2,2,1
# 2,1,2
# 2,1,1,1
# 1,3,1
# 1,2,2
# 1,2,1,1
# 1,1,1,1,1
# 1,1,2,1
# 1,1,3
# 1,1,1,2

# # of cookies = ways to eat
# 0 = 1
# 1 = 1
# 2 = 2
# 3 = 4
# 4 = 7
# 5 = 13
# 6 = 24
# 7 = 44
# 8 = 81
# 9 = 149
# 10 = 274

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
