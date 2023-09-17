#library
import math
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk mencari akar
def f(x):
    return eval(user_function)

# Metode bagi dua
def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Interval [a, b] tidak memenuhi syarat metode bagi dua.")
        return None

    x_values = []
    iteration = 0
    while iteration < max_iter:
        mid = (a + b) / 2.0
        x_values.append(mid)
        if f(mid) == 0 or (b - a) / 2.0 < tol:
            return mid, x_values
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        iteration += 1

    return (a + b) / 2.0, x_values

# Input fungsi dari pengguna
user_function = input("Masukkan fungsi (gunakan x sebagai variabel): ")
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
toleransi = float(input("Masukkan toleransi: "))
max_iterasi = int(input("Masukkan jumlah maksimum iterasi: "))

# Mencari akar dengan metode bagi dua
root, x_values = bisection_method(a, b, toleransi, max_iterasi)

if root is not None:
    print(f"Akar dari fungsi adalah {root:.6f}")

    # Menyiapkan data untuk plot grafik
    x = np.linspace(a, b, 100)
    y = [f(xi) for xi in x]

    # Menampilkan grafik fungsi dan akar yang ditemukan
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=user_function)
    plt.scatter(x_values, [f(xi) for xi in x_values], color='red', label='Akar')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Grafik Fungsi dan Akar')
    plt.grid(True)
    plt.show()
else:
    print("Metode tidak konvergen atau iterasi mencapai batas maksimum.")
