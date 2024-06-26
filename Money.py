import time
import InputProcess as ip
import os
import pickle
from text_color import *
from konversi_mata_uang import *

class Tanggal:
        def __init__(self, tahun, bulan, hari):
            self.hari = hari
            self.bulan = bulan
            self.tahun = tahun
            self.pekan = 1 if (1<=self.hari<=7) else (2 if (8<=self.hari<=14) else (3 if (15<=self.hari<=21) else 4))

        def showTanggal(self):
             return f"{self.hari}/{self.bulan}/{self.tahun}, Pekan ke-{self.pekan}"

def sumber_dana(sumber_dana):
    return ("Dompet Digital" if (sumber_dana == 1) else "Rekening rekening_bank")

def kategori(kategori):
    if (kategori == 1):
        return "Makanan"
    elif (kategori == 2):
        return "Transportasi"
    elif (kategori == 3):
        return "Hiburan"
    else:
        return "Lain-lain"

class Masuk:
    def __init__(self, waktu: Tanggal, sumber_dana, nominal) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal

    def showMasuk(self):
        return self.waktu.showTanggal() + "\n" + f"{sumber_dana(self.sumber_dana)} +{format_mata_uang(self.nominal)}"
    
    def showSuccess(self):
        os.system('cls')
        print("\033[0m----------------------------------------------")
        print(f"\t\t{hijau_tebal}Transaksi Berhasil{default}")
        print("\033[0m----------------------------------------------\n")
        print(f"Tanggal \t\t: \t{self.waktu.showTanggal()}")
        print(f"Nominal \t\t: \t{kuning}{format_mata_uang(self.nominal)}{default}")
        print(f"Sumber dana \t\t: \t{ungu}{sumber_dana(self.sumber_dana)}{default}")
        print(f"\n\t====== {biru_laut_tebal}Hemat Pangkal Kaya{default} ======\n")
        input("Tekan Enter untuk melanjutkan!")
    
class Keluar:
    def __init__(self, waktu:Tanggal, sumber_dana, nominal, kategori) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal
        self.kategori = kategori

    def showKeluar(self):
        return self.waktu.showTanggal() + "\n" + f"Kategori: {kategori(self.kategori)}" + "\n" + f"{sumber_dana(self.sumber_dana)} -{format_mata_uang(self.nominal)}"
    
    def showSuccessOut(self):
        print("\033[0m----------------------------------------------")
        print(f"\t\t{hijau_tebal}Transaksi Berhasil{default}")
        print("\033[0m----------------------------------------------\n")
        print(f"Tanggal \t\t: \t{self.waktu.showTanggal()}")
        print(f"Nominal \t\t: \t{kuning} {format_mata_uang(self.nominal)}{default}")
        print(f"Sumber dana \t\t: \t{ungu}{sumber_dana(self.sumber_dana)}{default}")
        print(f"Kategori \t\t: \t{biru}{kategori(self.kategori)}{default}")
        print(f"\n\t====== {biru_laut_tebal}Hemat Pangkal Kaya{default} ======\n")
        input("Tekan Enter untuk melanjutkan!")
    
class SaldoUser:
    def __init__(self, dompet_digital=0, rekening_bank=0) -> None:
        self.dompet_digital = dompet_digital
        self.rekening_bank = rekening_bank
        self.total = self.dompet_digital + self.rekening_bank

    def cekSaldo(self, sumber_dana:int):
        return self.dompet_digital if (sumber_dana == 1) else self.rekening_bank
    
    def saldoMasuk(self, transaksi_masuk:Masuk):
        if (transaksi_masuk.sumber_dana == 1):
            self.dompet_digital += transaksi_masuk.nominal
        else: 
            self.rekening_bank += transaksi_masuk.nominal
        self.total = self.dompet_digital + self.rekening_bank

    def saldoKeluar(self, transaksi_keluar:Keluar):
        if (transaksi_keluar.sumber_dana == 1):
            if (self.dompet_digital >= transaksi_keluar.nominal):
                self.dompet_digital -= transaksi_keluar.nominal
                self.total = self.dompet_digital + self.rekening_bank
                transaksi_keluar.showSuccessOut
            else: 
                print("Saldo Tidak Mencukupi")
                time.sleep(3)
        else:
            if (self.rekening_bank >= transaksi_keluar.nominal):
                self.rekening_bank -= transaksi_keluar.nominal
                self.total = self.dompet_digital + self.rekening_bank
            else: 
                print("Saldo Tidak Mencukupi")
                time.sleep(3)
    
    def showSaldoUser(self):
        return "SALDO USER\n" + "**********\n" + f"Dompet Digital: {format_mata_uang(self.dompet_digital)}\n" + f"Rekening Bank: {format_mata_uang(self.rekening_bank)}\n" + "**********\n" + f"Total: {format_mata_uang(self.total)}"

class User:
    def __init__(self, nama:str) -> None:
        self.nama = nama
        self.saldo = SaldoUser()
        self.transaksi_masuk = []
        self.transaksi_keluar = []

    def showInfo(self):
        print(f"{self.nama}")
        print("**********")
        print(self.saldo.showSaldoUser())
        print(f"{biru_tebal} ===== CLICK ENTER =====")
        input()

    def transaksiMasuk(self):
        transaksi_masuk = ip.inputMasuk()
        self.saldo.saldoMasuk(transaksi_masuk=transaksi_masuk)
        self.transaksi_masuk.append(transaksi_masuk)
        transaksi_masuk.showSuccess()
        transaksi_masuk.showMasuk()
        self.save_to_file()
        
    def transaksiKeluar(self):
        transaksi_keluar = ip.inputKeluar()
        self.saldo.saldoKeluar(transaksi_keluar=transaksi_keluar)
        self.transaksi_keluar.append(transaksi_keluar)
        transaksi_keluar.showKeluar()
        self.save_to_file()
           
    def save_to_file(self):
        with open("User.DAT", "wb") as file:
            pickle.dump(self, file)
            
    def read_from_file(self):
        with open("User.DAT", "rb") as file:
            tampung = pickle.load(file)
            self.nama = tampung.nama
            self.saldo = tampung.saldo
            self.transaksi_keluar = tampung.transaksi_keluar
            self.transaksi_masuk = tampung.transaksi_masuk
        
    def catatTransaksi(self):
        print("-------------------------------")
        print("\033[32mAyo Catat Keuangan Anda \033[34mdisini\033[0m")
        print("-------------------------------")
        print(f"{biru_laut_tebal}[{default}1{biru_laut_tebal}]{default} Pemasukan")
        print(f"{biru_laut_tebal}[{default}2{biru_laut_tebal}]{default} Pengeluaran")
        pilihan = int(input("Masukkan pilihan anda: "))

        if pilihan == 1:
            try :
                self.read_from_file()
            except FileNotFoundError:
                pass
            self.transaksiMasuk()
            
        elif pilihan == 2:
            try :
                self.read_from_file()
            except FileNotFoundError:
                pass
            self.transaksiKeluar()
    def showRiwayatMasuk(self):
        for transaksi in self.transaksi_masuk:
            print(f"{transaksi.showMasuk()}\n")
        print("***********************\n")
        

    def showRiwayatKeluar(self):
        for transaksi in self.transaksi_keluar:
            print(f"{transaksi.showKeluar()}\n")
        print("************************")
        
    def loadFullData(self):
        self.read_from_file()
        print(f"\n========= {hijau_tebal}DETAIL TRANSAKSI{default} =========\n")
        print(f"Jumlah saldo keseluruhan: {kuning}{format_mata_uang(self.saldo.total)}{default}\n")
        print(f"Jumlah Transaksi Masuk: {len(self.transaksi_masuk)}\n")
        print(f"Jumlah Transaksi Keluar: {len(self.transaksi_keluar)}\n")
        
        if(len(self.transaksi_masuk) > 0):
            print(f"===== {biru_laut_tebal}Transaksi Masuk{default} =====\n")
            self.showRiwayatMasuk()
        if(len(self.transaksi_keluar) > 0):    
            print(f"===== {biru_laut_tebal}Transaksi Keluar{default} =====\n")
            self.showRiwayatKeluar()
        