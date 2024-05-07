class Manusia:
    nama = ''
    umur = 0

    def __init__(self,namaku,umurku):
        self.nama = namaku
        self.umur = umurku
        print('Object Manusia berhasil dibuat, dengan nama :', self.nama)

    def get_nama(self):
        print('nama saya adalah', self.nama)
        return

class Tentara(Manusia):
    amu = 0
    granat = 0
    def __init__(self, namaku, umurku, jml_amunisi, jml_granat):
        self.nama = namaku
        self.umur = umurku
        self.amu = jml_amunisi
        self.granat = jml_granat
        print('Object Tentara berhasil dibuat, dengan nama :', self.nama)


class Prajurit(Tentara):
    pangkat = ''
    def __init__(self, namaku, umurku, jml_amunisi, jml_granat, pangkatku):
        self.nama = namaku
        self.umur = umurku
        self.amu = jml_amunisi
        self.granat = jml_granat
        self.pangkat = pangkatku

        print('Object Prajurit berhasil dibuat, dengan nama :', self.nama, ' dan berpangkat', self.pangkat)

febri = Tentara('febri', 20, 9, 2)
udin = Prajurit('udin', 19, 4, 1, 'jendral')

febri.get_nama()