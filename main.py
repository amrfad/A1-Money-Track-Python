from konversi_mata_uang import *
from rekap_harian import *
import os
from menu import *
from fiturLaporan import *
from rekap_pekanan import *
from rekap_bulanan import *

# load user
user = User('init_name')

if __name__ == '__main__':
    while(True):
        os.system('cls')
        cetak_banner()
        user.read_from_file()
        user.nama = 'Pak Asep'
        print(f"{biru_tebal}SELAMAT DATANG DI APLIKASI MONEY TRACKING!{default}\n")
        print(f"Halo, {kuning}{user.nama}{default}. Saldo Totalmu Adalah: {biru_laut} {format_mata_uang(user.saldo.total)}{default}")
        cetak_menu_utama()
        pilihan = input("Masukkan pilihan anda: ")
        os.system('cls')

        if pilihan == '1':
            cetak_banner()
            user.catatTransaksi()
        elif pilihan == '2':
            cetak_banner()
            user.showInfo()
            pass
        elif pilihan == '3':
            cetak_banner()
            tampil_menu_rekap_harian(user)
        elif pilihan == '4':
            cetak_banner()
            tampil_menu_rekap_pekanan(user)
            pass
        elif pilihan == '5':
            cetak_banner()
            tampil_menu_rekap_bulanan(user)
            pass
        elif pilihan == '6':
            cetak_banner()
            user.loadFullData()
            input()
        elif pilihan == '7':
            cetak_banner()
            tampil_menu_konversi()
        elif pilihan == '8':
            cetak_banner()
            inputLaporan(user=user)
            input()
            pass
        elif pilihan == '0':
            exit()
        else:
            print("Pilihan tidak valid!")