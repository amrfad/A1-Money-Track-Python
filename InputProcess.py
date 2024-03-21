import datetime
import os
from Money import Tanggal
from Money import Masuk
from Money import Keluar
from Money import User

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
        print("Masukkan Tanggal Transaksi: ")
        user_input = input().split()
        hari = int(user_input[0])
        bulan = int(user_input[1])
        tahun = int(user_input[2])

    return Tanggal(tahun, bulan, hari)
# Input Tanggal E N D

# Input Masuk S T A R T
def inputMasuk():
    waktu_transaksi = inputTanggal()
    sumber_dana = 0
    print("Sumber Dana")
    print("1. Dompet Digital")
    print("2. Rekening Bank")
    while (sumber_dana != 1 and sumber_dana != 2):
        print("Masukkan Input: ", end="")
        sumber_dana = int(input())
    nominal = -999
    while (nominal < 0):
        print("Masukkan Nominal: ", end="")
        nominal = int(input())
    return Masuk(waktu=waktu_transaksi, sumber_dana=sumber_dana, nominal=nominal)
# Input Masuk E N D

# Input Keluar S T A R T
def inputKeluar():
    waktu_transaksi = inputTanggal()
    print("Sumber Dana")
    print("1. Dompet Digital")
    print("2. Rekening Bank")
    sumber_dana = 0
    while (sumber_dana != 1 and sumber_dana != 2):
        print("Masukkan Input: ", end="")
        sumber_dana = int(input())
    nominal = -999
    while (nominal < 0):
        print("Masukkan Nominal: ", end="")
        nominal = int(input())
    print("Kategori Pengeluaran")
    print("1. Makanan")
    print("2. Transportasi")
    print("3. Hiburan")
    print("4. Tagihan")
    print("5. Lain-lain")
    kategori = -1
    while (kategori < 0 or kategori > 5):
        print("Masukkan Input: ", end="")
        kategori = int(input())

    return Keluar(waktu=waktu_transaksi, sumber_dana=sumber_dana, nominal=nominal, kategori=kategori)
# Input Keluar E N D