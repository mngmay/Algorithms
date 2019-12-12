#!/usr/bin/python

import sys
# Questions
# Are denominations always sorted?
# Always > 0?
# Does having 0 cents count as 1 ways to make change or 0?


def making_change(amount, denominations):

    if amount < 0:
        return 0

    # initialize cache, we know 0 has 1 way, + remaining amounts for 1-amount.
    cache = [1] + [0] * amount

    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            cache[higher_amount] += cache[higher_amount-coin]

    # return integer of ways to make change
    return cache[amount]


if __name__ == "__main__":
              # Test our your implementation from the command line
              # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
