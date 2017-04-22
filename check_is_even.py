#define the function using if/elif statements 
def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

#alternative method using one line of code
def is_even(number):
	return number % 2 == 0

#testing the code
def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(8) == True
  assert is_even(100) == True
  assert is_even(101) == False
  print("YOUR CODE IS CORRECT!")

test_is_even()