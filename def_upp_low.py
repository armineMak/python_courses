user_input = input("input some text: ")

def check_alphanumeric(some_input, is_upper=False, is_low=False, is_digit=False):

	for i in some_input:
		if i.isupper():
			is_upper = True
		elif i.islower():
			is_low = True
		elif i.isdigit():
			is_digit = True	

	if is_upper is True and is_low is True and is_digit is True:
		print("it's contains upper, lower and digits")
	elif is_upper is True and is_low is True:
		print("it's contains upper and lower")
	elif is_upper is True and is_digit is True:
		print("it's contains upper and digit")
	elif is_low is True and is_digit is True:
		print("it's contains lower and digit")
	elif is_digit is True:
		print("it's digit")	 
	elif is_low is True:
		print("it's low")
	elif is_upper is True:
		print("it's upper")
	else:
		print("error")

check_alphanumeric(user_input)

while True:
	try: 
		digit_input = int(input("input some digits: "))
		print("it's digit")
		break
	except ValueError:
		print("input only digits")


