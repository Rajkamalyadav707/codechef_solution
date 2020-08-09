t = int(input())
for x in xrange(0,t):
	act = raw_input()
	newact = ""
	for i in act:
		if i == "<":
			i = ">"
		elif i == ">":
			i = "<"
		newact += i

	print(str(newact.count("><")))
