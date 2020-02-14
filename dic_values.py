input_num = int(input("please input fields num: "))
all_values = {}

for i in range(input_num):
    user_input_key = input("please input your user key: ")
    user_input_value = input("please input your user value: ")
    all_values[user_input_key] = user_input_value

print(all_values)