# What is a web service?

# When a developer wants to share the functionality of a function
# but not the actual code in the program, they can place the function
# on a web server.

# A programmer with the address of that function on the web server and
# the required permissions can call the function

# ====================================================================
# What is an API?

# You can't call a function unless you know the function name and the 
# required parameters

# When you create a web service you create an Application Programing
# Interface (API)

# The API defines the function names and parameters so others know 
# how to call your function.

# Example: analyze(visualfeatures, details, language)

# ===================================================================
# Keys allow me to track which users have permission to use my web service

# A developer signs on my web site, or buys a license for my software
# and is provided a unique key.

# When the developer calls my web service they provide their unique key
# and I am able to verify the key has been approved for calls to my
# web service.

# ===================================================================
# There is a standard for sending messages across the web

# Hypertext Transfer Protocol (HTTP) is a standard protocol for sending
# messages across the web.

# GET 
#  - pass values in query string only
#  - special characters must be "escaped"
#  - limited amounf of data

# POST
#  - pass values in query string and body
#  - no need to escape special characters if passed in body
#  - can pass large amount of data, including images, in body

# ====================================================================
# The requests library simplifies HTTP calls from Python code

# requests.post(address,
#               http_headers,
#               function_parameters,
#               message_body)

































