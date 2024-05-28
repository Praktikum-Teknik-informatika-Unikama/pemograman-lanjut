def hitung_luas_persegi(sisi):
    try:
        return sisi * sisi
    except TypeError:
        return 'Type data yang anda masukkan tidak sesuai !!!'
    
sisi = input('masukkan sisi : ')
persegi = hitung_luas_persegi(sisi)
print(persegi)
