def string_length(string):
	return len(string)

print(string_length('hello!'))
print(string_length('bro'))
print(string_length('I'))
print(string_length('hilarious'))
print(string_length('007'))

def test_string_length():
  assert string_length('hello!') == 6
  assert string_length('bro') == 3
  assert string_length('I') == 1
  assert string_length('hilarious') == 9
  assert string_length('007') == 3
  print("YOUR CODE IS CORRECT!")
  
test_string_length()