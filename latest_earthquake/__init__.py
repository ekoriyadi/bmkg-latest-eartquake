import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        datetime = soup.find('span', {'class': 'waktu'})
        dt = datetime.text.split(', ')
        print(f'Scrap dari website : {title.string}')

        tag_list = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        list = tag_list.findChildren('li')
        # print(list)
        i = 0
        skala = None
        ls = None
        bt = None
        pusatgempa = None
        potensi = None
        for res in list:
            print(i, res)
            if i == 1:
                skala = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                tikor = res.text.split(' - ')
                ls = tikor[0]
                bt = tikor[1]
            elif i == 4:
                pusatgempa = res.text
            elif i == 5:
                potensi = res.text
            i = i+1

    # print(content)
    # soup = BeautifulSoup(content)
    # print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = dt[0]            # '09 November 2023'
    hasil['waktu'] = dt[1]              # '00:25:05 WIB'
    hasil['magnitudo'] = skala          # 5.4
    hasil['kedalaman'] = kedalaman
    hasil['tikor'] = {'ls': ls, 'bt': bt}
    hasil['pusatgempa'] = pusatgempa    # "256 km BaratDaya SERAM BAGIAN TIMUR-MALUKU"
    hasil['potensi'] = potensi          # 'tidak berpotensi TSUNAMI'
    return hasil


def tampilkan_data(result):
    if result is None:
        print("URL salah. Data tidak dapat ditampilkan")
        return

    print('# Gempa terkini berdasarkan BMKG')
    # print(result)
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Titik Koordinat: LS= {result['tikor']['ls']}, BT= {result['tikor']['bt']}")
    print(f"Pusat gempa: {result['pusatgempa']}")
    print(f"Potensi: {result['potensi']}")


if __name__ == '__main__':
    print('Ini adalah package latest EQ')
    print('Hai')
