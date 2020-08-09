t = int(input());

for i in range(t):
	n = int(input());
	am = []; # encoded array of a and b
	for _ in range(n):
		am.append(int(input()))

	a = [];
	b = [];
	for num in am:
		a.append(int(65535 & num));
		b.append(int(num >> 16));
	print("Case " + str(i+1) + ":");
	print(*a);
	print(*b);
