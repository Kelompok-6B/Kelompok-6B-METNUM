def f(x):
    return x**3 - 2*x + 1 #fungsi yang diberikan

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Interval [a, b] tidak memenuhi syarat metode bagi dua.")
        return None

    while (b - a) / 2> tol:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

# Menentukan interval awal [a, b] dan toleransi
a = -2
b = 2
toleransi = 0.001

hasil_akar = bisection_method(a, b, toleransi)

if hasil_akar is not None:
    print(f"Akar dari fungsi adalah {hasil_akar:.3f}") 
