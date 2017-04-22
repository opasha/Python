bob_hours_worked = 40
if bob_hours_worked > 39:
	print ('he worked overtime')

johnny_homework = True
johnny_throw_out_garbage = True
if johnny_homework and johnny_throw_out_garbage:
	print('Johnny can play Xbox-One')

print not(johnny_homework or not(johnny_throw_out_garbage))

# rock paper scissors
human = 'rock'
computer = 'scissors'
if human == 'rock' and computer == 'scissors':
	human_score = 1
print(human_score)

computer = 'bananas'
if human == 'rock' and computer == 'scissors':
	human_score = 1
elif human == 'rock' and computer == 'bananas':
	computer_score = 0
	human_score = 0
print('You cant pick anything other than rock paper scissors')



# if (CONDITION --> True):
# 	THIS BLOCK OF CODE RUNS
if human == 'rock' and computer == 'scissors':
	human_score = 1
elif human == 'rock' and computer == 'bananas':
	computer_score = 0
	human_score = 0
else: # else runs if the above two conditions are not met
# if human == 'bananas' or computer == 'bananas':
	print ()

if computer != 'rock' or computer != 'scissors' or computer != 'paper':
	print('WRONG CHOICE, PICK AGAIN!')

if computer != 'rock' and computer != 'scissors' and computer != 'paper':
	print('WRONG CHOICE, PICK AGAIN!')

computer = 'banana'
if computer != 'rock' and computer != 'scissors' and computer != 'paper':
	print('WRONG CHOICE, PICK AGAIN!')

