"""
## Tugas
- Buatlah sebuah kelas Mahasiswa yang memiliki atribut nama, NIM, dan IPK. Atribut-atribut tersebut tidak boleh diakses langsung dari luar kelas.
- Implementasikan metode untuk mengatur nilai atribut nama, NIM, dan IPK dari luar kelas Mahasiswa.
- Implementasikan metode untuk mengambil nilai atribut nama, NIM, dan IPK dari luar kelas Mahasiswa.
- Berikan contoh penggunaan kelas Mahasiswa beserta cara mengakses dan mengubah nilai atributnya.
"""



class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.__nama = nama
        self.__nim = nim
        self.__ipk = ipk

    def set_nama(self, nama):
        # Metode untuk mengatur nilai atribut nama
        self.__nama = nama

    def set_nim(self, nim):
        # Metode untuk mengatur nilai atribut nim
        self.__nim = nim

    def set_ipk(self, ipk):
        # Metode untuk mengatur nilai atribut ipk
        self.__ipk = ipk

    def get_nama(self):
        # Metode untuk mengambil nilai atribut nama
        return self.__nama

    def get_nim(self):
        # Metode untuk mengambil nilai atribut nim
        return self.__nim

    def get_ipk(self):
        # Metode untuk mengambil nilai atribut ipk
        return self.__ipk

# Contoh penggunaan kelas Mahasiswa
aufal = Mahasiswa("aufal", "2134", 3.75)

# Mengakses nilai atribut menggunakan metode get
aufal.set_nama('sudah diganti')
print("Nama:", aufal.get_nama())
print("NIM:", aufal.get_nim())
print("IPK:", aufal.get_ipk())

