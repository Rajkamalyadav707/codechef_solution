t = int(input());
for _ in range(0, t):
	x, y = list(map(int, input().split(' ')));
	minimum = max(x,y);
	maximum = x + y;

	print(str(minimum) + " " + str(maximum));
