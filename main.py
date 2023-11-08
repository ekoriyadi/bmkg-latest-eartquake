"""
Earth Quake App BMKG
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal : 09 November 2023,
    Waktu : 00:25:05 WIB
    Magnitudo : 5.4
    Kedalaman : 10 km
    Tikor : 5.40 LS - 130.25 BT
    Pusat gempa : 256 km BaratDaya SERAMBAGIANTIMUR-MALUKU
    Potensi : tidak berpotensi TSUNAMI

    """
    hasil = dict()
    hasil['tanggal'] = '09 November 2023'
    hasil['waktu'] = '00:25:05 WIB'
    hasil['magnitudo'] = 5.4
    hasil['tikor'] = {'ls' : 5.40, 'bt' : 130.25}
    hasil['pusatgempa'] = '256 km BaratDaya SERAMBAGIANTIMUR-MALUKU'
    hasil['potensi'] = 'tidak berpotensi TSUNAMI'
    return hasil


def tampilkan_data(result):
    print('# Gempa terkini berdasarkn BMKG')
    # print(result)
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Titik Koordinat: LS= {result['tikor']['ls']}, BT= {result['tikor']['bt']}")
    print(f"Pusat gempa {result['pusatgempa']}")
    print(f"Potensi {result['potensi']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)

    