from Money import Tanggal

def rekapPekananMasuk(user):
    tanggalRekap = Tanggal(0, 0, 0)

    print("Masukkan tahun yang ingin ditampilkan data rekapnya. (Contoh: 2023)")
    tanggalRekap.tahun = int(input(">> "))
    print("Masukkan bulan yang ingin ditampilkan data rekapnya. (Silakan masukkan angkanya saja)")
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
    print("12. Desember")
    tanggalRekap.bulan = int(input(">> "))

    while tanggalRekap.bulan < 1 or tanggalRekap.bulan > 12:
        print("Tolong masukkan angka yang valid")
        tanggalRekap.bulan = int(input(">> "))
    
    print("Masukkan pekan yang ingin direkap dari bulan tersebut (1-4)")
    tanggalRekap.pekan = int(input(">> "))
    while (tanggalRekap.pekan != 1 and tanggalRekap.pekan != 2 and tanggalRekap.pekan != 3 and tanggalRekap.pekan != 4):
        print("Tolong masukkan angka yang valid")
        tanggalRekap.pekan = int(input(">> "))
    
    tanggalRekap.tahun=user.transaksi_masu.waktu.tahun

    totalPemasukan = 0
    ada_pemasukan=False
    print("\033[134m%-10s\t%-10s\t%s\033[0m", "Tanggal", "Nominal", "Sumber Dana")
    for i in range(user.indek_masuk):
        if (isSameWeek(tanggalRekap, user.transaksi_masuk[i].waktu)):
            print("%02d/%02d/%d\t", user.transaksi_masuk[i].waktu.tanggal, user.transaksi_masuk[i].waktu.bulan, user.transaksi_masuk[i].waktu.tahun)
            formatMataUang(user.transaksi_masuk[i].nominal)
            print("\t%s", "Dompet Digital" if user.transaksi_masuk[i].sumber_dana == 1 else "Bank")
            totalPemasukan += user.transaksi_masuk[i].nominal
            ada_pemasukan=True
    
    if (ada_pemasukan==True):
        print("\033[134mTotal Pemasukan pada Pekan ke-%d, Bulan ", tanggalRekap.pekan)
        if tanggalRekap.bulan == 1:
            print("Januari: \033[132m", end="")
        elif tanggalRekap.bulan == 2:
            print("Februari: \033[132m", end="")
        elif tanggalRekap.bulan == 3:
            print("Maret: \033[132m", end="")
        elif tanggalRekap.bulan == 4:
            print("April: \033[132m", end="")
        elif tanggalRekap.bulan == 5:
            print("Mei: \033[132m",end="")
        elif tanggalRekap.bulan == 6:
            print("Juni: \033[132m", end="")
        elif tanggalRekap.bulan == 7:
            print("Juli: \033[132m", end="")
        elif tanggalRekap.bulan == 8:
            print("Agustus: \033[132m", end="")
        elif tanggalRekap.bulan == 9:
            print("September: \033[132m", end="")
        elif tanggalRekap.bulan == 10:
            print("Oktober: \033[132m", end="")
        elif tanggalRekap.bulan == 11:
            print("November: \033[132m", end="")
        elif tanggalRekap.bulan == 12:
            print("Desember: \033[132m", end="")
        formatMataUang(totalPemasukan)
        print("\033[0m")
    else:
        print("\033[132mData Kosong\033[0m")

def rekapPekananKeluar(user):
    tanggalRekap = Tanggal(0, 0, 0)

    print("Masukkan tahun yang ingin ditampilkan data rekapnya. (Contoh: 2023)")
    tanggalRekap.tahun = int(input(">> "))
    print("Masukkan bulan yang ingin ditampilkan data rekapnya. (Silakan masukkan angkanya saja)")
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
    print("12. Desember")
    tanggalRekap.bulan = int(input(">> "))
    
    while (tanggalRekap.bulan < 1 or tanggalRekap.bulan > 12):
        print("Tolong masukkan angka yang valid")
        tanggalRekap.bulan = int(input(">> "))
    
    print("Masukkan pekan yang ingin direkap dari bulan tersebut (1-4)>> ")
    tanggalRekap.pekan = int(input(">> "))

    while (tanggalRekap.pekan != 1 and tanggalRekap.pekan != 2 and tanggalRekap.pekan != 3 and tanggalRekap.pekan != 4):
        print("Tolong masukkan angka yang valid>> ")
        tanggalRekap.pekan = int(input(">> "))
    tanggalRekap.tahun=user.transaksi_keluar.waktu.tahun

    kategori = {"Makanan", "Transportasi", "Hiburan", "Tagihan", "Lain-lain"}
    totalPengeluaran = 0
    ada_pengeluaran=False
    print("\033[134m%-10s\t%-10s\t%s\t%s\033[0m", "Tanggal", "Nominal", "Sumber Dana", "Kategori")
    for i in range(user.indeksKeluar):
        if (isSameWeek(tanggalRekap, user.transaksi_keluar[i].waktu)):
            print("%02d/%02d/%d\t", tanggalRekap.tanggal, tanggalRekap.bulan, tanggalRekap.tahun)
            formatMataUang(user.transaksi_keluar[i].nominal)
            print("\t%s\t%s", "Dompet Digital" if user.transaksi_keluar[i].sumber_dana == 1  else "Bank", kategori[user.transaksi_keluar[i].kategori])
            totalPengeluaran += user.transaksi_keluar[i].nominal
            ada_pengeluaran=True
    
    if ada_pengeluaran==True:
        print("\033[134mTotal Pengeluaran pada pekan ke-%d, bulan ", tanggalRekap.pekan)
        if tanggalRekap.bulan == 1:
            print("Januari: \033[132m", end="")
        elif tanggalRekap.bulan == 2:
            print("Februari: \033[132m", end="")
        elif tanggalRekap.bulan == 3:
            print("Maret: \033[132m", end="")
        elif tanggalRekap.bulan == 4:
            print("April: \033[132m", end="")
        elif tanggalRekap.bulan == 5:
            print("Mei: \033[132m",end="")
        elif tanggalRekap.bulan == 6:
            print("Juni: \033[132m", end="")
        elif tanggalRekap.bulan == 7:
            print("Juli: \033[132m", end="")
        elif tanggalRekap.bulan == 8:
            print("Agustus: \033[132m", end="")
        elif tanggalRekap.bulan == 9:
            print("September: \033[132m", end="")
        elif tanggalRekap.bulan == 10:
            print("Oktober: \033[132m", end="")
        elif tanggalRekap.bulan == 11:
            print("November: \033[132m", end="")
        elif tanggalRekap.bulan == 12:
            print("Desember: \033[132m", end="")
        formatMataUang(totalPengeluaran)
        print("\033[0m")
    else:
        print("\033[132mData Kosong\033[0m")