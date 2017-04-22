groceries = ['apple', 'banana', 5, 6, 'oranges']
print groceries[0] #first in the list
print groceries[1] #second in the list
print groceries[-1] #last in the last (-1 is always last in the list)

#split section

'what-is-going-on'.split() #this is a list of strings
print 'what-is-going-on'.split('-') 

greeting = 'what-is-going-on'.split('-')
print greeting[0]
print greeting[1]
print greeting[-1]

# [START:STOP:STEP]

race = ['john', 'bob', 'timothy']
print race
print race[0:]
print race[:] 
print race[0:2]
print race[0:-1]
print race[0::1]
print race[0::2]
print race[0::-1]
print race[::-1] #reverse the list

#split in detail
data = 'XBOX 360 | 150 | New'

data.index('|')

print data.split('|')

details = data.split('|')
print details

product = details[0]
print product

price = details[1]
print price

condition = details[2]
print condition

#Easiest method

product, price, condition = data.split('|')

print data.split('|')
print product
print price
print condition