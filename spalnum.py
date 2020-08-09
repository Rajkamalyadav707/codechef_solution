# def isPalindrom(num):
# 	rev = 0;
# 	n = num;
# 	while num != 0:
# 		d = num % 10;
# 		rev = rev*10 + d;
# 		num = int(num/10);

# 	if n == rev:
# 		return True;
# 	else:
# 		return False;

def isPalindrom(num):
	str_num = str(num);
	return str_num == str_num[::-1];


t = int(input());

for _ in range(t):
	sump = 0;
	left , right = list(map(int, input().split(' ')));
	for n in range(left, right+1):
		if isPalindrom(n):
			sump += n;

	print(sump);
