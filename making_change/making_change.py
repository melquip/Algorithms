#!/usr/bin/python

import sys


def making_change(amount, coins = [1, 5, 10, 25, 50], cache = {}):
  # get the all possible coins left
  uniqueCoins = len(coins)
  # coin value was higher than amount
  # so dont add anything to total
  if amount < 0: return 0
  # finished coin combination
  # so add 1 to total ways of making change for n $
  elif amount == 0: return 1
  # use cache to improve performance
  elif (amount, uniqueCoins) in cache: return cache[(amount, uniqueCoins)]
  # recursive loop
  else:
    total = 0
    for c in range(0, uniqueCoins):
      coin = coins[c]
      if coin > amount:
        continue
      else:
        result = making_change(amount - coin, coins[c:], cache)
        if result > 0:
          total += result
    cache[(amount, uniqueCoins)] = total
    return total

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")