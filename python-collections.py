# Lists are collections of items 

# names = ['Z', 'Zone']
# scores = []
# scores.append(98) # Add new item to the end
# scores.append(99)
# print(names)
# print(scores)
# print(scores[1]) #Collections are zero-indexed

# Arrays are also collections of items 

# from array import array

# scores = array('d')
# scores.append(97)
# scores.append(98)
# print(scores)
# print(scores[1])

# Common operations on Lists

# key_words = ['X', 'Zone']
# print(len(key_words)) # Get the number of items
# key_words.insert(0, 'Z') # Insert before index
# print(key_words)
# key_words.sort()
# print(key_words)


# Dictionaries

# key_value = {'first' : 'Z'}
# key_value['last'] = 'Zone'
# print(key_value)
# print(key_value['first'])

person1 = {}
person1['first'] = 'John'
person1['last'] = 'Jay'

person2 = {}
person2['first'] = 'Anna'
person2['last'] = 'Peson'

people = []
people.append(person1)
people.append(person2)
people.append({
    'first' : 'Bill', 'last' : 'Gates'
})

print(people[0])