print("PROGRAM MENGHITUNG NILAI RATA_RATA")
n = int(input("\nBanyaknya data: "))
print ()
data = []
jum = 0 
for i in range(0,n) :
    temp = int(input("Masukkan data ke-%d: "%(i+1)))
    data.append(temp)
    jum += data[i]
    rata_rata = jum/n
print("\nRata-rata = %0.2f" % rata_rata)