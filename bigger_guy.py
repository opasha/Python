def bigger_guy(a, b):
	if a > b:
		return a
	else:
		return b

print bigger_guy(5, 10)
print bigger_guy(10, 20)
print bigger_guy(40, 20)
print bigger_guy(20, 20)
print bigger_guy(100, 50)
print bigger_guy('a', 'b')


def test_bigger_guy():
  assert bigger_guy(5, 10) == 10
  assert bigger_guy(10, 20) == 20
  assert bigger_guy(40, 20) == 40
  assert bigger_guy(20, 10) == 20
  assert bigger_guy(100, 50) == 100
  assert bigger_guy('a', 'b') == 'b'  # 'b' is greater than 'a'
  print("YOUR CODE IS CORRECT!")
  
test_bigger_guy()