# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import json
import operator

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
ingredient_frequency = {}

# stores the number of recipes corresponding to each recipe size
recipeSize_recipes = {}

for i in range(len(data)):
    dict = data[i]
    list_ingredients = dict['ingredients']

    # Finding out the frequency of each ingredient
    for ingredient in list_ingredients:
        if ingredient in ingredient_frequency:
            ingredient_frequency[ingredient] = ingredient_frequency[ingredient]+1
        else:
            ingredient_frequency[ingredient] = 1

    recipe_size = len(list_ingredients)
    if recipe_size in recipeSize_recipes:
        recipeSize_recipes[recipe_size] = recipeSize_recipes[recipe_size]+1
    else:
        recipeSize_recipes[recipe_size] = 1

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

for cuisine in uniqueCuisines:

    # Stores the number of recipes corresponding to each recipe and cuisine
    recipeSize_numberOfCuisies = {}
    Legend.append(cuisine)

    # to calculate percentage of recipe size
    numOfRecipesInCuisine = 0.0
    for recipe in data:
        recipe_size = len(recipe['ingredients'])

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

# Computing the percentage of each recipe size
for recipe_size in recipeSize_recipes:
    recipeSize_recipes[recipe_size] = recipeSize_recipes[recipe_size]/float(len(data))

# Plotting the graph
x_axis = list(recipeSize_recipes.keys())
y_axis = list(recipeSize_recipes.values())
plt.scatter(x_axis, y_axis)
plt.xlabel("Recipe size")
plt.ylabel("Percentage")
plt.show()

# Plotting CDF
cdfData = x_axis
count, bins_count = np.histogram(cdfData, bins = 10)
pdf = count/sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, color="blue", label="CDF")
plt.legend()
plt.show()

# Q3 a
sorted_matrix = sorted(ingredient_frequency.items(),key=operator.itemgetter(1),reverse=True)
sorted_dict = {}
topTenIngredients = []
j = 0

for i in range(len(sorted_matrix)):
    sorted_dict[i] = sorted_matrix[i][1]
    if(j<10):
        topTenIngredients.append(sorted_matrix[i][0])
    j = j+1

# print(sorted_dict)
x_axis = list(sorted_dict.keys())
y_axis = list(sorted_dict.values())

# Dot plot
plt.scatter(x_axis,y_axis)
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.show()

# Line plot
plt.plot(x_axis,y_axis)
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.show()

print("The 10 most popular ingredients in the recipes are: ")
for ingredient in topTenIngredients:
    print(ingredient)