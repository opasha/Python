#define the function using if/elif statements 
def is_odd(number):
	if number % 2 != 0:
		return True
	else:
		return False

#alternative method using one line of code
def is_odd(number):
	return number % 2 != 0

#testing the code
def test_is_odd():
  assert is_odd(2) == False
  assert is_odd(3) == True
  assert is_odd(8) == False
  assert is_odd(100) == False
  assert is_odd(101) == True
  print("YOUR CODE IS CORRECT!")

test_is_odd()