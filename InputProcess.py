import datetime
import os
from Money import * 
from text_color import *
from menu import *

# Input Tanggal S T A R T
def isValidTanggal(tahun, bulan, tanggal):
    """
    Fungsi untuk memeriksa validitas tanggal yang diinput

    Parameter:
    tahun: Tahun transaksi
    bulan: Bulan transaksi
    tanggal: tanggal transaksi

    Return:
    boolean - True jika valid, False jika invalid
    """
    try:
        cur_date = datetime.datetime(tahun, bulan, tanggal)
        return True
    except ValueError:
        return False

def inputTanggal():
    """
    Fungsi untuk menginput tanggal transaksi

    Parameter:
    None

    Return:
    Tanggal - Instance dari objek Tanggal
    """

    hari = 0
    bulan = 0
    tahun = 0

    while(not isValidTanggal(tahun=tahun, bulan=bulan, tanggal=hari)):
        os.system('cls')
        cetak_banner()
        print(f"Masukkan Tanggal Transaksi: \n[{biru_laut}dd{default} {hijau}m{default} {kuning}yyyy{default}]")
        user_input = input(f"\n{hijau}>>{default} ").split()
        hari = int(user_input[0])
        bulan = int(user_input[1])
        tahun = int(user_input[2])

    tanggal = Tanggal(tahun, bulan, hari)
    return tanggal
# Input Tanggal E N D

# Input Masuk S T A R T
def inputMasuk():
    waktu_transaksi = inputTanggal()
    sumber_dana = 0
    os.system('cls')
    cetak_banner()
    print("Sumber Dana\n")
    print(f"{biru_laut_tebal}[{default}1{biru_laut_tebal}]{default} Dompet Digital")
    print(f"{biru_laut_tebal}[{default}2{biru_laut_tebal}]{default} Rekening Bank")
    while (sumber_dana != 1 and sumber_dana != 2):
        print("\nMasukkan Input: ", end="")
        sumber_dana = int(input())
    nominal = -999
    
    while (nominal < 0):
        print(f"\nMasukkan Nominal: {kuning}Rp. {default}", end="")
        nominal = int(input())
    return Masuk(waktu=waktu_transaksi, sumber_dana=sumber_dana, nominal=nominal)
# Input Masuk E N D

# Input Keluar S T A R T
def inputKeluar():
    waktu_transaksi = inputTanggal()
    os.system('cls')
    cetak_banner()
    print("Sumber Dana")
    print(f"{biru_laut_tebal}[{default}1{biru_laut_tebal}]{default} Dompet Digital")
    print(f"{biru_laut_tebal}[{default}2{biru_laut_tebal}]{default} Rekening Bank")
    sumber_dana = 0
    while (sumber_dana != 1 and sumber_dana != 2):
        print("\nMasukkan Input: ", end="")
        sumber_dana = int(input())
    nominal = -999
    while (nominal < 0):
        print(f"\nMasukkan Nominal: {kuning}Rp.{default} ", end="")
        nominal = int(input())
    print("Kategori Pengeluaran")
    print(f"{biru_laut_tebal}[{default}1{biru_laut_tebal}]{default} Makanan")
    print(f"{biru_laut_tebal}[{default}2{biru_laut_tebal}]{default} Transportasi")
    print(f"{biru_laut_tebal}[{default}3{biru_laut_tebal}]{default} Hiburan")
    print(f"{biru_laut_tebal}[{default}4{biru_laut_tebal}]{default} Tagihan")
    print(f"{biru_laut_tebal}[{default}5{biru_laut_tebal}]{default} Lain-lain")
    kategori = -1
    while (kategori < 0 or kategori > 5):
        print("\nMasukkan Input: ", end="")
        kategori = int(input())

    return Keluar(waktu=waktu_transaksi, sumber_dana=sumber_dana, nominal=nominal, kategori=kategori)
# Input Keluar E N D