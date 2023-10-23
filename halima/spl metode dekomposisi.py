import numpy as np

#fungsi untuk melakukan dekomposisi LU
def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U

#fungsi untuk menyelesaikan sistem persamaan linear
def solve_lu_system(L, U, b):
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    #menggunakan dekomposisi LU untuk menyelesaikan Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    #menggunakan dekomposisi LU untuk menyelesaikan Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x, y

#input ukuran matriks
n = int(input("Masukkan ukuran matriks (n): "))

#input matriks koefisien
A = np.zeros((n, n))
print("Masukkan matriks koefisien A:")
for i in range(n):
    A[i] = [float(x) for x in input().split()]

#input vektor hasil
b = np.zeros(n)
print("Masukkan vektor hasil b:")
b = [float(x) for x in input().split()]

#dekomposisi LU
L, U = lu_decomposition(A)

#menyelesaikan sistem persamaan linear
x, y = solve_lu_system(L, U, b)

#output
print("Matriks L:")
print(L)
print("\nMatriks U:")
print(U)
print("\nNilai x:")
print(x)
print("\nNilai y:")
print(y)
