jenis_bahan = ["MPPF FORM 5x1000x900mm","CONTROL HORN","PUSH ROD WIRE","BRUSHLESS MOTOR","LINKAGE STOPPER","ESC(SW50A)","Receiver(iA108 12x)","Carbon fiber rod 3mm","Servo 9g","RC Lipo Battery","PROPELLER!","flysky-16X REMOTE CONTROL"]
harga_barang = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("HARGA BARANG MPPF FORM 5x1000x900mm,CONTROL HORN,PUSH ROD WIRE,BRUSHLESS MOTOR,LINKAGE STOPPER,ESC(SW50A),Receiver(iA108 12x),Carbon fiber rod 3mm,Servo 9g,RC Lipo Battery,PROPELLER!,flysky-16X REMOTE CONTROL")
a=int(input("Masukkan tempahan untuk MPPF FORM:"))
b=int(input("Masukkan tempahan untuk CONTROL HORN:"))
c=int(input("Masukkan tempahan untuk PUSH ROD WIRE:"))
d=int(input("Masukkan tempahan untuk BRUSHLESS MOTOR:"))
e=int(input("Masukkan tempahan untuk LINKAGE STOPPER:"))
f=int(input("Masukkan tempahan untuk ESC(SW50A):"))
g=int(input("Masukkan tempahan untuk RECEIVER(iA108 Rx):"))
h=int(input("Masukkan tempahan untuk CARBON FIBER ROD 3mm:"))
j=int(input("Masukkan tempahan untuk SERVO 9g:"))
k=int(input("Masukkan tempahan untuk RC LIPO BATTERY:"))
l=int(input("Masukkan tempahan untuk PROPELLER!:"))
m=int(input("Masukkan tempahan untuk flysky-16X REMOTE CONTROL:1"))

tempahan = [a,b,c,d,e,f,g,h,j,k,l,m]

def jumlah_harga():
    for i in range(12):
        jumlah[i] = harga_barang[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"bahan",jenis_bahan[0])
    print(b,"bahan",jenis_bahan[1])
    print(c,"bahan",jenis_bahan[2])
    print(d,"bahan",jenis_bahan[3])
    print(e,"bahan",jenis_bahan[4])
    print(f,"bahan",jenis_bahan[5])
    print(g,"bahan",jenis_bahan[6])
    print(h,"bahan",jenis_bahan[7])
    print(j,"bahan",jenis_bahan[8])
    print(k,"bahan",jenis_bahan[9])
    print(l,"bahan",jenis_bahan[10])
    print(m,"bahan",jenis_bahan[11])

    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()