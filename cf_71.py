n = int(input()) #masukan n yang merupakan banyak perulangan nantinya

for i in range(0,n): #disini kita masukan range dari 0 - ke-n
    x = str(input()) #masukan kata yang mau dibuat ke singkatan
    l = len(x)
    if l > 10:
        print(x[0],end='')
        print(l-2,end='')
        print(x[l-1])
    else:
        print(x)