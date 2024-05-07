class manusia:
    __nama = ''
    __umur = 0
    def set_nama(self, namaku):
        self.__nama = namaku
        return

    def set_umur(self, umurku):
        self.__umur = umurku
        return

    def get_nama(self):
        return self.__nama


    def get_umur(self):
        return self.__umur




umurku = input('masukkan umur anda : ')

manusia_baru = manusia()
manusia_baru.set_umur(umurku)
print('Umurku adalah ', manusia_baru.get_umur())