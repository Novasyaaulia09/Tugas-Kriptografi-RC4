# Tugas-Kriptografi-RC4
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

# Cara menjalankan program
Pastikan sudah terinstal Python 3
1. Lakukan clone repository
   '''
   git clone https://github.com/Novasyaaulia09/Tugas-Kriptografi-RC4.git](https://github.com/Novasyaaulia09/Tugas-Kriptografi-RC4.git
   '''
3. Arahkan direkotori ke dalam folder repository
   cd Tugas-Kriptografi-RC4
4. Jalankan file program dengan perintah berikut
   python algoritma_rc4.py
5. Program akan berjalan
