L = [0,1,2,3]

#a. Lỗi "IndexError: list index out of range" vì list không có chỉ mục thứ 4
print(L[4])

#b. Vì list L nằm trong đoạn [-1000:100]
print(L[-1000:100]) #print [0, 1, 2, 3]

#c. 
L[3:1]=['?']
print(L) # print [0, 1, 2, '?', 3]
