t = int(input());

for _ in range(t):
	n, k = list(map(int, input().split(' ')));
	max = 0;
	for i in range(2,k+1):
		c = n % i;
		if c >= max:
			max = c;

	print(max);
© 2020 GitHub, Inc.
