import os
import sys

#modul
def tampilkanMenu():
    print("1. Tambahkan Kontak")
    print("2. Cari Kontak")
    print("3. Hapus Kontak")
    print("4. Update Kontak")
    print("5. Tampilkan Semua Kontak")
    print("99. Keluar Program")
    pilih = int(input("Pilih Menu : "))
    pilihMenu(pilih)

def pilihMenu(pilih):
    match pilih:
        case 1:
            tambahKontak()
        case 2:
            cariKontak()
        case 3:
            hapusKontak()
        case 4:
            updateKontak()
        case 5:
            tampilkanSemuaKontak()
        case 99:
            sys.exit("Terima Kasih")
        case other:
            print("Pilihan Menu Tidak Valid")
            tampilkanMenu()

def tambahKontak():
    nama = input("Masukan nama : ")
    nomor = input("Masukan Nomor : ")
    file = open("phoneBook.txt", "a")
    file.write(nama+" "+nomor+"\n")
    file.close()
    tampilkanMenu()

def tampilkanSemuaKontak():
    print("No".ljust(3,' ')+"Nama".ljust(25, ' ') + "Nomor")
    i = 1
    file = open("phoneBook.txt", "r")
    for line in file:
        simpan = line.split(" ")
        print (str(i) + ". " + simpan[0].ljust(25,' ') + simpan[1][:-1])
        i = i + 1
    file.close()
    tampilkanMenu()
    
def cariKontak():
    file = open("phoneBook.txt", "r")
    print("Cari Berdasarkan : ")
    print("1. Nama")
    print("2. Nomor Hp")
    pilih = int(input("Masukan Pilihan : "))
    if (pilih == 1):
        nama = input("Masukan nama yang di cari : ")
    elif (pilih == 2):
        nomor = input("Masukan nomor yang di cari : ")
    ketemu = False
    for line in file:
        simpan = line.split(" ")
        if(not ketemu):
            if(pilih == 1):
                if(simpan[0] == nama):
                    ketemu = True
                    break
            else:
                if(simpan[1][:-1] == nomor):
                    ketemu = True
                    break
    if (ketemu):
        print("Nama : "+simpan[0]+"\nNomor : "+simpan[1][:-1])
    else:
        print("Data Tidak Ditemukan")
    file.close()
    tampilkanMenu()

def hapusKontak():
    file = open("phoneBook.txt", "r")
    data = file.readlines()
    file.close()
    print("Cari Berdasarkan : ")
    print("1. Nama")
    print("2. Nomor Hp")
    pilih = int(input("Masukan Pilihan : "))
    if (pilih == 1):
        nama = input("Masukan nama yang di cari : ")
    elif (pilih == 2):
        nomor = input("Masukan nomor yang di cari : ")
    index = -1
    for i in range(len(data)):
        temp = data[i].split(" ")
        if(pilih == 1):
            if(temp[0] == nama):
                index = i
                break
        elif(pilih == 2):
            if(temp[1][:-1] == nomor):
                index = i
                break
    if(index != -1):
        path = "C:\Kuliah\Semester 2\Python\Pertemuan 5/phoneBook.txt"
        os.remove(path)
        file = open("phoneBook.txt", "a")
        for i in range(len(data)):
            if(i != index):
                file.write(data[i])
        file.close()
    else:
        print("Data yang dicari tidak ada")
    tampilkanMenu()

def updateKontak():
    file = open("phoneBook.txt", "r")
    data = file.readlines()
    file.close()
    nama = input("Masukan Nama Orang yang Ingin Nomornya diubah : ")
    index = -1
    for i in range(len(data)):
        temp = data[i].split(" ")
        if(temp[0] == nama):
            index = i
            break
    if(index != -1):
        path = "C:\Kuliah\Semester 2\Python\Pertemuan 5/phoneBook.txt"
        os.remove(path)
        nomor = input("Masukan Nomor Pengganti : ")
        data[index] = nama + " " + nomor + "\n"
        file = open("phoneBook.txt", "a")
        for i in range(len(data)):
            file.write(data[i])
        file.close()
    tampilkanMenu()
        
#main
tampilkanMenu()

