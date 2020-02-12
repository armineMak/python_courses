# 1
# file1 = open("text_doc.txt", "r")

# name = []
# rating = []
# lang_list = []

# for i in file1:
# 	x = i.split()

# 	name.append(x[0])
# 	rating.append(x[1])

# print(name)
# print(rating)

# file1.close()

# # 2


file_doc = open("text_doc.txt", "r")
file_doc2 = open("text_doc1.txt", "w")

names = []
ratings = []
languages = ["en", "ru", "hy", "en", "ru", "hy", "en", "ru", "hy", "en"]

for i in file_doc:
	x = i.split()

	names.append(x[0])
	ratings.append(x[1])

str_prop = ""
for i in range(10):
	str_prop += str(names[i]) + " " + str(languages[i]) + " " + str(ratings[i]) + "\n"

file_doc2.write(str_prop)
file_doc.close()
file_doc2.close()