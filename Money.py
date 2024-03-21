class Tanggal:
        def __init__(self, tahun, bulan, hari):
            self.hari = hari
            self.bulan = bulan
            self.tahun = tahun
            self.pekan = 1 if (1<=self.hari<=7) else (2 if (8<=self.hari<=14) else (3 if (15<=self.hari<=21) else 4))

        def showTanggal(self):
             return f"{self.hari}/{self.bulan}/{self.tahun}, Pekan ke-{self.pekan}"
        
class Masuk:
    def __init__(self, waktu, sumber_dana, nominal) -> None:
        self.waktu = waktu
        self.sumber_dana = sumber_dana
        self.nominal = nominal

    def showMasuk(self):
        return f"TRANSAKSI MASUK" + "\n***************\n" + ("Dompet Digital: " if (self.sumber_dana == 1) else "Rekening Bank: ") + f"+Rp. {self.nominal}" + "\n***************"