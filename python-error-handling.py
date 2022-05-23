# Defining terms
# -> Error handling - Try/Expect/Finally is where there's something that's happened 
#    external to my application, that I couldn't predict.  
# -> Debugging - I've got a problem with my code, I'm trying to fix that problem.

#Error types
# -> Syntax errors
# -> Runtime errors
# -> Logic errors

# Syntax errors
# This code won't run at all
# x = 42
# y = 206
# if x == y
#     print('Success!!')


# Runtime errors 
# This code will fail when run
# x = 41
# y = 0 
# print(x/y)


# Catching runtime errors 

# try:
#     print(x /y)
# except ZeroDivisionError as e:
#     # Optionally, log e somewhere
#     print('Sorry, sommething went wrong')
# except:
#     print('Something really went wrong')
# finally:
#     print('This always runs on success or failure')


# Logic errors
# This code won't rut at all
# x = 206
# y = 42
# if x < y:
#     print(str(x) + ' is greater than' + str(y))


# Figuring out what went wrong
# Stack trace
# -> Last calls are on the top
# -> Your code is likely on the bottom
# -> Seek out line numbers

# Finding your mistake
# -> Reread ypur code
# -> Check the documentation
# -> Search the internet StackOverFlow
# -> Take a break
# -> Ask someone for help

x = 1
y = 0

try:
    print (x/y)
except ZeroDivisionError as e:
    # raise e
    print('Not allowed to divide by ')
else:
    print('Something else went wrong')    
finally:
    print('This is our cleanup code')