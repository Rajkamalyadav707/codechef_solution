def hasFour(num):
	str_n = str(num);
	return str_n.count('4');

t = int(input());

for _ in range(t):
	n = int(input());
	print(str(hasFour(n)));
