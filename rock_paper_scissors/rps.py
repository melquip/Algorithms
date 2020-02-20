#!/usr/bin/python

import sys

def memoize(f):
  cache = {}
  def memoized(n, r, c = {}):
    c = cache
    key = r + [n]
    key = "".join(r)
    if key in c:
      return cache[key]
    result = f(n, r, c)
    cache[key] = result
    return result
  return memoized

# (1) [['rock'], ['paper'], ['scissors']]
# (2) [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

def rock_paper_scissors(rounds):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  @memoize
  def roundOutcome(roundsLeft, result, cache = {}):
    if roundsLeft == 0:
      outcomes.append(result)
      return False
    
    for play in plays:
      roundOutcome(roundsLeft - 1, result + [play])

  roundOutcome(rounds, [])

  return outcomes
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')