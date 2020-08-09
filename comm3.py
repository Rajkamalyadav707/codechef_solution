import math;
def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2-y1)**2);

t = int(input());
for _ in range(t):
	r = int(input());

	cx, cy = list(map(int, input().split(' ')));
	hx, hy = list(map(int, input().split(' ')));
	sx, sy = list(map(int, input().split(' ')));

	dh = distance(cx, cy, hx, hy);
	ds = distance(cx, cy, sx, sy);
	dhs = distance(hx, hy, sx, sy);

	if dh <= r and ds <= r:
		print("yes");
	elif (dh <= r or ds <= r) and dhs <= r:
		print("yes");
	else:
		print("no");
