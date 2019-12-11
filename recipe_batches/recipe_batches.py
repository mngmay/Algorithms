#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    print(recipe, ingredients)
    batches = [0] * len(recipe)
    i = 0
    print(batches)
    # for all ingredients needed in recipe
    for key in recipe:
        # if ingredient not avail, return 0
        if key not in ingredients:
            return 0
        # if you have it, while ingredient # >= what's needed, take ingredient # and subtract recipe #
        while ingredients[key] >= recipe[key]:
            ingredients[key] -= recipe[key]
            batches[i] += 1
        i += 1

    return min(batches)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
