# ==========================================
# TUGAS KRIPTOGRAFI: ALGORITMA RC4 (FROM SCRATCH)
# ==========================================

# LANGKAH 1: KSA (Key-Scheduling Algorithm)
# Fungsi ini bertugas untuk mengacak array S (berisi angka 0-255) menggunakan Kunci
def ksa(key):
    key_length = len(key)
    S = list(range(256)) # Membuat list angka 0 sampai 255
    j = 0
    for i in range(256):
        # Rumus mengacak/menukar posisi berdasarkan kunci
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Proses pertukaran posisi (Swap)
    return S

# LANGKAH 2: PRGA (Pseudo-Random Generation Algorithm)
# Fungsi ini menghasilkan aliran kunci (Keystream) yang panjangnya sama dengan panjang pesan
def prga(S, text_length):
    i = 0
    j = 0
    keystream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap lagi
        K = S[(S[i] + S[j]) % 256] # Mengambil nilai keystream
        keystream.append(K)
    return keystream

# FUNGSI UTAMA RC4 (Untuk Enkripsi dan Dekripsi)
def rc4_encrypt_decrypt(key, text_ascii):
    # Ubah string kunci menjadi daftar angka (ASCII)
    key_ascii = [ord(c) for c in key]
    
    # Panggil fungsi KSA untuk mengacak array
    S = ksa(key_ascii)
    
    # Panggil fungsi PRGA untuk membuat keystream
    keystream = prga(S, len(text_ascii))
    
    # LANGKAH 3: Operasi XOR antara Pesan dan Keystream
    result = []
    for i in range(len(text_ascii)):
        # Tanda '^' di Python adalah operasi XOR
        hasil_xor = text_ascii[i] ^ keystream[i]
        result.append(hasil_xor)
        
    return result

# 1. Input Pesan dan Kunci
pesan_asli = input("Masukkan pesan asli : ")
kunci = input("Masukkan kunci rahasia   : ")

# Mengubah pesan asli menjadi angka ASCII
pesan_ascii = [ord(c) for c in pesan_asli]

# 2. PROSES ENKRIPSI
# Memasukkan kunci dan pesan ke dalam fungsi RC4
ciphertext_ascii = rc4_encrypt_decrypt(kunci, pesan_ascii)
# Mengubah hasil ASCII kembali ke dalam bentuk huruf dan format Hexadecimal agar rapi
ciphertext_hex = ''.join([format(c, '02x') for c in ciphertext_ascii])
print("\n[+] Hasil Enkripsi (Ciphertext - Hex) :", ciphertext_hex)

# 3. PROSES DEKRIPSI
# Untuk dekripsi di RC4, caranya SAMA PERSIS dengan enkripsi.
# Kita masukkan ciphertext dan kunci yang sama ke fungsi RC4.
plaintext_ascii_kembali = rc4_encrypt_decrypt(kunci, ciphertext_ascii)
# Mengubah angka kembali menjadi teks
plaintext_kembali = ''.join([chr(c) for c in plaintext_ascii_kembali])
print("[+] Hasil Dekripsi (Pesan Kembali)    :", plaintext_kembali)
print("====================================")