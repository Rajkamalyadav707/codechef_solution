t = input();
for x in range(0, t):
	 # read input
	 n = int(input())
	 triangle = [];
	 for i in range(0, n):
	 	row = [];
	 	for i in raw_input().split():
	 		row.append(int(i));
	 	triangle.append(row);

	 # we start from the last row and first column
	 # if the current column is j and row is i
	 # we choose between the number at [i][j] and [i][j-1]
	 # which will be added to [i-1][j]
	 for i in range(len(triangle)-1, -1, -1):
	 	for j in range(i):
	 		if(triangle[i][j] > triangle[i][j+1]):
	 			triangle[i-1][j] += triangle[i][j];
	 		else:
	 			triangle[i-1][j] += triangle[i][j+1];



	 print triangle[0][0];
