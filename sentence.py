def count_sentence(word):
	word_count = 0
	for i in word:
		word_count += 1
	return word_count

count_input = input("please input text: ")
print(count_sentence(count_input))