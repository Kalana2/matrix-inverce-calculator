

def determinant (a):
    if(len(a) == 2):
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
     
    totalDet = 0
    for col in range(len(a)):

        minor = [row[:col] + row[col+1:] for row in a[1:]]

        sign = (-1)**col
        totalDet += sign * a[0][col] * determinant(minor)
    
    return totalDet



def cofactor (a):
    if(len(a)  == 2):
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
      

    cofactorMatrix = []

    for row in range(len(a)):
        cofactorRow = []
        for col in range(len(a)):
                
            minor = [r[:col] + r[col+1:] for r in (a[:row] + a[row + 1:])]

            minorDet = determinant(minor)

            sign = (-1)**(row + col)
                
            cofactorRow.append(sign * minorDet)
    
        cofactorMatrix.append(cofactorRow)

    return cofactorMatrix



def inverse(a):

    determinantOfMatrix = determinant(a)

    if (determinantOfMatrix == 0 ):
        raise Exception("Matrix is singular, Does not exits inverse.")
    
    cofactorMatrix = cofactor(a)
    adjointMatrix = [[0] * len(a) for _ in range(len(a))] 
 
    #calculate ajoint matrix
    for row in range(len(a)):
        for col in range(len(a)):
            adjointMatrix[col][row] = cofactorMatrix[row][col]

    inverseMartix = [[adjointMatrix[row][col]/determinantOfMatrix for col in range(len(a))] for row in range(len(a))]

    return inverseMartix


def displayMatrix(matrix):
    numberOfRows = len(matrix)

    for row in range(numberOfRows):
        print(matrix[row])

        

def getInput():
    row_count = int(input("Enter number of Rows: "))
    col_count = int(input("Enter number of Cols: "))
    
    print(f"Matrix dimensions: {row_count} x {col_count}")
    
    matrix = [[0 for _ in range(col_count)] for _ in range(row_count)]
    
    print("Enter the matrix values:\n")
    for row in range(row_count):
        for col in range(col_count):
            print(f"Enter value for position ({row}, {col}): ", end="")
            matrix[row][col] = int(input())
    
    print("Final Matrix:")
    for row in matrix:
        print(row)
    return matrix


    
a = [
    [1, 2, 1],
    [3, 4, 1],
    [5, 5, 4]
]

b = [
    [1,1,0],
    [2,3,0],
    [5,6,0]
]


try:
    matrix = getInput()
    matrix = inverse(matrix)
    print("\n\n Output \n ")
    displayMatrix(matrix)

except Exception as error:
    print(error)
