class manusia:
    __nama = ''
    def set_nama(self, namaku='manusia'):
        self.__nama = namaku

    def get_nama(self):
        return self.__nama

manusia_baru = manusia()
print('sebelum diset', manusia_baru.get_nama())
manusia_baru.set_nama('aufal')
print('setelah di set nama', manusia_baru.get_nama())