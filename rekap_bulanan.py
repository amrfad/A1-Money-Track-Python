from msvcrt import getch
import re
from konversi_mata_uang import *
from InputProcess import *
from Money import Tanggal
from konversi_mata_uang import *

def rekapBulananMasuk(user):
    tanggalRekap = Tanggal(0, 0, 0)
    print(f"{hijau_tebal}Masukkan tahun yang ingin ditampilkan data rekapnya. (Contoh: 2023){default}")
    tanggalRekap.tahun = int(input(">> "))
    print(f"{hijau_tebal}Masukkan bulan yang ingin ditampilkan data rekapnya. (Silakan masukkan angkanya saja){biru_laut}")
    print("1. Januari")
    print("2. Februari")
    print("3. Maret")
    print("4. April")
    print("5. Mei")
    print("6. Juni")
    print("7. Juli")
    print("8. Agustus")
    print("9. September")
    print("10. Oktober")
    print("11. November")
    print(f"12. Desember{default}")
    tanggalRekap.bulan = int(input(">> "))
    while tanggalRekap.bulan < 1 or tanggalRekap.bulan > 12:
        print(f"{merah}Tolong masukkan angka yang valid{default}")
        tanggalRekap.bulan = int(input(">> "))
    
    ada_pemasukan = False
    total_pemasukan = 0
    print((biru_tebal + "{0:10s}\t{1:20s}\t{2}" + default).format("Tanggal", "Nominal", "Sumber Dana"))
    for transaksi in user.transaksi_masuk:
        if isSameMonth(tanggalRekap, transaksi.waktu):
            print((default + "{0:10s}\t{1:20s}\t{2}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()), 
                                                             format_mata_uang(transaksi.nominal), transaksi.sumber_dana))
            total_pemasukan += transaksi.nominal
            ada_pemasukan=True
    if ada_pemasukan==True:
        print(f"{biru_tebal}Total pemasukan pada bulan ", end="")
        if tanggalRekap.bulan == 1:
            print("Januari: ", end="")
        elif tanggalRekap.bulan == 2:
            print("Februari: ", end="")
        elif tanggalRekap.bulan == 3:
            print("Maret: ", end="")
        elif tanggalRekap.bulan == 4:
            print("April: ", end="")
        elif tanggalRekap.bulan == 5:
            print("Mei: ",end="")
        elif tanggalRekap.bulan == 6:
            print("Juni: ", end="")
        elif tanggalRekap.bulan == 7:
            print("Juli: ", end="")
        elif tanggalRekap.bulan == 8:
            print("Agustus: ", end="")
        elif tanggalRekap.bulan == 9:
            print("September: ", end="")
        elif tanggalRekap.bulan == 10:
            print("Oktober: ", end="")
        elif tanggalRekap.bulan == 11:
            print("November: ", end="")
        elif tanggalRekap.bulan == 12:
            print("Desember: ", end="")
        print(f"{hijau_tebal}{format_mata_uang(total_pemasukan)}{default}")
    else:
        print(f"{kuning_tebal}Data Kosong{default}")
    print("Tekan apapun untuk kembali ke menu awal.")
    getch()


def rekapBulananKeluar(user):
    tanggalRekap = Tanggal(0, 0, 0)
    
    print(f"{hijau_tebal}Masukkan tahun yang ingin ditampilkan data rekapnya. (Contoh: 2023){default}")
    tanggalRekap.tahun = int(input(">> "))
    print(f"{hijau_tebal}Masukkan bulan yang ingin ditampilkan data rekapnya. (Silakan masukkan angkanya saja){biru_laut}")
    print("1. Januari")
    print("2. Februari")
    print("3. Maret")
    print("4. April")
    print("5. Mei")
    print("6. Juni")
    print("7. Juli")
    print("8. Agustus")
    print("9. September")
    print("10. Oktober")
    print("11. November")
    print(f"12. Desember{default}")
    tanggalRekap.bulan = int(input(">> "))
    while tanggalRekap.bulan < 1 or tanggalRekap.bulan > 12:
        print(f"{merah}Tolong masukkan angka yang valid{default}")
        tanggalRekap.bulan = int(input(">> "))

    kategori = {"Makanan", "Transportasi", "Hiburan", "Tagihan", "Lain-lain"}
    total_pengeluaran = 0
    ada_pengeluaran=False
    
    print((biru_tebal + "{0:10s}\t{1:20s}\t{2:15s}\t{3}" + default).format("Tanggal", "Nominal", "Kategori", "Sumber Dana"))
    for transaksi in user.transaksi_keluar:
        if isSameMonth(tanggalRekap, transaksi.waktu):
            print((default + "{0:10s}\t{1:20s}\t{2:15s}\t{3}").format(re.sub(r', Pekan ke-\d+', '', transaksi.waktu.showTanggal()),
                                                                      format_mata_uang(transaksi.nominal), transaksi.kategori,
                                                                      transaksi.sumber_dana))
            total_pengeluaran += transaksi.nominal
            ada_pengeluaran = True
    if ada_pengeluaran==True:
        print(f"{biru_tebal}Total pengeluaran pada bulan ", end="")
        
        if tanggalRekap.bulan == 1:
            print("Januari: ", end="")
        elif tanggalRekap.bulan == 2:
            print("Februari: ", end="")
        elif tanggalRekap.bulan == 3:
            print("Maret: ", end="")
        elif tanggalRekap.bulan == 4:
            print("April: ", end="")
        elif tanggalRekap.bulan == 5:
            print("Mei: ",end="")
        elif tanggalRekap.bulan == 6:
            print("Juni: ", end="")
        elif tanggalRekap.bulan == 7:
            print("Juli: ", end="")
        elif tanggalRekap.bulan == 8:
            print("Agustus: ", end="")
        elif tanggalRekap.bulan == 9:
            print("September: ", end="")
        elif tanggalRekap.bulan == 10:
            print("Oktober: ", end="")
        elif tanggalRekap.bulan == 11:
            print("November: ", end="")
        elif tanggalRekap.bulan == 12:
            print("Desember: ", end="")
        print(f"{hijau_tebal}{format_mata_uang(total_pengeluaran)}{default}")
    else:
        print(f"{kuning_tebal}Data Kosong{default}")
    print("Tekan apapun untuk kembali ke menu awal.")
    getch()

def tampil_menu_rekap_bulanan(user):
    print(f"{kuning}Menu Rekap Harian{default}")
    print(f"{hijau_tebal}1.{default} Rekap Bulanan Transaksi Masuk")
    print(f"{hijau_tebal}2.{default} Rekap Bulanan Transaksi Keluar")
    choice = int(input(f"{biru_tebal}Pilih: {default}"))
    if choice == 1:
        rekapBulananMasuk(user)
    else:
        rekapBulananKeluar(user)

def isSameMonth(tanggal1, tanggal2) -> bool:
    equal=False
    equal = (tanggal1.bulan == tanggal2.bulan)
    equal = equal and (tanggal1.tahun == tanggal2.tahun)
    return equal