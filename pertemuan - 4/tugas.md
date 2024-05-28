# Tugas 

- Buatlah kelas `Pembayaran` dengan metode `proses_pembayaran`(self, jumlah) yang tidak melakukan apa-apa (pass).
- Buat kelas `KartuKredit` yang merupakan turunan dari Pembayaran.
  - Kelas `KartuKredit` harus memiliki atribut `nama_kartu` dan `nomor_kartu`.
  - Override metode `proses_pembayaran`(self, jumlah) untuk mencetak pesan bahwa pembayaran sedang diproses menggunakan kartu kredit.

- Buat kelas `PayPal` yang merupakan turunan dari `Pembayaran`.
  - Kelas ini harus memiliki atribut `email`.
  - Override metode `proses_pembayaran`(self, jumlah) untuk mencetak pesan bahwa pembayaran sedang diproses menggunakan PayPal.

- Buat variable untuk mamenggil object `KartuKredit` dan `PayPal`, kemudian panggil metode `proses_pembayaran` pada masing-masing objek.