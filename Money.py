import time
import InputProcess as ip

class Tanggal:
        def __init__(self, tahun, bulan, hari):
            self.hari = hari
            self.bulan = bulan
            self.tahun = tahun
            self.pekan = 1 if (1<=self.hari<=7) else (2 if (8<=self.hari<=14) else (3 if (15<=self.hari<=21) else 4))

        def showTanggal(self):
             return f"{self.hari}/{self.bulan}/{self.tahun}, Pekan ke-{self.pekan}"

def sumber_dana(sumber_dana):
    return ("Dompet Digital: " if (sumber_dana == 1) else "Rekening rekening_bank: ")

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
    def __init__(self, waktu, sumber_dana, nominal) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal

    def showMasuk(self):
        return "TRANSAKSI MASUK" + "\n***************\n" + sumber_dana(self.sumber_dana) + f"+Rp.{self.nominal}" + "\n***************"
    
class Keluar:
    def __init__(self, waktu, sumber_dana, nominal, kategori) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal
        self.kategori = kategori

    def showKeluar(self):
        return "TRANSAKSI KELUAR" + "\n****************\n" + sumber_dana(self.sumber_dana) + f"-Rp.{self.nominal}\n" + f"Kategori: {kategori(self.kategori)}" + "\n****************"

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

    def transaksiMasuk(self, transaksi_masuk):
        if (transaksi_masuk == None):
            transaksi_masuk = ip.inputMasuk()
        else:
            transaksi_masuk = transaksi_masuk
        self.saldo.saldoMasuk(transaksi_masuk=transaksi_masuk)
        self.transaksi_masuk.append(transaksi_masuk)
        transaksi_masuk.showMasuk()

    def transaksiKeluar(self, transaksi_keluar):
        if (transaksi_keluar == None):
            transaksi_keluar = ip.inputKeluar()
        else:
            transaksi_keluar = transaksi_keluar
        self.saldo.saldoKeluar(transaksi_keluar=transaksi_keluar)
        transaksi_keluar.showKeluar()

    def showRiwayatMasuk(self):
        print("RIWAYAT TRANSAKSI MASUK")
        print("***********************")
        for transaksi in self.transaksi_masuk:
            transaksi.showMasuk()
        print("***********************")

    def showRiwayatKeluar(self):
        print("RIWAYAT TRANSAKSI Keluar")
        print("************************")
        for transaksi in self.transaksi_keluar:
            transaksi.showKeluar()
        print("************************")
