def name_place(name):
  return {'Usain': 1, 'Me': 2, 'Tom': 3}[name]



def place_name(place):
  return {1: 'Usain', 2: 'Me', 3: 'Tom'}[place]

def test_name_place():
  assert name_place('Usain') == 1
  assert name_place('Me') == 2
  assert name_place('Tom') == 3
  
def test_place_name():
  assert place_name(1) == 'Usain'
  assert place_name(2) == 'Me'
  assert place_name(3) == 'Tom'
  print("SUCCESS")
def test_all():
  try:
    test_name_place()
    test_place_name()
  
  except AssertionError:
    import wrong
  
test_all()