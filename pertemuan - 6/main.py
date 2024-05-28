from abc import ABC, abstractmethod

class ttg_interface_manusia(ABC):

    @abstractmethod
    def berjalan(self):
        pass

    @abstractmethod
    def berlari(self, jarak):
        pass

class atlit(ttg_interface_manusia):
    def berjalan(self):
        print("Aku Atlit. aku mampu berjalan")

    def berlari(self, jarak):
        print("Aku atlit. aku mampu berlari sejauh", jarak, "km")

class petani(ttg_interface_manusia):
    def berjalan(self):
        print("Aku Petani. aku mampu berjalan")
    
    def berlari(self, jarak):
        print("Aku Petani. aku mampu berlari sejauh", jarak, "km")
        


febri = atlit()
aufal = petani()


febri.berjalan()
febri.berlari(42)

aufal.berjalan()
aufal.berlari(10)