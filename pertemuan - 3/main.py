class Manusia: 
    def __init__(self, namaku, umurku):
        self.nama = namaku
        self.umur = umurku
        self.pesan() 
        
    def pesan(self):
        print('Object {} diciptakan .. ! dengan nama : {}'.format(type(self).__name__,self.nama))

class Tentara(Manusia):
    def __init__(self, namaku, umurku, ):
        super().__init__(namaku, umurku)



febri = Manusia('febri', 21)
# print(type(febri).__name__)