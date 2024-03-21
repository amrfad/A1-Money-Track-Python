import time
import InputProcess as ip
import os
import pickle

class Tanggal:
        def __init__(self, tahun, bulan, hari):
            self.hari = hari
            self.bulan = bulan
            self.tahun = tahun
            self.pekan = 1 if (1<=self.hari<=7) else (2 if (8<=self.hari<=14) else (3 if (15<=self.hari<=21) else 4))

        def showTanggal(self):
             return f"{self.hari}/{self.bulan}/{self.tahun}, Pekan ke-{self.pekan}"

def sumber_dana(sumber_dana):
    return ("Dompet Digital:" if (sumber_dana == 1) else "Rekening rekening_bank:")

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
        return self.waktu.showTanggal() + "\n" + f"{sumber_dana(self.sumber_dana)} +Rp.{self.nominal}"
    
    def showSuccess(self):
        os.system('cls')
        print("\033[0m----------------------------------------------")
        print("\t\tTransaksi Berhasil")
        print("\033[0m----------------------------------------------\n")
        print(f"Tanggal \t\t: \t{self.waktu.showTanggal()}")
        print(f"Nominal \t\t: \tRp. {self.nominal}")
        print(f"Sumber dana \t\t: \t{sumber_dana(self.sumber_dana)}")
        print("\n\t====== Hemat Pangkal Kaya ======\n")
        input("Tekan Enter untuk melanjutkan!")
    
class Keluar:
    def __init__(self, waktu:Tanggal, sumber_dana, nominal, kategori) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal
        self.kategori = kategori

    def showKeluar(self):
        return self.waktu.showTanggal() + "\n" + f"Kategori: {kategori(self.kategori)}" + "\n" + f"{sumber_dana(self.sumber_dana)} -Rp.{self.nominal}"
    
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
        return "SALDO USER\n" + "**********\n" + f"Dompet Digital: Rp.{self.dompet_digital}\n" + f"Rekening Bank: Rp.{self.rekening_bank}\n" + "**********\n" + f"Total: Rp.{self.total}"

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

    def transaksiMasuk(self):
        transaksi_masuk = ip.inputMasuk()
        self.saldo.saldoMasuk(transaksi_masuk=transaksi_masuk)
        
        self.transaksi_masuk.append(transaksi_masuk)
        transaksi_masuk.showSuccess()
        transaksi_masuk.showMasuk()
    
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
        

            
    # def save_to_file_masuk(self):
    #     with open("UserMasuk.txt", "w") as file:
    #         for i, transaksi in enumerate(self.transaksi_masuk):
    #             if transaksi is not None:
    #                 file.write(f"{transaksi},{'Dompet Digital' if transaksi.sumber_dana == 1 else 'Bank'},{transaksi.nominal:.2f}\n")
    
    def transaksiKeluar(self):
        transaksi_keluar = ip.inputKeluar()
        self.saldo.saldoKeluar(transaksi_keluar=transaksi_keluar)
        transaksi_keluar.showKeluar()
        
    # def save_to_file_keluar(self):
    #     with open("UserKeluar.DAT", "w") as file:
    #         file.write(f"Nama: {self.nama}\n")
    #         file.write(f"Saldo Dompet Digital: {self.saldo.dompet_digital:.2f}\n")
    #         file.write(f"Saldo Bank: {self.saldo.bank:.2f}\n")
    #         file.write(f"Saldo Total: {self.saldo.total:.2f}\n")
    #         file.write("Transaksi Keluar:\n")
    #         for i, transaksi in enumerate(self.transaksi_keluar):
    #             if transaksi is not None:
    #                 file.write(f"{i + 1}. {transaksi.waktu} | Sumber Dana: {'Dompet Digital' if transaksi.sumber_dana == 1 else 'Bank'} | Nominal: {transaksi.nominal:.2f} | Kategori: {kategori}\n")
    
    def catatTransaksi(self):
        self.read_from_file()
        print("-------------------------------")
        print("\033[32mAyo Catat Keuangan Anda \033[34mdisini\033[0m")
        print("-------------------------------")
        print("(1) Pemasukan")
        print("(2) Pengeluaran")
        pilihan = int(input("Masukkan pilihan anda: "))

        if pilihan == 1:
            self.transaksiMasuk()
            self.save_to_file()
        elif pilihan == 2:
            self.transaksiKeluar()
            # self.save_to_file()

    def showRiwayatMasuk(self):
        print("RIWAYAT TRANSAKSI MASUK")
        print("***********************")
        for transaksi in self.transaksi_masuk:
            print(transaksi.showMasuk())
        print("***********************")

    def showRiwayatKeluar(self):
        print("RIWAYAT TRANSAKSI Keluar")
        print("************************")
        for transaksi in self.transaksi_keluar:
            print(transaksi.showKeluar())
        print("************************")
        
