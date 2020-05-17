import numpy as np

x = np.array([16, 21, 22, 18, 20])
y = np.array([[1, 5, 8], [2, 5, 1], [6, 3, 0]])

########################################################## NUMPY FUNCTIONS
print("FUNCTIONS ###############################################")
# PRINT ARRAY
print(y)

# DIMENSION OF ARRAY
print (y.shape)

# STANDARD DEVIATION
print (x.std())

# HIGHEST NUMBER
print(x.max())

# LOWEST NUMBER
print (x.min()) 

# AVERAGE 
print (x.mean())

# SQUARE ROOT
print (np.sqrt(625))

# SQUARE
print(np.square(15))

# SIN
print(np.sin(np.deg2rad(90)))

# COS
print(np.cos(np.deg2rad(90)))

# TAN
print(np.tan(np.deg2rad(90)))

# LOG
print(np.log(10000)) # LOG

print (np.log10(10000)) # LOG 10


##################################################################################### CREATING ARRAYS
print("CREATE ARRAYS ###############################################")
# REGULAR ARRAYS
print(np.arange(5, 20, 2)) # STARTS WITH 5, STOP AT 20, WITH INTERVALS OF 2

# ALL VALUES IN ARRAY ARE ONES
print(np.ones(5)) # 5 COLUMNS

print(np.ones((2, 4))) # TWO ROWS, 5 COLUMNS

print(np.ones((5), dtype = "int32")) # ALL VALUES ARE INT

# ALL VALUES IN ARRAY ARE ZERO
print(np.zeros(5))


####################################################################################### RANDOM 
print ("RANDOM ###############################################")
# RANDOM NUMBER BETWEEN 0 TO 1
print(np.random.rand(5)) # UNIFORMLY DISTRIBUTED

print(np.random.randn(5)) # NORMAL DISTRIBUTION MEAN = 0, STD = 1

# RANDOM INT
print(np.random.randint(5, 20)) # RANDOM 1 INT BETWEEN 5 AND 20

print(np.random.randint(5, 20, 5)) # RANDOM 5 INT BETWEEN 5 AND 20

print(np.random.randint(5, 20, (3, 2))) # RANDOM INT ARRAY 3 ROWS, 2 COLUMNS BETWEEN 5 AND 20

# PICK RANDOM VALUES FROM LIST
l = list("abcdefghijklmnopqrstuvwxyz")
print(np.random.choice(l)) # 1 VALUE

print(np.random.choice(l, 10)) # 10 VALUES


######################################################################################## LINEAR ALGEBRA
print ("LINEAR ALGREBRA ###############################################")

#  equation :
#  3x - 5y = 5
#  4x + 2y = 24


a = [[3, -5], [4, 2]] # VALUE BEFORE VARIABLE
b = [5, 24] # RESULT OF EQUATION

print(np.linalg.solve(a, b))

############################################################################################ MATRIX
print ("MATRIX ###############################################")
# SOURCE : 
# https://www.programiz.com/python-programming/matrix

# CREATE A MATRIX
m = np.matrix([[7, 4, 2], [3, 5, 6], [8, 2, 3]])

# INVERSE OF MATRIX
print(np.linalg.inv(m))

# DETERMINANT OF MATRIX
print(np.linalg.det(m))

# MATRIX OPERATIONS
m1 = np.array([[10, 20, 30], [209, 231, 381]])
m2 = np.array([[26, 32, 39], [201, 523, 101]])

m3 = np.array([[10, 20, 30], [29, 39, 21]])
m4 = np.array([[26], [32], [39]])
m5 = np.array([13])

# ADD MATRICES
print(m1 + m2)

# MULTIPLY MATRICES
print(m3.dot(m4)) # 2 MATRICES

print(m3.dot(m4).dot(m5)) # 3 MATRICES

# TRANSPOSE MATRIX
print(m1.transpose())




