from Money import *
class User:
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
    