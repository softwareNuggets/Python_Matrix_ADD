import numpy as np;


#Matrix A
A = np.array([
                [1,2],
                [3,4]],dtype=int)

#Matrix B
B = np.array([[5,6],
              [7,8]],dtype=int)


#Matrix Add
R = np.add(A,B);


#Show Results
print(A, end='\n\n')
print(B, end='\n\n')
print(R, end='\n\n')

