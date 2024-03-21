from text_color import *

# Dictionary berisi mengenai informasi dari sebuah mata uang
MATA_UANG = {
    'AUD': {'Negara': 'Australia', 
            'Kurs': 10192.32},
    'BND': {'Negara': 'Brunei Darussalam', 
            'Kurs': 11660.99},
    'CAD': {'Negara': 'Kanada', 
            'Kurs': 11506.61},
    'CHF': {'Negara': 'Swiss', 
                'Kurs': 17687.27},
    'CNH': {'Negara': 'Tiongkok (Offshore)', 
            'Kurs': 2168.46},
    'CNY': {'Negara': 'Tiongkok (Onshore)', 
            'Kurs': 2173.01},
    'DKK': {'Negara': 'Denmark', 
            'Kurs': 2279.03},
    'EUR': {'Negara': 'Eurozone', 
            'Kurs':  16986.68},
    'GBP': {'Negara': 'Inggris', 
            'Kurs': 19884.02},
    'HKD': {'Negara': 'Hong Kong', 
            'Kurs': 1999.77},
    'JPY': {'Negara': 'Jepang', 
            'Kurs': 104.5748},
    'KRW': {'Negara': 'Korea Selatan', 
            'Kurs': 11.72},
    'KWD': {'Negara': 'Kuwait', 
            'Kurs': 50833.08},
    'LAK': {'Negara': 'Laos', 
            'Kurs': 0.75},
    'MYR': {'Negara': 'Malaysia', 
            'Kurs': 3306.78},
    'NOK': {'Negara': 'Norwegia', 
            'Kurs': 1479.79},
    'NZD': {'Negara': 'Selandia Baru', 
            'Kurs': 9530.56},
    'PGK': {'Negara': 'Papua Nugini', 
            'Kurs': 4042.51},
    'PHP': {'Negara': 'Filipina', 
            'Kurs': 279.96},
    'SAR': {'Negara': 'Arab Saudi', 
            'Kurs': 4171.17},
    'SEK': {'Negara': 'Swedia', 
            'Kurs': 1506.73},
    'SGD': {'Negara': 'Singapura', 
            'Kurs': 11660.99},
    'THB': {'Negara': 'Thailand', 
            'Kurs': 437.85},
    'USD': {'Negara': 'Amerika Serikat', 
            'Kurs': 15644.39},
    'VND': {'Negara': 'Vietnam', 
            'Kurs': 0.63}
    }


# Class untuk Mata Uang
class MataUang:
    """
    
    """
    def __init__(self, nama):
        self.nama = nama
        self.negara = MATA_UANG[nama]['Negara']
        self.kurs = MATA_UANG[nama]['Kurs']

    def konversi_ke_rupiah(self, nominal):
        return nominal * self.kurs
    
    def konversi_dari_rupiah(self, nominal):
        return nominal / self.kurs

    
# Melakukan formatting untuk mata uang
def format_mata_uang(nominal)->str:
    nominal = float(nominal)
    digits = list(str(round(nominal, 2)))
    decimals = digits[digits.index('.'):]
    digits = digits[:digits.index('.')-len(digits)]
    digits = digits[::-1]
    length = len(digits)
    formatted = []
    for i in range(len(digits)):
        formatted.append(digits.pop())
        if (length-i-1) % 3 == 0 and (length-i-1) != 0:
            formatted.append('.')
    
    if len(decimals) < 3:
        decimals += ['0']
    decimals[decimals.index('.')] = ','
    formatted = ['Rp '] + formatted + decimals

    return ''.join(formatted)

# Mencetak hasil konversi mata uang
def cetak_hasil_konversi(mata_uang: MataUang, nominal, ke_rupiah: bool):
    print(f"{kuning}Hasil Konversi: {hijau_tebal}", end='')
    if ke_rupiah:
        print(f"{format_mata_uang(nominal)} {mata_uang.nama} = ", end='')
        print(f"{format_mata_uang(mata_uang.konversi_ke_rupiah(nominal))} IDR")
    else:
        print(f"{format_mata_uang(nominal)} IDR = ", end='')
        print(f"{format_mata_uang(mata_uang.konversi_dari_rupiah(nominal))} {mata_uang.nama}")
    set_color(default)

# Menampilkan menu konversi mata uang
def tampil_menu_konversi():
    print(kuning + "Menu Konversi Mata Uang" + default)
    print(biru_tebal + '{0:5s}\t{1:20s}\t{2}'.format('[ $ ]', 'Nama Negara', 'Kurs Mata Uang') + default) 
    for i, mata_uang in enumerate(MATA_UANG):
        print(f"{hijau_tebal}[{mata_uang:3s}]{default}\t{MATA_UANG[mata_uang]['Negara']:20s}\t{format_mata_uang(MATA_UANG[mata_uang]['Kurs'])}")
    mata_uang = MataUang(input(f'{biru_tebal}Pilih Mata Uang: {default}').upper())
    print(f"{hijau_tebal}[1]{default} Konversi dari Rupiah ke Mata Uang Asing")
    print(f"{hijau_tebal}[2]{default} Konversi dari Mata Uang Asing ke Rupiah")
    mode_konversi = int(input(f"{biru_tebal}Masukkan Pilihanmu: {default}"))
    if mode_konversi == 1:
        nominal = float(input(f"{biru_tebal}Masukkan Nominal {mata_uang.nama} yang Ingin Dikonversikan ke IDR: {default}"))
        cetak_hasil_konversi(mata_uang, nominal, True)
    else:
        nominal = float(input(f"{biru_tebal}Masukkan Nominal IDR yang Ingin Dikonversikan ke {mata_uang.nama}: {default}"))
        cetak_hasil_konversi(mata_uang, nominal, False)