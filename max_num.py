def max_num(num1, num2, num3):
	
	if num1 >= num2:
		if num1 >= num3:
			return num1
		return num3
	if num2 >= num3:
		return num2
	return num3

num1 = int(input("please input your number1: "))
num2 = int(input("please input your number2: "))
num3 = int(input("please input your number3: "))

print(max_num(num1, num2, num3))
