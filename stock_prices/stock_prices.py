#!/usr/bin/python

import argparse


def find_max_profit(prices):
    curr_min = prices[0]

    best_profit = prices[1] - prices[0]

    for price in prices:
        if price < curr_min:
            curr_min = price

        if prices.index(curr_min) < prices.index(price):
            if price - curr_min > best_profit:
                best_profit = price - curr_min

    # return final best price

    return best_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
