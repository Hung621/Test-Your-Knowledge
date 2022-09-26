import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:2d}'.format(secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t -= 1
    print("\n\n\n\n\n")
    for i in range(5,0,-1):
        print(i)

t=int(input("Nhap so giay bat dau dem nguoc : "))
countdown(t)
