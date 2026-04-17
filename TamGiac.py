# Nhập chiều cao
n = int(input("Nhập chiều cao tam giác: "))

for i in range(1, n + 1):
    # In khoảng trắng
    print(" " * (n - i), end="")
    # In dấu *
    print("*" * (2 * i - 1))
