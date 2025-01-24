# Hình trái tim dựa vào tọa độ từ hình vẽ
for i in range(9):  # Duyệt qua từng hàng (từ 0 đến 8)
    for j in range(9):  # Duyệt qua từng cột (từ 0 đến 8)
        # Điều kiện các ô cần in *
        if (i == 1 and j in [2, 3, 5, 6]) or \
           (i == 2 and j in [1, 4, 7]) or \
           (i == 3 and j in [1, 7]) or \
           (i == 4 and j in [2, 6]) or \
           (i == 5 and j in [3, 5]) or \
           (i == 6 and j == 4):
            print('*', end='  ')  # In dấu * trên cùng hàng
        else:
            print(' ', end='  ')  # In dấu cách để căn chỉnh
    print()  # Xuống dòng sau mỗi hàng




"""# Vẽ cây thông Giáng Sinh không dùng NumPy
for i in range(1, 16, 2):  # Tầng cây từ 1 đến 15, cách 2 để tăng số "*"
    print(' ' * ((15 - i) // 2) + '*' * i)  # Căn giữa các tầng

# Vẽ thân cây
for _ in range(3):  # Thân cây cao 3 dòng
    print(' ' * 6 + '||')  # Căn giữa thân cây

# Vẽ chân đế
print(' ' * 3 + '\\=====/')
"""
