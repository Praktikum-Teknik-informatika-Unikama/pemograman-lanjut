class Kendaraan :
    def __init__(self, nama, warna, harga):
        self.nama = nama
        self.warna = warna
        self.harga = harga

    def  tampilkan(self):
        print('Details: {} {} {}'.format(self.nama, self.warna, self.harga))

    def kecepatan_max(self):
        pass
    
    def change_gear(self):
        pass

class Mobil(Kendaraan):

    def kecepatan_max(self):
        print('kecepatan kendaraan max 240 km/jam')
    def change_gear(self):
        print('kendaraan ini bisa berganti gear sampai 7')

class Truck(Kendaraan):

    def kecepatan_max(self):
        print('kecepatan kendaraan max 160 km/jam')
    def change_gear(self):
        print('kendaraan ini bisa berganti gear sampai 10')

"UNTUK CLASS MOBIL"
mobil = Mobil('toyota', 'ungu', 1000)
mobil.tampilkan()
mobil.kecepatan_max()
mobil.change_gear()

print("===================================")
"UNTUK CLASS KENDARAAN"
truck = Truck('Truck', 'kuning', 2000)
truck.tampilkan()
truck.kecepatan_max()
truck.change_gear()