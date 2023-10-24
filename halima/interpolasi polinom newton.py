def newton_interpolasi(x_values, y_values, x):
    n = len(x_values)
    koefisien = y_values.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            koefisien[i] = (koefisien[i] - koefisien[i - 1]) / (x_values[i] - x_values[i - j])

    result = koefisien[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (x - x_values[i]) + koefisien[i]

    return result

def inputan_user():
    n = int(input("Masukkan jumlah titik data: "))

    x_values = []
    y_values = []

    for i in range(n):
        x = float(input(f"Masukkan nilai x-{i + 1}: "))
        y = float(input(f"Masukkan nilai y-{i + 1}: "))
        x_values.append(x)
        y_values.append(y)

    x_interpolasi = float(input("Masukkan nilai x untuk diinterpolasi: "))

    return x_values, y_values, x_interpolasi

def main():
    x_values, y_values, x_interpolasi = inputan_user()

    result = newton_interpolasi(x_values, y_values, x_interpolasi)
    print(f"Interpolasi pada x = {x_interpolasi} adalah {result}")

if _name_ == "_main_":
    main()
