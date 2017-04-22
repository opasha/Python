# read as DO SOMETHING 5 TIMES, i can be anything so better to use words (number) instead										 # to never use 1 letter variables
for i in range(5): 
	print("Hello")

# range(5) evaluates to [0, 1, 2, 3, 4]
print(list(range(5))) 

for number in [0, 1, 2, 3, 4]:
	print(number)

# range(0, 2) --> [0, 1] so, starts with 0, but stops before 2

# from 20-40, 20 is the START (included) 41 is the STOP(not included)
for number in range(20, 41): 
	print(number)

# [1, 2, 3] --> 6
count = 0
for number in range(1, 4):
	count = count + number #new count = old_count + number
#print(count) # answer should be 6 at end of the loop

#write a function that sums all elements of a list and returns them
def sum_list(my_list):
	count = 0
	for number in my_list:
		count = count + number

	return count
# assertion if correct gives no error (nothing shown), incorrect gives error
assert sum_list([1, 2, 3]) == 6 
assert sum_list([1, 2, 3, 4]) == 10

print(sum_list([1, 2]))

