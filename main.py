from konversi_mata_uang import *
from rekap_harian import *
import os
from menu import *

# load user
user = User('init_name')


if __name__ == '__main__':
    while(True):
        cetak_banner()
        cetak_menu_utama(user)
        pilihan = input("Masukkan pilihan anda: ")
        os.system('cls')

        if pilihan == '1':
            cetak_banner()
            pass
        elif pilihan == '2':
            cetak_banner()
            pass
        elif pilihan == '3':
            cetak_banner()
            tampil_menu_rekap_harian(user)
        elif pilihan == '4':
            cetak_banner()
            pass
        elif pilihan == '5':
            cetak_banner()
            pass
        elif pilihan == '6':
            cetak_banner()
            pass
        elif pilihan == '7':
            cetak_banner()
            tampil_menu_konversi()
        elif pilihan == '8':
            cetak_banner()
            pass
        elif pilihan == '0':
            exit()
        else:
            print("Pilihan tidak valid!")