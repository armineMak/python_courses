input_str = input("please input smth: ")

first_el = input_str[0]
new_str = input_str.replace(first_el, "$")
print(first_el + new_str[1:])