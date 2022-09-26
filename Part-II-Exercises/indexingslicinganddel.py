L = [2,5,1,4]
L[2] = [] # print [2, 5, [], 4]
# Giá trị của L[2] là 1 int hoặc 1 str
L[2:3] = [] # print [2, 5, 4]
# Giá trị của L[2:3] là 1 mảng


del L[1:]
# Xóa các index từ 1 trở đi. chỉ giữ lại index 0

L[1:2]=1
# Lỗi "can only assign an iterable". Nó chỉ gán được một mảng
