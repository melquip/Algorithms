#!/usr/bin/python

import sys
import functools

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  if n < 1:
    return 1
  actions = [1, 2, 3]
  currCookie = n
  allCombs = [[action] for action in actions if action <= n]
  # print('init?', responseArr)
  while (currCookie > 1):
    combs = []
    for action in actions:
      combinations = []
      for resArr in allCombs:
        newCombination = None
        if sum(resArr) + action <= n:
          newCombination = [action] + resArr
        elif sum(resArr) == n:
          newCombination = resArr
        # print('resArr, action, newCombination', resArr, action, newCombination)
        if newCombination != None:
          combinations.append(newCombination)
      # print('combinations', combinations)
      combs += combinations
    allCombs = combs
    currCookie -= 1

  # remove duplicates in place
  allCombs = [allCombs[i] for i in range(0, len(allCombs)) if allCombs.index(allCombs[i]) == i]
  print('response:', allCombs)
  return len(allCombs)
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')