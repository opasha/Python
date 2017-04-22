class BankAccount:
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount
	
	def deposit(self, deposit_amount):
		self.amount += deposit_amount

	def withdrawal(self, withdrawal_amount):
		self.amount -= withdrawal_amount

	def __str__(self):
		return "{} Amount: {}".format(self.account_type, self.amount)


omar = BankAccount("Checkings", 100)
print(omar.account_type)
print(omar.amount)

omar.deposit(30)
print(omar.amount)

omar.withdrawal(45)
print(omar)
print(omar.amount)
