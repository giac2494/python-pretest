in_f = open("words.txt","rb")
out_f = open("words_count.txt","wb")

i = 1
for line in in_f:
	out_f.write(str(i) + ") " + line)
	i+= 1

in_f.close()
out_f.close()