# Nhập số phần tử
n = int(input("Nhập số phần tử của mảng: "))

# Nhập mảng 1
a = list(map(int, input("Nhập mảng 1: ").split()))

# Nhập mảng 2
b = list(map(int, input("Nhập mảng 2: ").split()))

# Kiểm tra độ dài
if len(a) != n or len(b) != n:
    print("Số phần tử không hợp lệ!")
else:
    # Cộng 2 mảng
    c = []
    for i in range(n):
        c.append(a[i] + b[i])

    print("Mảng kết quả:", c)
