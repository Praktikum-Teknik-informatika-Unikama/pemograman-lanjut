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
        namaku = self.__nama.isdigit()
        if self.__nama == '':
            print('nama tidak boleh kosong')
        elif namaku == False : 
            print('Selamat datang', self.__nama)
        else : 
            print('Masukkan nama dengan benar')


    def get_umur(self):
        umurku = self.__umur.isdigit()  # type: ignore
        if umurku == True : 
            print('Umur anda saat ini adalah', self.__umur)
        else : 
            print('Masukkan umur dengan benar')
        

namaku = input('masukkan nama anda : ')
umurku = input('masukkan umur anda : ')

manusia_baru = manusia()
manusia_baru.set_nama(namaku)
manusia_baru.set_umur(umurku)
manusia_baru.get_nama()
manusia_baru.get_umur()