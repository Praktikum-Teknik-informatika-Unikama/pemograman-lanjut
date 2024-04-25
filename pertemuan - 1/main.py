import sys

class Data_diri : 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def say_hello(self):
        print('hallo dunia',self.nama) 

    def show_detail(self):
        print("=======================================")
        print("++++++ data diri berhasil dibuat ++++++\nnama : ",self.nama, "\numur : ",self.umur,"\n+++++++++++++++ Selesai +++++++++++++++")
 

nama = str(input('Masukkan nama anda : '))
umur = int(input('Masukkan umur anda : '))
new_data_diri = Data_diri(nama, umur)
new_data_diri.show_detail()


sys.exit(0)