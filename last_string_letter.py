def last_letter(string):
	return string[-1]

print last_letter('hola')
print last_letter('cargo')
print last_letter('99')
print last_letter('DUDE')
print last_letter('1')

def test_last_letter():
  assert last_letter('hola') == 'a'
  assert last_letter('cargo') == 'o'
  assert last_letter('99') == '9'
  assert last_letter('DUDE') == 'E'
  assert last_letter('1') == '1'
  print("YOUR CODE IS CORRECT!")
  
test_last_letter()