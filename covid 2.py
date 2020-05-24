print('Masukkan data orang positif corona (dalam angka): ', end = " ")
a = int(input())
nama = []

for positif in range(a):
    print('Nama orang ke ', positif + 1, end = " ")
    nama.insert(positif, input())
    
print('\n')

print('Masukkan data orang random (dalam angka): ', end = " ")
b = int(input())
nama2 = []
for random in range(b):
    print('Nama orang ke ', random + 1, end = " ")
    nama2.insert(random, input())

print('\n')

relasi = []
print('Pernah berinteraksi atau tidak (1 untuk pernah dan 0 untuk tidak)')
for hubungan in range (len(nama)):
    print('Apakah '+nama[hubungan], 'pernah berinteraksi dengan ')
    for hubungan2 in range (len(nama2)):
        print(nama2[hubungan2], end = " ")
        z = int(input())
        if z == 1:
            relasi.insert(hubungan2, nama2[hubungan2])
            print(nama2[hubungan2], "kemungkinan PDP atau ODP\n")
        else:
            print('\n')
    
PDP = set(relasi)

print('Positif corona', nama)
print('Kemungkinan PDP atau ODP', PDP)

