t = int(input());

for _ in range(0 , t):
	num = int(input());
	sum = 0;
	while num != 0:
		d = num % 10;
		sum += d;
		num = int(num / 10);

	print(str(sum));
