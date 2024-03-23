from text_color import *
from InputProcess import *
from Money import *
from konversi_mata_uang import *
from rekap_harian import *

def cetak_menu_utama(user: User):
    print(f"{biru_tebal}SELAMAT DATANG DI APLIKASI MONEY TRACKING!{default}\n")
    print(f"Halo, {kuning}{user.nama}{default}. Saldo Totalmu Adalah: {biru_laut}Rp. {format_mata_uang(user.saldo.total)}{default}")
    print(f"{hijau}[1]{default} Catat Transaksi Baru")
    print(f"{hijau}[2]{default} Cek Saldo")
    print(f"{hijau}[3]{default} Tunjukkan Rekap Harian")
    print(f"{hijau}[4]{default} Tunjukkan Rekap per Pekan")
    print(f"{hijau}[5]{default} Tunjukkan Rekap Bulanan")
    print(f"{hijau}[6]{default} Muat Data dan Tampilkan Seluruh Riwayat Transaksi")
    print(f"{hijau}[7]{default} Kalkulator Konversi Mata Uang")
    print(f"{hijau}[8]{default} Laporan Keuangan")
    print(f"{hijau}[0]{default} Keluar")

def cetak_banner():
    print(" /$$      /$$                                               /$$$$$$$$                           /$$       /$$                    ")
    print("| $$$    /$$$                                              |__  $$__/                          | $$      |__/                    ")
    print("| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$         | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$ ")
    print("| $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$")
    print("| $$  $$$| $$| $$  \\ $$| $$  \\ $$| $$$$$$$$| $$  | $$         | $$| $$  \\__/ /$$$$$$$| $$      | $$$$$$/ | $$| $$  \\ $$| $$  \\ $$")
    print("| $$\\  $ | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$")
    print("| $$ \\/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \\  $$| $$| $$  | $$|  $$$$$$$")
    print("|__/     |__/ \\______/ |__/  |__/ \\_______/ \\____  $$         |__/|__/      \\_______/ \\_______/|__/  \\__/|__/|__/  |__/ \\____  $$")
    print("                                            /$$  | $$                                                                   /$$  \\ $$")
    print("                                           |  $$$$$$/                                                                  |  $$$$$$/")
    print("                                            \\______/                                                                    \\______/ ")