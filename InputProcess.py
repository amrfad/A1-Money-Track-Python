import datetime
from Money import Tanggal

# Input Tanggal S T A R T
def isValidTanggal(tahun, bulan, tanggal):
    """
    Fungsi untuk memeriksa validitas tanggal yang diinput

    Parameter:
    tahun: Tahun transaksi
    bulan: Bulan transaksi
    tanggal: tanggal transaksi

    Return:
    boolean - True jika valid, False jika invalid
    """
    try:
        cur_date = datetime.datetime(tahun, bulan, tanggal)
        return True
    except ValueError:
        return False

def inputTanggal():
    """
    Fungsi untuk menginput tanggal transaksi

    Parameter:
    None

    Return:
    Tanggal - Instance dari objek Tanggal
    """

    while(True):
        print("Masukkan Tanggal Transaksi: ")
        print("Hari: ", end="")
        hari = int(input())
        print("Bulan: ", end="")
        bulan = int(input())
        print("Tahun: ", end="")
        tahun = int(input())

        if (isValidTanggal(tahun, bulan, hari)):
            break;

    return Tanggal(tahun, bulan, hari)
# Input Tanggal E N D