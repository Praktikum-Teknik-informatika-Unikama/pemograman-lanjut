class Pembayaran:
    def proses_pembayaran(self, jumlah):
        pass

class KartuKredit(Pembayaran):
    def __init__(self, nama_kartu, nomor_kartu):
        self.nama_kartu = nama_kartu
        self.nomor_kartu = nomor_kartu

    def proses_pembayaran(self, jumlah):
        return f"Memproses pembayaran {jumlah} menggunakan Kartu Kredit {self.nama_kartu}."

class PayPal(Pembayaran):
    def __init__(self, email):
        self.email = email

    def proses_pembayaran(self, jumlah):
        return f"Memproses pembayaran {jumlah} menggunakan PayPal akun {self.email}."

# Contoh penggunaan
pembayaran_metode = [
    KartuKredit("Visa", "1234-5678-9012-3456"),
    PayPal("user@example.com")
]

for metode in pembayaran_metode:
    print(metode.proses_pembayaran(500000))
