def fibonacci(n):
	a, b = 0, 1
	for i in range (n):
		a, b = b, a + b
	return a
# 0, 1, 1, 2, 3, 5, 8
print(fibonacci(5))