# Tugas 1

- Buatlah kelas `Pembayaran` dengan metode `proses_pembayaran`(self, jumlah) yang tidak melakukan apa-apa (pass).
- Buat kelas `KartuKredit` yang merupakan turunan dari Pembayaran.
  - Kelas `KartuKredit` harus memiliki atribut `nama_kartu` dan `nomor_kartu`.
  - Override metode `proses_pembayaran`(self, jumlah) untuk mencetak pesan bahwa pembayaran sedang diproses menggunakan kartu kredit.

- Buat kelas `PayPal` yang merupakan turunan dari `Pembayaran`.
  - Kelas ini harus memiliki atribut `email`.
  - Override metode `proses_pembayaran`(self, jumlah) untuk mencetak pesan bahwa pembayaran sedang diproses menggunakan PayPal.

- Buat variable untuk mamenggil object `KartuKredit` dan `PayPal`, kemudian panggil metode `proses_pembayaran` pada masing-masing objek.


# Tugas

- Buat kelas abstrak `LibraryItem` dengan metode abstrak `display_info` dan `calculate_late_fee`.
- Buat kelas turunan `Book`, dan `DVD` yang mengimplementasikan metode dari kelas abstrak `LibraryItem`.
- Implementasikan metode `display_info` untuk menampilkan informasi detail tentang item.
- Implementasikan metode `calculate_late_fee` untuk menghitung biaya keterlambatan berdasarkan jumlah hari keterlambatan dan tarif per hari yang berbeda untuk setiap jenis item.

## Book:
Memiliki atribut `title`, `author`, dan `daily_late_fee` (misalnya, 5000 per hari).
Biaya keterlambatan dihitung sebagai jumlah hari keterlambatan dikalikan dengan `daily_late_fee`.


## DVD:
Memiliki atribut `title`, `director`, dan `daily_late_fee` (misalnya, 10000 per hari).
Biaya keterlambatan dihitung sebagai jumlah hari keterlambatan dikalikan dengan `daily_late_fee`.