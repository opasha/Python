def biggest_guy(a, b, c):
	if a > b:
		bigger_guy = a
	else:
		bigger_guy = b
	
	if bigger_guy > c:
		biggest_guy = bigger_guy
	else:
		biggest_guy = c
	
	return biggest_guy



#alternate method using one line of code
def bigger_guy(a, b):
	if a > b:
		return a
	else:
		return b

def biggest_guy(a, b, c):
	return bigger_guy(bigger_guy(a, b), c)

#examples
print biggest_guy(1, 3, 2)
print biggest_guy(30, 10, 20)
print biggest_guy(20, 10, 30)
print biggest_guy(2, 1, 9)
print biggest_guy('a', 'a', 'b')


def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b'  # 'b' is greater than 'a'
    print("SUCCESS!")
    print("YOUR CODE IS CORRECT!")

  except (AssertionError) as e:
    print(e)
    import wrong
    return

test_biggest_guy()