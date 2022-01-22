# CGAS-BIO544

# Introduction
The repository contains all the assignments that I submitted for the course Computational Gastronomy at IIIT Delhi.
Computational Gastronomy is an elementary course to the science of the food.

- The assignment 1 deals with the EDA of the food data available to us. We try to find the number of unique ingredients available to us and their popularity in different cuisines. We find out the reason for the ingredients' popularity. We also delve into the food patterns of different cuisines.
- In the assignment 2, our aim is to replicate the copy-mutate algorithm. After replicating it properly, we improvise it for the limitations of not taking account of deletion and addition of ingredients. 
- Assignment 3 demands us to analyse the food pairing patterns of the cuisines by applying apriori algorithm. We also create random controls to study the evolution of cuisines.

This is an exploratory course and the above assignments serve as a foundational stone for Computational Gastronomy.

# Dataset
The dataset used for all the assignment is the same. It is a json file of nested dictionaries. Each dictionary within the outer dictionary corresponds to a recipe. It has following keys:
- id: the unique identity of a recipe
- cuisine: the cuisine which the recipe belongs to
- ingredients: it is a list of the ingredients used in the recipe

# Steps to run
- Download the .ipynb file in an assignment that you wish to run.
- Open the notebook on [colab.research.google.com](colab.research.google.com)
- Upload the dataset 'train.json'
- Go to 'Runtime' and click on 'Run all'
