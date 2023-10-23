def lagrange_interpolation(x_values, y_values, x):
    result = 0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

#input
n = int(input("Masukkan jumlah titik data: "))

x_values = []
y_values = []

for i in range(n):
    x = float(input(f"Masukkan nilai x-{i + 1}: "))
    y = float(input(f"Masukkan nilai y-{i + 1}: "))
    x_values.append(x)
    y_values.append(y)

x_interpolate = float(input("Masukkan nilai x untuk diinterpolasi: "))

#menggunakan fungsi interpolasi
result = lagrange_interpolation(x_values, y_values, x_interpolate)
print(f"Interpolasi pada x = {x_interpolate} adalah {result}")
