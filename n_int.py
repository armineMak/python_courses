def int_num(n_num):
	x = (int(str(n_num) + str(n_num))) + (int(str(n_num) + str(n_num) + str(n_num))) 
	return x + n_num

n_num = int(input("please input something: "))

print(int_num(n_num))