# We already learned to create functions
# which accept a parameter and return values

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# print('Your initial is: ' + first_name_initial)

# ===============================================

# You can specify a default value for a 
# parameter

# def get_initial(name, force_uppercase=True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# print('Your initial is: ' + first_name_initial)

# ===============================================

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase=True, name=first_name)

print('Your initial is: ' + first_name_initial)