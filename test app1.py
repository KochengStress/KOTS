import cmath
import math
import random

kalkulator = False
wordle = False
program = True
hasil = 0
while program:
    print("silakan pilih apa yang mau anda lakukan:")
    print("""1. Kalkulator \n2.  game""")
    aktivitas = int(input())
    if aktivitas == 1:
        kalkulator = True
        program = False
    elif aktivitas == 2:
        print("program belum tersedia")
    else:
        print("pilihan tidak tersedia, Coba lagi")
    while kalkulator:
        print("""1. Perkalian
2. pertambahan
3. Pembagian
4. pengurangan
5. pythagoras matematika (segitiga siku siku)
setelah memilih, masukkan angka pertama, kemudian angka kedua""")
        print("masukkan pilihan anda:")
        metode = int(input())
        if metode == 1:
            print("""Perkalian:
            masukkan angka pertama:""") #perkalian
            a_a = int(input())
            print("masukkan angka kedua:")
            b_a = int(input())
            hasil = a_a * b_a
        elif metode == 2:
            print("""Pertambahan:
            masukkan angka pertama:""") #pertambahan
            a_a = int(input())
            print("masukkan angka kedua:")
            b_a = int(input())
            hasil = a_a + b_a
        elif metode ==3:
            print("""Pembagian:
            masukkan angka pertama:""")
            a_a = int(input())
            print("masukkan angka kedua:")
            b_a = int(input())
            hasil = a_a / b_a
        elif metode == 4:
            print("""Pengurangan:
            masukkan angka pertama:""")#pengurangan
            a_a = int(input())
            print("masukkan angka kedua:")
            b_a = int(input())
            hasil = a_a - b_a
        elif metode == 5:
            print("""masukkan jenis sudur yang dicari:
1. Miring
2. Depan
3. Samping""")
            pythagoras = True
            while pythagoras:
                a_a = int(input())
                if a_a == 1:
                    pythagoras = False
                    a_ab = float(input('panjang depan:(cm)'))#pythagoras segitiga siku siku
                    a_ac = float(input('panjang samping:(cm)'))
                    a_ad = a_ab * a_ab
                    a_ae = a_ac * a_ac
                    a_af = a_ad + a_ae
                    hasil = cmath.sqrt(a_af)
                if a_a == 2:
                    pythagoras = False
                    a_ab = float(input ('panjang miring: (cm)'))
                    a_ac = float(input('panjang samping: (cm)'))
                    a_abb = a_ab * a_ab
                    a_acc = a_ac * a_ac
                    a_af = a_abb - a_acc
                    hasil = cmath.sqrt(a_af)
                if a_a == 3:
                    pythagoras = False
                    a_ab = float(input ('panjang miring: (cm)'))
                    a_ac = float(input ('panjang depan: (cm)'))
                    a_abb = a_ab * a_ab
                    a_acc = a_ac * a_ac
                    a_f = a_abb - a_acc
                    hasil = cmath.sqrt(a_f)
                elif a_a >= 4:
                    print("pilihan tak tersedia")
        elif metode >= 6:
            print("pilihan tak tersedia, coba lagi")
        print("hasil:")
        hasil_a = hasil
        print(hasil_a)
        lanjut = True
        while lanjut:
            kalkulator = input("apakah masih ingin melanjutkan?(y/n)")
            if kalkulator == "y":
                kalkulator = True
                lanjut = False
            elif kalkulator == "n":
                n = True
                while n:
                    kalkulator = False
                    print("apakah anda ingin melanjutkan program?(y/n)")
                    program = input()
                    if program == "y":
                        lanjut = False
                        n = False
                        program = True
                    elif program == "n":
                        print("menutup program")
                        program = False
                        lanjut = False
                        break
                    else: print("input tidak valid, coba lagi")
            else: print("pilihan tidak tersedia, coba lagi")