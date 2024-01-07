import math  # memanggil library math supaya program dapat mengenal bilangan euler ('e')

e = math.e


def f(x):
    return e**x - 5 * (x**2)  # mendefinisikan fungsi f(x) dari contoh soal


def g(x):
    return e**x - 10 * x  # mendefinisikan fungsi g(x) dari contoh soal


akar = 0  # inisialsisasi nilai akar


def newtonRaphson(a, eps, f, g, N):
    # memproses pencarian akar
    if g(a) != 0:
        i = 1
        while i <= N:
            # terus lakukan iterasi jika i masih belum sama dengan N
            c = a - (f(a) / g(a))
            if abs(c - a) < eps or abs(f(c)) < eps:
                akar = c
                # hasil akar dari pencarian iterasi ke-i
                print("Akar ke-", i, "=", akar)
                break
            else:
                akar = c
                # hasil akar dari pencarian iterasi ke-i
                print("Akar ke-", i, "=", akar)
            a = c
            i = i + 1
    else:
        print("g(x) = 0")


# mencari akar menggunakan fungsi newtonRaphson dengan memasukkan a, epsilon, f(x), g(x), dan N
newtonRaphson(1, 0.001, f, g, 4)
