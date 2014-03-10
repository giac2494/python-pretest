def find_longest_word(words):
	max_len = 0
	for word in words:
		if len(word)>max_len:
			max_len = len(word)
	return max_len


def filter_long_words(words, n):
	words_len = [];
	for word in words:
		if(len(word) > n):
			words_len.append(word)
	return words_len


words = ["parola","casa","oggetto","bicicletta"]
print "part 1"
print find_longest_word(words)
print "part 2"
print filter_long_words(words, 6);
