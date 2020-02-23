#!/usr/bin/python

import sys
import argparse

def find_max_profit(prices):
  buy = max(prices)
  # find best buy opportunity
  for i in range(0, len(prices) - 1):
    # if this is a better buy opportunity
    if prices[i] < buy:
      # check if we'll be able to sell at a higher price
      for p in prices[i+1:]:
        if p > prices[i]:
          # replace buy order with the new/better one
          buy = prices[i]
          break
  # print('buy at:', buy)
  # max profit starts at the lowest
  maxProfitSoFar = -sys.maxsize
  sell = buy
  # find best sell opportunity after the buy order
  for i in range(prices.index(buy) + 1, len(prices)):
    # if this is NOT the best trade we can have
    if prices[i] - buy > maxProfitSoFar:
      # change sell order to a new/better one
      sell = prices[i]
      # for higher profit
      maxProfitSoFar = sell - buy
  # print('sell at:', sell)

  return maxProfitSoFar


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))