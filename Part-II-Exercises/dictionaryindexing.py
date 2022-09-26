D = {"a":"", "b":"", "c":""}
D['d'] # Lỗi
D['d'] = 'spam' # Chương trình được chạy.
print(D) # {'a': '', 'b': '', 'c': '', 'd': 'spam'}
# Khi muốn gán thêm một phần tử của Dictionary thì phải có cả key và value
