"""
Earth Quake App BMKG
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
# from latest_earthquake import ekstraksi_data, tampilkan_data
import latest_earthquake

if __name__ == '__main__':
    print('Aplikasi Utama (Main)')
    result = latest_earthquake.ekstraksi_data()
    latest_earthquake.tampilkan_data(result)

    