# Modules

# What's a module?
# A Python file with functions, classes and other components.
 
# Why use modules? 
# Break code down into reusable structures

# =======================================
# Creating a module 
# helpers.py
# def display(message, is_warning=False):
#     if is_warning:
#         print('Warning!!')
#     print(message)
# =======================================
# Import a module

# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')

# ===========================================
# Packages

# What are packages?
# Published collections of modules 

# How do I find packages?
# Python Package Index - Internet search

# Installing packages
# Install an individual package
# pip install colorama

# Install from a list of packages
# pip install -r requirements.txt

# requirements.txt
# colorama