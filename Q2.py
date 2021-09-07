# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import json

f = open('train.json')

# This data is list of dictionaries
data = json.load(f)

# Q2
# Printing the number of recipes
print("The number of recipes:")
numOfRecipes = len(data)
print(numOfRecipes)

uniqueIngredients = []
uniqueCuisines = []
cuisine_recipes = {}

for i in range(len(data)):
    dict = data[i]
    list_ingredients = dict['ingredients']
    cuisine = dict['cuisine']

    # Finding the number of cuisines and storing number of recipes for each cuisine
    if cuisine in uniqueCuisines:
        cuisine_recipes[cuisine] = cuisine_recipes[cuisine]+1

    else:
        uniqueCuisines.append(cuisine)
        cuisine_recipes[cuisine] = 1
        
    # Finding the number of ingredients
    for j in range(len(list_ingredients)):
        element = list_ingredients[j]
        if element in uniqueIngredients:
            pass
        else:
            uniqueIngredients.append(element)
        

# Printing the number of unique ingredients
print("The number of unique ingredients:")
print(len(uniqueIngredients))

# Printing the number of cuisines
print("The number of cuisines:")
print(len(uniqueCuisines))

# print(uniqueIngredients)
# print(uniqueCuisines)

# Defining the measures for x and y axes
x_axis = list(cuisine_recipes.keys())
y_axis = list(cuisine_recipes.values())

# Horizontal bar plot as some names are not completely visible
plt.barh(x_axis, y_axis)

# Bar plot
bar_plot = plt.figure(figsize = (10,8))
plt.bar(x_axis,y_axis,color = 'green', width = 0.4)
plt.xticks(rotation = 45) 
plt.xlabel("Cuisine")
plt.ylabel("No. of recipes")
plt.title("Recipes for each cuisine")
plt.show()

# Extracting recipe size and number of cuisines for each cuisine
# to distinguish every cuisine
Legend = []
i = 0

# stores the number of recipes corresponding to each recipe
recipeSize_recipes = {}
for cuisine in uniqueCuisines:

    # Stores the number of recipes corresponding to each recipe and cuisine
    recipeSize_numberOfCuisies = {}
    Legend.append(cuisine)

    # to calculate percentage of recipe size
    numOfRecipesInCuisine = 0.0
    for recipe in data:
        recipe_size = len(recipe['ingredients'])

        if recipe_size in recipeSize_recipes:
            recipeSize_recipes[recipe_size] = recipeSize_recipes[recipe_size]+1
        else:
            recipeSize_recipes[recipe_size] = 1

        if cuisine==recipe['cuisine']:
            numOfRecipesInCuisine = numOfRecipesInCuisine+1
            if recipe_size in recipeSize_numberOfCuisies:
                recipeSize_numberOfCuisies[recipe_size] = recipeSize_numberOfCuisies[recipe_size]+1
            else:
                recipeSize_numberOfCuisies[recipe_size] = 1

    # Calculating the recipe size percentage for each cuisine
    for recipe_size in recipeSize_numberOfCuisies:
        recipeSize_numberOfCuisies[recipe_size] = recipeSize_numberOfCuisies[recipe_size]/numOfRecipesInCuisine

    # Plotting every cuisine
    x_axis = list(recipeSize_numberOfCuisies.keys())
    y_axis = list(recipeSize_numberOfCuisies.values())
    plt.scatter(x_axis, y_axis)

plt.xlabel("Recipe size")
plt.ylabel("Percentage")
plt.legend(Legend)
plt.show()