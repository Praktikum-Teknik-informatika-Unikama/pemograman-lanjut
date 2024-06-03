from abc import ABC,abstractmethod

class Poligon(ABC):
    @abstractmethod
    def jumlah_sisi(self):
        pass

class Segitiga(Poligon):
    def jumlah_sisi(self):
        print('saya memiliki 3 sisi')

class Segiempat(Poligon):
    def jumlah_sisi(self):
        print('saya memiliki 4 sisi')

segitiga = Segitiga()
segitiga.jumlah_sisi()

segiempat = Segiempat()
segiempat.jumlah_sisi()