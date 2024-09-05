### 1. Implementasikan ADT papan skor menjadi struktur data. 
### Gunakan struktur data yang telah anda buat untuk mencatat hasil pertandingan antara tim garuda dengan tim elang
- Di menit ke 10 tim garuda menyarangkan gol
- Di menit 40 tim elang menyarangkan gol
- Di menit 70 tim elang menyarangkan gol
- Gol di menit 70 dianulir wasit
- Di menit 87 tim garuda menyarangkan gol


### **PapanSkor**
ADT ini digunakan untuk mencatat gol yang terjadi selama pertandingan antara dua tim, menghapus gol yang dianulir, serta menampilkan skor akhir pertandingan.

### **Properti**:

-   `teams`: Dictionary yang menyimpan informasi mengenai kedua tim, skor yang dicetak, dan menit gol.

#### Struktur Data:

-   **teams** : Dictionary
    -   Key : Nama tim (`tim1`, `tim2`)
    -   Value : Dictionary berisi properti:
        -   `score`: Integer, menyimpan jumlah gol tim.
        -   `menit`: List, menyimpan menit terjadinya gol.

### **Operasi**:

#### 1. **papanSkor(tim1, tim2)**

-   **Deskripsi**: Konstruktor yang menginisialisasi dua tim beserta skor awal (0 gol) dan list kosong untuk mencatat menit terjadinya gol.
    
-   **Parameter**:
    
    -   `tim1`: String, nama tim pertama.
    -   `tim2`: String, nama tim kedua.
-   **Prekondisi**: Dua tim diinisialisasi dengan skor 0 dan list kosong untuk menyimpan menit gol.
    
-   **Postkondisi**: Menciptakan objek papanSkor dengan dua tim yang skornya dimulai dari 0.
    

#### 2. **gol(tim, menit)**

-   **Deskripsi**: Menambahkan gol untuk tim tertentu dan mencatat menit terjadinya gol.
    
-   **Parameter**:
    
    -   `tim`: String, nama tim yang mencetak gol.
    -   `menit`: Integer, menit terjadinya gol.
-   **Prekondisi**: Tim harus ada dalam `teams`.
    
-   **Postkondisi**: Skor tim bertambah 1, dan menit gol ditambahkan ke list `menit` untuk tim tersebut. Pesan dicetak mengindikasikan gol.
    

#### 3. **anulir_gol(tim, menit)**

-   **Deskripsi**: Menghapus gol yang dianulir untuk tim tertentu pada menit tertentu.
    
-   **Parameter**:
    
    -   `tim`: String, nama tim yang golnya dianulir.
    -   `menit`: Integer, menit terjadinya gol yang dianulir.
-   **Prekondisi**: Tim harus ada dalam `teams` dan gol pada menit yang spesifik harus sudah tercatat.
    
-   **Postkondisi**: Skor tim berkurang 1 dan menit gol dihapus dari list `menit`. Pesan dicetak mengindikasikan gol yang dianulir.
    

#### 4. **tampilkan_skor()**

-   **Deskripsi**: Menampilkan skor akhir pertandingan dan menit gol yang dicetak oleh masing-masing tim.
    
-   **Parameter**: Tidak ada.
    
-   **Prekondisi**: Pertandingan telah berlangsung dan beberapa gol mungkin sudah dicatat.
    
-   **Postkondisi**: Skor dari kedua tim dicetak, termasuk menit-menit gol yang terjadi.

```python
class papanSkor:
    def __init__(self, tim1, tim2):
        # Inisialisasi tim dengan mencatat nama tim dan jumlah gol awal (0)
        self.teams = {
            tim1: {
                'score': 0,
                'menit': []
            },
            tim2: {
                'score': 0,
                'menit': []
            }
        }
    
    def gol(self, tim, menit):
        # Mencatat gol oleh tim tertentu di menit tertentu
        if tim in self.teams:
            self.teams[tim]['score'] += 1
            self.teams[tim]['menit'].append(menit)
            print("Tim",tim,"mencetak gol pada menit",menit)
        else:
            print(f"Tim {tim} tidak ditemukan.")
    
    def anulir_gol(self, tim, menit):
        # Menghapus gol dari tim tertentu pada menit tertentu jika dianulir
        if tim in self.teams and menit in self.teams[tim]['menit']:
            self.teams[tim]['score'] -= 1
            self.teams[tim]['menit'].remove(menit)
            print("Skor dari team",tim,"dianulir pada menit",menit)
        else:
            print(f"Gol dari tim {tim} pada menit {menit} tidak ditemukan atau tidak bisa dianulir.")
    
    def tampilkan_skor(self):
        # Menampilkan skor akhir pertandingan dan detil gol dari setiap tim
        for tim, data in self.teams.items():
            print(f"Tim {tim}: {data['score']} gol")
            if data['menit']:
                print(f"Gol di menit: {', '.join(map(str, data['menit']))}")
            else:
                print("Belum ada gol")
        print("\n")


# Contoh penggunaan
skor_pertandingan = papanSkor("Garuda", "Elang")

# Di menit ke 10 tim Garuda menyarangkan gol
skor_pertandingan.gol("Garuda", 10)

# Di menit 40 tim Elang menyarangkan gol
skor_pertandingan.gol("Elang", 40)

# Di menit 70 tim Elang menyarangkan gol
skor_pertandingan.gol("Elang", 70)

# Gol di menit 70 dianulir wasit
skor_pertandingan.anulir_gol("Elang", 70)

# Di menit 87 tim Garuda menyarangkan gol
skor_pertandingan.gol("Garuda", 87)

# Menampilkan skor akhir
skor_pertandingan.tampilkan_skor()

```
Output:
```bash
Tim Garuda mencetak gol pada menit 10
Tim Elang mencetak gol pada menit 40
Tim Elang mencetak gol pada menit 70
Skor dari team Elang dianulir pada menit 70
Tim Garuda mencetak gol pada menit 87
Tim Garuda: 2 gol
Gol di menit: 10, 87
Tim Elang: 1 gol
Gol di menit: 40
```

### 2. Terdapat alat penghitung dzikir. ketika dihidupkan, hitungan dzikirnya mula mula 0. alat tersebut dijalankan dengan cara ditekan. setiap ditekan hitungan dzikir bertambah 1. alat tersebut mengeluarkan peringatan jika telah ditekan 33, 66, atau 99 kali. terdapat tombol reset untuk mengembalikan hitungan menjadi 0

- Buat ADT
- Implementasikan ADT
- beri contoh cara menggunakan struktur data


#### PenghitungDzikir
ADT ini digunakan untuk mencatat jumlah hitungan dzikir setiap kali alat ditekan. Alat ini mengeluarkan peringatan ketika hitungan mencapai 33, 66, atau 99 kali, serta dapat di-reset ke hitungan awal (0).

### **Properti**:

-   `hitung`: Integer, menyimpan jumlah hitungan dzikir.

#### Struktur Data:

-   **hitung**: Integer, dimulai dari 0, dan akan bertambah setiap kali alat ditekan.

### **Operasi**:

#### 1. **PenghitungDzikir()**

-   **Deskripsi**: Konstruktor untuk menginisialisasi hitungan awal dzikir.
    
-   **Prekondisi**: Hitungan dimulai dari 0.
    
-   **Postkondisi**: Objek penghitung dzikir dibuat dengan hitungan awal 0.
    

#### 2. **tekan()**

-   **Deskripsi**: Meningkatkan hitungan dzikir sebanyak 1 setiap kali alat ditekan.
    
-   **Prekondisi**: Alat telah diinisialisasi dan hitungan dimulai dari 0.
    
-   **Postkondisi**: Hitungan bertambah 1 dan jika mencapai 33, 66, atau 99, alat mengeluarkan peringatan.
    

#### 3. **reset()**

-   **Deskripsi**: Mengembalikan hitungan dzikir ke 0.
    
-   **Prekondisi**: Hitungan dzikir berada pada angka tertentu.
    
-   **Postkondisi**: Hitungan kembali ke 0.
    

#### 4. **tampilkan_hitung()**

-   **Deskripsi**: Menampilkan jumlah hitungan dzikir saat ini.
    
-   **Prekondisi**: Tidak ada.
    
-   **Postkondisi**: Hitungan dzikir saat ini ditampilkan.

```python
class PenghitungDzikir:
    def __init__(self):
        # Inisialisasi hitungan awal dzikir
        self.hitung = 0
    
    def tekan(self):
        # Meningkatkan hitungan setiap kali alat ditekan
        self.hitung += 1
        print(f"Hitungan dzikir saat ini: {self.hitung}")
        
        # Mengeluarkan peringatan ketika hitungan mencapai 33, 66, atau 99
        if self.hitung in [33, 66, 99]:
            self.tampilkan_hitung()
            
    def reset(self):
        # Reset hitungan dzikir ke 0
        self.hitung = 0
        print("Hitungan telah di-reset ke 0.")
    
    def tampilkan_hitung(self):
        # Menampilkan hitungan dzikir saat ini
        print(f"Masyaallah, kamu telah berzikir {self.hitung} kali!")

# Contoh penggunaan ADT PenghitungDzikir

# Membuat objek penghitung dzikir
dzikir = PenghitungDzikir()

# Tekan tombol dzikir beberapa kali
for _ in range(35):
    dzikir.tekan()

# Tampilkan hitungan saat ini
dzikir.tampilkan_hitung()

# Reset hitungan
dzikir.reset()

# Tampilkan hitungan setelah reset
dzikir.tampilkan_hitung()

```
Output:
```bash
Hitungan dzikir saat ini: 1
Hitungan dzikir saat ini: 2
Hitungan dzikir saat ini: 3
Hitungan dzikir saat ini: 4
Hitungan dzikir saat ini: 5
Hitungan dzikir saat ini: 6
Hitungan dzikir saat ini: 7
Hitungan dzikir saat ini: 8
Hitungan dzikir saat ini: 9
Hitungan dzikir saat ini: 10
Hitungan dzikir saat ini: 11
Hitungan dzikir saat ini: 12
Hitungan dzikir saat ini: 13
Hitungan dzikir saat ini: 14
Hitungan dzikir saat ini: 15
Hitungan dzikir saat ini: 16
Hitungan dzikir saat ini: 17
Hitungan dzikir saat ini: 18
Hitungan dzikir saat ini: 19
Hitungan dzikir saat ini: 20
Hitungan dzikir saat ini: 21
Hitungan dzikir saat ini: 22
Hitungan dzikir saat ini: 23
Hitungan dzikir saat ini: 24
Hitungan dzikir saat ini: 25
Hitungan dzikir saat ini: 26
Hitungan dzikir saat ini: 27
Hitungan dzikir saat ini: 28
Hitungan dzikir saat ini: 29
Hitungan dzikir saat ini: 30
Hitungan dzikir saat ini: 31
Hitungan dzikir saat ini: 32
Hitungan dzikir saat ini: 33
Masyaallah, kamu telah berzikir 33 kali!
Hitungan dzikir saat ini: 34
Hitungan dzikir saat ini: 35
Masyaallah, kamu telah berzikir 35 kali!
Hitungan telah di-reset ke 0.
Masyaallah, kamu telah berzikir 0 kali!
```