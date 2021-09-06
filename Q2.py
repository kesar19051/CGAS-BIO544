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
print(len(data))

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

