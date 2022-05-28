# Functions

# Use functions instead of repeating code

# import datetime
# # Print the current time
# def print_time():
#     print('task completed')
#     print(datetime.datetime.now())
#     print()

# first_name = 'John'
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()


# By moving the code to a function, you reduce 
# rework and the chance of introducing bugs
# when you change the code you had copied

# Import the datetime class form datetime libraty
from datetime import datetime
# Print the current time
def print_time():
    print('task completed')
    # Now I don't need the extra datetime prefix
    print(datetime.now())
    print()

# ===============================================
# Pass the task name as a parameter

# from datetime import datetime 

# # Print the current time and task name
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = 'John'
# print_time('firs name assigned')

# for x in range(0,10):
#     print(x)
# print_time('loop completed')

# ============================================

# Function returns a value
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial
+ last_name_initial)