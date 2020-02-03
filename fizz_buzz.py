def fizz_buzz(div_num):
	
	if div_num % 3 == 0:
		if div_num % 5 == 0:
			return "FizzBuzz" 
		return "Fizz"
	if div_num % 5 == 0:
		return "Buzz"
	else: 
		return div_num

div_num = int(input("input number: "))

print(fizz_buzz(div_num))