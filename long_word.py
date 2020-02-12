# long_word_list = ["test", "bulkijgbdvfdbgfghf", "xachapuri", "ansahman"]
# long_word_list.sort( key = len )
# print(long_word_list[-1])

long_word_list = ["test", "bulkijgbdvfdbgfghf", "xachapuri", "ansahman", "sgfbdsmfdmsbnfmbdnmfbmndbmnfbmdnbfb"]

def find_longest_word(long_word_list):

    d = []
    for c in long_word_list:
        d.append(len(c))
        e = max(d) 
    for b in long_word_list:
        if len(b) == e:
            print("the longest word is:", b)

find_longest_word(long_word_list)