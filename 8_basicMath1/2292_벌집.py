n = int(input())
compare = 1
idx = 1
while 1:
	if n > compare:
		compare += (6 * idx)
		idx += 1
	else:
		print(idx)
		break
