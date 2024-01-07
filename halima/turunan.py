# mendefinisikan fungsi untuk selisih maju
def hitung_selisih_maju(fx, h, indeks):
    return (fx[indeks + 1] - fx[indeks]) / h


# mendefinisikan fungsi untuk selisih mundur
def hitung_selisih_mundur(fx, h, indeks):
    return (fx[indeks] - fx[indeks - 1]) / h


# mendefinisikan fungsi untuk selisih pusat
def hitung_selisih_pusat(fx, h, indeks):
    return (fx[indeks + 1] - fx[indeks - 1]) / (2 * h)


# input untuk memasukkan data
n = int(input("Masukkan jumlah titik data: "))
x = []
fx = []

for i in range(n):
    xi = float(input(f"Masukkan x[{i}]: "))
    fxi = float(input(f"Masukkan f(x)[{i}]: "))
    x.append(xi)
    fx.append(fxi)

# Mendapatkan input pengguna untuk indeks di mana turunan dihitung dan nilai h
indeks = int(input("Masukkan indeks turunan yang akan dihitung: "))
h = float(input("Masukkan nilai h: "))

# Menghitung turunan menggunakan metode selisih maju, selisih mundur, dan selisih pusat
selisih_maju = hitung_selisih_maju(fx, h, indeks)
selisih_mundur = hitung_selisih_mundur(fx, h, indeks)
selisih_pusat = hitung_selisih_pusat(fx, h, indeks)

# Menampilkan hasil turunan
print("Hasil turunan menggunakan metode selisih maju:", selisih_maju)
print("Hasil turunan menggunakan metode selisih mundur:", selisih_mundur)
print("Hasil turunan menggunakan metode selisih pusat:", selisih_pusat)
