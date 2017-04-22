def square_number(number):
	return number ** 2

print(square_number(4))
print(square_number(8))
print(square_number(16))


def test_square_number():
  assert square_number(4) == 16
  assert square_number(8) == 64
  assert square_number(16) == 256
  print("YOUR CODE IS CORRECT!")

test_square_number()