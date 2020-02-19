#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # get the recipe ingredients REQUIRED
  # make a copy of that recipe with all ingredients at 0
  # loop through the ingredients and add the batch number for each on the copy recipe
  # return the lowest value on the copy recipy as that is the max batch number
  batches = recipe.copy()
  for k in batches.keys():
    if k in ingredients:
      batches[k] = ingredients[k] // recipe[k]
      if batches[k] == 0:
        break
    else:
      batches[k] = 0
  return min(batches.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))