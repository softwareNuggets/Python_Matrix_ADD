#A Matrix
A = [[1, 2],
     [3, 4]]

#B Matrix
B = [[5, 6],
     [7, 8]]

#R matrix is where we will store the result
R = [[0, 0],
     [0, 0]]

#r = row, all rows begin with 0
#c = column, all columns begin with 0

for r in range(2):
    for c in range(2):
        R[r][c] = A[r][c] + B[r][c]

print(A, end='\n\n')
print(B, end='\n\n')
print(R, end='\n\n')
