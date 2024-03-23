import re, os
from konversi_mata_uang import *
from InputProcess import *
from Money import *

# Memeriksa apakah tanggal rekap dan tanggal transaksi sama
def is_same_day(tanggal_rekap: Tanggal, tanggal_transaksi: Tanggal):
    result = tanggal_rekap.hari == tanggal_transaksi.hari 
    result = result and tanggal_rekap.bulan == tanggal_transaksi.bulan
    result = result and tanggal_rekap.tahun == tanggal_transaksi.tahun
    return result

# Menampilkan Rekap Harian Transaksi Masuk
def rekap_harian_masuk(user: User, tanggal_rekap):
    print(f"{kuning}Rekap Harian Transaksi Masuk{default}")
    total_pemasukan = 0
    print((biru_tebal + "{0:10s}\t{1:20s}\t{2}" + default).format("Tanggal", "Nominal", "Sumber Dana"))
    for transaksi in user.transaksi_masuk:
        if is_same_day(tanggal_rekap, transaksi.waktu):
            total_pemasukan += transaksi.nominal
            print((default + "{0:10s}\t{1:20s}\t{2}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()), 
                                                             format_mata_uang(transaksi.nominal), transaksi.sumber_dana))
    print(f"{biru_tebal}Total Pemasukan: {hijau_tebal}{format_mata_uang(total_pemasukan)}{default}")

# Menampilkan Rekap Harian Transaksi Keluar
def rekap_harian_keluar(user: User, tanggal_rekap):
    print(f"{kuning}Rekap Harian Transaksi Keluar{default}")
    total_pengeluaran = 0
    print((biru_tebal + "{0:10s}\t{1:20s}\t{2:15s}\t{3}" + default).format("Tanggal", "Nominal", "Kategori", "Sumber Dana"))
    for transaksi in user.transaksi_keluar:
        if is_same_day(tanggal_rekap, transaksi.waktu):
            total_pengeluaran += transaksi.nominal
            print((default + "{0:10s}\t{1:20s}\t{2:15s}\t{3}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()),
                                                                      format_mata_uang(transaksi.nominal), transaksi.kategori,
                                                                      transaksi.sumber_dana))
    print(f"{biru_tebal}Total Pengeluaran: {merah_tebal}{format_mata_uang(total_pengeluaran)}{default}")

# Menampilkan Rekap Keseluruhan
def rekap_harian_total(user: User, tanggal_rekap):
    print(f"{kuning}Rekap Harian Transaksi Keseluruhan{default}")
    total = 0
    print((biru_tebal + "{0:10s}\t{1:20s}\t{2:15s}\t{3}" + default).format("Tanggal", "Nominal", "Kategori", "Sumber Dana"))
    for transaksi in user.transaksi_masuk:
        if is_same_day(tanggal_rekap, transaksi.waktu):
            total += transaksi.nominal
            print((default + "{0:10s}\t{1:20s}\t{2:15s}\t{3}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()), 
                                                             format_mata_uang(transaksi.nominal), '-', transaksi.sumber_dana))
    for transaksi in user.transaksi_keluar:
        if is_same_day(tanggal_rekap, transaksi.waktu):
            total -= transaksi.nominal
            print((default + "{0:10s}\t{1:20s}\t{2:15s}\t{3}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()),
                                                                      format_mata_uang(transaksi.nominal), transaksi.kategori,
                                                                      transaksi.sumber_dana))
    print(f"{biru_tebal}Total Keseluruhan: {hijau_tebal if total>0 else merah_tebal}{format_mata_uang(total)}{default}")

# Menampilkan Menu Rekap Harian
def tampil_menu_rekap_harian(user: User):
    pilihan_rekap = [rekap_harian_masuk, rekap_harian_keluar, rekap_harian_total]
    print(f"{kuning}Menu Rekap Harian{default}")
    print(f"{hijau_tebal}1.{default} Rekap Harian Transaksi Masuk")
    print(f"{hijau_tebal}2.{default} Rekap Harian Transaksi Keluar")
    print(f"{hijau_tebal}3.{default} Rekap Harian Transaksi Keseluruhan")
    print(f"{biru_tebal}Masukkan Pilihanmu: {default}", end='')
    pilihan = int(input())
    tanggal = inputTanggal()
    os.system('cls')
    pilihan_rekap[pilihan-1](user, tanggal)
    print(f"\n{biru_laut}[Klik di mana saja untuk kembali ke menu utama.]{default}")
    input()
    os.system('cls')