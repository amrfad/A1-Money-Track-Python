from InputProcess import *
from Money import *
# from Money1 import *

# transaksi = Transaksi("20 Juli 2005", "bank", 20000.0, None)
# print(transaksi.tanggal)

# catat = User("Reqiii")20 
# catat.catat_keuangan()


user = User("Agus")
user.catatTransaksi()

# user.save_to_file()
# user.showRiwayatMasuk()
# user.showRiwayatKeluar()

print(user.transaksi_masuk[0].nominal)

# print(user.transaksi_keluar[0].nominal)
# print(user.saldo.total)
