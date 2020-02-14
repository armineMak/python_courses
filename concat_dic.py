dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

concat_dic = {}
# concat_dic.update(dic1)
# concat_dic.update(dic2)
# concat_dic.update(dic3)

for i in [dic1, dic2, dic3]:
	concat_dic.update(i)

# key_check
some_input = int(input("input something: "))

if some_input in concat_dic: 
	print("your key is:", some_input)
else:
	print("we didn't find your key")

# min/max values
min_val = min(concat_dic.values())
max_val = max(concat_dic.values())
print("your max val is: ", max_val," " + " ","and min val is:", min_val)

print(concat_dic)

