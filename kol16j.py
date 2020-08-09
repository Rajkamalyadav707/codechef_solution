t = int(input());

for i in range(t):
	n = int(input());
	chapters = list(map(int, input().split(' ')));


	s_ch = sorted(chapters);

	if chapters == s_ch:
		print("no");
	elif s_ch != list(range(1, n+1)):
		print("no");
	else:
		print("yes");
