# Librería de matemáticas
# Paola De León

# Matriz de indentidad

def identidad(num):
    identity = []
    iPos = 1
    for i in range(num*num):
        row = []
        if len(identity)%num != 0:
            if (iPos%num) == 0:
                row.append(1)
            else:
                row.append(0)
            iPos = iPos + 1
        else:
            identity.append(row)
            row = []

    return identity


def matrixMultiplication (A, B):
    '''
        Multiplicación de matrices
            m1: Primera matriz
            m2: Segunda matriz
            res: Matriz resultante
    '''
    result = [[(sum(a * b for a, b in zip(B_row, A_col)))
                            for A_col in zip(*B)]
                                for B_row in A]
    return result

def defineMatrix (rowCount, colCount, dataList):
    '''
        Función para definir una matriz.
            rowCount: Cantidad de filas
            colCount: Cantidad de columnas
            dataList: Lista con los datos.
            mat: Matriz resultante.
    '''
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat

def multiplyVectorMatrix(M, v):
    '''
        Función para mutiplicar un vector por una matriz.
            v: Vector
            M: Matriz como una lista de list.
            result: Matriz resultante.
    '''
    # Comprobar que se pueda multiplicar
    if len(M[0]) != len(v):
        # No se puede multiplicar
        return None
    res = []

    # Si se puede multiplicar
    for i in range(len(M)):
        suma = 0
        for j in range(len(M[0])):
            suma += M[i][j]*v[j]
        res.append(suma)

    return res