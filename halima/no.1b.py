import math

def f(x):
    return math.exp(x) - x

def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Interval [a, b] tidak memenuhi syarat metode bagi dua.")
        return None

    iteration = 0
    while (b - a) / 2.0 > tol and iteration < max_iter:
        mid = (a + b) / 2.0
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        iteration += 1

    return (a + b) / 2.0

# Menentukan interval awal [a, b], toleransi, dan maksimum iterasi
a = 0.0
b = 1.0
toleransi = 0.001
max_iterasi = 3

hasil_akar = bisection_method(a, b, toleransi, max_iterasi)

if hasil_akar is not None:
    print(f"Akar dari fungsi adalah {hasil_akar:.3f}")
else:
    print("Metode tidak konvergen atau iterasi mencapai batas maksimum.")
