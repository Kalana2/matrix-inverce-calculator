
a = [
    [1, 2, 1],
    [3, 4, 1],
    [5, 5, 4]
]

def determinant (a):
    if(len(a) == 2):
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
     
    totalDet = 0
    for col in range(len(a)):

        minor = [row[:col] + row[col+1:] for row in a[1:]]

        sign = (-1)**col
        totalDet += sign * a[0][col] * determinant(minor)
    
    return totalDet


