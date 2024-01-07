import numpy as np  # memanggil library numpy
import math  # memanggil library math supaya program dapat mengenal bilangan euler ('e')

e = math.e  # digunakan jika user menginput e sebagai bilangan euler pada fungsi


def inputFungsi():  # mendefinisikan fungsi yang diinputkan user
    fungsi = input("Masukkan f(x): ")
    return lambda x: eval(fungsi)


def inputBatas():  # mendefinisikan batas bawah dan batas atas integral yang diinputkan user
    a = float(input("Masukkan batas bawah integral: "))
    b = float(input("Masukkan batas atas interval: "))
    return a, b


def inputPartisi():  # mendefinisikan jumlah partisi
    n = int(input("Masukkan jumlah partisi: "))
    return n


f = inputFungsi()
a, b = inputBatas()
n = inputPartisi()


# mendefinisikan fungsi untuk metode trapesium
def trapesium(f, a, b, n):
    # mendapatkan interval
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    # menjumlahkan interval
    trap = f(x[0]) + f(x[n])
    for i in range(1, n):
        trap += 2 * f(x[i])
    trap = (h / 2.0) * trap
    return trap


# mendefinisikan fungsi untuk metode simpson 1/3
def simpson(f, a, b, n):
    # interval harus genap untuk metode simpson 1/3
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    # menjumlahkan interval
    simp = f(x[0]) + f(x[n])
    for i in range(1, n):
        if i % 2 == 0:
            w = 2
        else:
            w = 4
        simp += w * f(x[i])
    simp = (h / 3.0) * simp
    return simp


def titikTengah(f, a, b, n):
    # mendapatkan interval
    h = (b - a) / n
    tengah = 0
    for i in range(n):
        x_tengah = a + (i + 0.5) * h
        tengah += f(x_tengah)
    tengah *= h
    return tengah


# call integration routines
trap = trapesium(f, a, b, n)
simp = simpson(f, a, b, n)
tengah = titikTengah(f, a, b, n)


# Menampilkan hasil integrasi
print("Hasil integrasi menggunakan metode trapesium: ", trap)
print("Hasil integrasi menggunakan metode Simpson 1/3: ", simp)
print("Hasil integrasi menggunakan metode titik tengah: ", tengah)
