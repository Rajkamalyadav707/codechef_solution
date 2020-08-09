def findLargestMenu(num):
	for i in range(11,-1,-1):
		if 2**i <= num:
			#print("Trying: " + str(i));
			return 2**i;
	return 1;

t = int(input());
for x in range(0, t):
	num = int(input());
	sum = 0;
	while num > 0:
		m = findLargestMenu(num);
		#print("choosing: " + str(m));
		sum += 1;
		num = num - m;
	print(sum);
