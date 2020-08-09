import math;

t = int(input());

for _ in range(t):
	b, ls = list(map(int, input().split(' ')))

	min = math.sqrt(ls ** 2 - b ** 2);

	max = math.sqrt(b ** 2 + ls ** 2);

	print("{0:.5f}".format(min) + ' ' + "{0:.5f}".format(max));
