# dictionaries 
# DICT[key] --> value
# LIST[0] --> 0th element of the list
# { key1: value1, key2: value2, ... }

phone_book = {
	'omar': ['123-456-7890', 'omar@omar.com'], 
	'dave': ['222-222-2222', 'dave@dave.com'],
	'joe': ['333-333-3333', 'joe@joe.com']
	}

print(phone_book['omar'][0])
print(phone_book['dave'][0])
print(phone_book['joe'][1])

# DICT[omar] --> list of thigs containing ph# and email.