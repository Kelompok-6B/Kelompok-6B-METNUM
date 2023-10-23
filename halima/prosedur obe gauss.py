import numpy as np

#fungsi untuk mencetak matriks
def print_matrix(matrix):
    for row in matrix:
        print(row)

#fungsi untuk melakukan eliminasi Gauss
def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        #mencari elemen terbesar dalam kolom saat ini untuk pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        #menukar baris saat ini dengan baris dengan elemen terbesar
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        #membuat elemen diagonal menjadi 1
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        #menggunakan eliminasi untuk membuat semua elemen di bawah pivot menjadi 0
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    return matrix

#fungsi untuk menyelesaikan sistem persamaan linear
def back_substitution(matrix):
    n = len(matrix)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]

    return x

#input matriks koefisien dan vektor hasil dari pengguna
n = int(input("Masukkan ukuran matriks (n): "))
print("Masukkan matriks koefisien A:")
A = []
for i in range(n):
    row = [float(x) for x in input().split()]
    A.append(row)

print("Masukkan vektor hasil b:")
b = [float(x) for x in input().split()]

#menggabungkan matriks koefisien dengan vektor hasil
augmented_matrix = np.column_stack((A, b))

print("\nMatriks Awal:")
print_matrix(augmented_matrix)

#melakukan eliminasi Gauss
gaussian_elimination(augmented_matrix)

print("\nMatriks Setelah Eliminasi Gauss:")
print_matrix(augmented_matrix)

#menyelesaikan sistem persamaan linear
x = back_substitution(augmented_matrix)

#output solusi
print("\nSolusi:")
for i, val in enumerate(x):
    print(f"x{i+1} = {val}")
