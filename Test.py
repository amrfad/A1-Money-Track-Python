from InputProcess import *
from Money import *

# transaksi = Transaksi("20 Juli 2005", "bank", 20000.0, None)
# print(transaksi.tanggal)

# catat = User("Reqiii")20 
# catat.catat_keuangan()


user = User("Agus")
# user.catatTransaksi()

# user.save_to_file()
# user.showRiwayatMasuk()
# user.showRiwayatKeluar()

user.read_from_file()
# with open("User.DAT", "rb") as file:
#     user = pickle.load(file)
print(user.transaksi_masuk[3].nominal)
