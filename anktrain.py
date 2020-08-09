t = int(input())
for i in range(0, t):
	num = int(input())
	k = num % 8
	if(k==0):
		print(str(num-1) + "SL")
	elif(k == 1):
		print(str(num+3) + "LB")
	elif(k == 2):
		print(str(num+3) + "MB")
	elif(k == 3):
		print(str(num+3) + "UB")
	elif(k == 4):
		print(str(num-3) + "LB")
	elif(k == 5):
		print(str(num-3) + "MB")
	elif(k == 6):
		print(str(num-3) + "UB")
	else:
		print(str(num+1) + "SU")
