# from InputProcess import *
from Money import *
from konversi_mata_uang import format_mata_uang

def hitungRataRata(list):
    total = 0
    for data in list:
        total += data.nominal
    return format_mata_uang(total//len(list))

def translateBulan(bulan):
    nama_bulan = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember",
    }
    return nama_bulan[bulan]

def laporanTahunan(current_user, kategori, tahun):
    bulan = {
        1: []   ,
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
    }
    if (kategori.lower() == "keluar"):
        for transaksi in current_user.transaksi_keluar:
            if (transaksi.waktu.tahun == tahun):
                bulan[transaksi.waktu.bulan].append(transaksi)
    else:
        for transaksi in current_user.transaksi_masuk:
            if (transaksi.waktu.tahun == tahun):
                bulan[transaksi.waktu.bulan].append(transaksi)
        

    for i in range(1, 13):
        if (len(bulan[i]) != 0):
            print(f"Bulan {translateBulan(i)} Tahun {tahun}")
            print(f"     Rata-rata {"pengeluaran" if (kategori.lower()=="keluar") else "pemasukan"}: {hitungRataRata(bulan[i])}")
        else:
            print(f"Bulan {translateBulan(i)} Tahun {tahun}")
            print("     Belum ada pengeluaran.")

def inputLaporan(user):
    print("FITUR LAPORAN")
    print("Pilih Kategori: 1. Pemasukan/ 2. Pengeluaran")
    kategori = int(input(">> "))
    while (not (1<=kategori<=2)):
        os.system('cls')
        print("FITUR LAPORAN")
        print("Pilih Kategori: 1. Pemasukan/ 2. Pengeluaran")
        print("ENTER A VALID INPUT")
        kategori = int(input(">> "))

    print("Masukkan Tahun: ")
    tahun = int(input(">> "))
    laporanTahunan(user, "keluar" if (kategori==2) else "masuk", tahun)