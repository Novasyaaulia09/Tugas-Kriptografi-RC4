# Implementasi Algortima RC4 (From Scratch- Python)
# Deskripsi Proyek
Repository ini berisi implementasi algoritma kriptografi RC4 (Rivest Chiper 4) yang dibuat menggunakan bahasa pemrograman Python tanpa library kriptografi tambahan.
Program ini dapat melakukan:
- Enkripsi pesan
- Dekkripsi pesan
- Menampilkan chipertext dalam format hexadecimal

# Cara kerja RC4
1. Menginisialisasi array S berisi 0-255
2. Mengacak array menggunakan kunci KSA
3. Menghasilkan keystream PRGA
4. Melakukan XOR antara plaintext dan keystream untuk membuat chiperetxt
5. Melakukan XOR antara chipertext dan keystream untuk menghasilkan kembali plaintext
Operasi utama RC4 adalah XOR maka proses enkripsi dan dekripsi menggunakan algoritma yang sama
A ⊕ B ⊕ B = A

# Cara Menjalankan Program

Pastikan sudah terinstal Python 3

## 1. Clone Repository
```
git clone https://github.com/Novasyaaulia09/Tugas-Kriptografi-RC4.git
```

## 2. Masuk ke Folder Repository
```
cd Tugas-Kriptografi-RC4
```

## 3. Jalankan Program
```
python algoritma_rc4.py
```

Program akan berjalan.

## Contoh Output Program

Berikut contoh hasil ketika program dijalankan:

```
Masukkan pesan asli      : kriptografi
Masukkan kunci rahasia   : 123

[+] Hasil Enkripsi (Ciphertext - Hex) : 3882d6f2911b638944056a
[+] Hasil Dekripsi (Pesan Kembali)    : kriptografi
====================================
```
