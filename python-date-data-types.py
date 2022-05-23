# =========================================
# We often need current date and time
# when logging errors and saving data

# To get current date and time 
# we need to use the datetime library

from datetime import datetime

current_date = datetime.now()
# the now function returns a datetime object

print('Today is: ' + str(current_date))

# ========================================
# There are functions you can use with
# datetime objects to manipulate dates

from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# =========================================
# Use date functions to control date formatting

from datetime import datetime
current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

print('Hour: ' + str(current_date.hour))
print('Minute: ' + str(current_date.minute))
print('Second: ' + str(current_date.second))


# ===========================================
# Somethimes you receive the date as a string
# and need to convert it to a datetime object 

from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy) ? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birhday: ' + str(birthday_date))







