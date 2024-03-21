class Tanggal:
        def __init__(self, tahun, bulan, hari):
            self.hari = hari
            self.bulan = bulan
            self.tahun = tahun
            self.pekan = 1 if (1<=self.hari<=7) else (2 if (8<=self.hari<=14) else (3 if (15<=self.hari<=21) else 4))

        def showTanggal(self):
             return f"{self.hari}/{self.bulan}/{self.tahun}, Pekan ke-{self.pekan}"

def sumber_dana(sumber_dana):
    return ("Dompet Digital: " if (sumber_dana == 1) else "Rekening Bank: ")

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
    
class User:
    def __init__(self, nama) -> None:
        self.nama = nama
        self.transaksi_masuk = []
        self.indeksMasuk = 0
        self.transaksi_keluar = []
        self.indeksKeluar = 0