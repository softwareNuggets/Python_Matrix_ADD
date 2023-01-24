#A Matrix
A = [[1, 2],
     [3, 4]]

#B Matrix
B = [[5, 6],
     [7, 8]]

#B matrix is where we will store the result
R = [[0, 0],
     [0, 0]]

#r = row, all rows begin with 0
#c = column, all columns begin with 0

R[0][0] = A[0][0]+B[0][0]
print(R[0][0])


R[0][1] = A[0][1]+B[0][1]
print(R[0][1])

# r  c       r c     r c
R[1][0] = A[1][0]+B[1][0]
print(R[1][0])

# r  c       r c     r c
R[1][1] = A[1][1]+B[1][1]
print(R[1][1])
