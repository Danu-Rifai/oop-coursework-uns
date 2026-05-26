# ✈️ Singapore Airlines Booking System

> Simulasi sistem pemesanan tiket pesawat berbasis Python dengan pendekatan **Object-Oriented Programming (OOP)** — mencakup manajemen penerbangan, penumpang, bagasi, dan kalkulasi tarif otomatis dengan sistem diskon.

---

## 📁 Struktur Proyek

```
singapore-airlines-system/
├── jenis_pesawat.py  # Kelas JenisPesawat (spesifikasi armada)
├── penerbangan.py    # Kelas Penerbangan (rute & jadwal)
├── pemesan.py        # Kelas Pemesan (data penumpang)
└── pemesanan.py      # Kelas Pemesanan (orkestrasi + kalkulasi tarif)
```

---

## 🏗️ Arsitektur & Relasi Antar Kelas

Program ini menggunakan pola **Composition** — semua kelas independen, kemudian dirangkai oleh `Pemesanan` sebagai orchestrator.

### 🔗 Relasi Antar Komponen

```
┌───────────────┐      menggunakan     ┌────────────────────┐
│  JenisPesawat │ ──────────────────► │                    │
└───────────────┘                     │     Pemesanan      │
                                      │   (Orchestrator)   │
┌───────────────┐      terbang di     │                    │
│  Penerbangan  │ ──────────────────► │                    │
└───────────────┘                     └─────────┬──────────┘
                                                │
┌───────────────┐      dipesan oleh             │
│   Pemesan     │ ◄─────────────────────────────┘
└───────────────┘
```

`Pemesanan` menerima objek dari ketiga kelas lain dan bertanggung jawab atas seluruh logika bisnis — kalkulasi biaya bagasi, diskon grup, dan total tarif akhir.

---

## ⚙️ Cara Kerja Program

### 1. Definisi Armada & Rute

```python
boeing = JenisPesawat('Boeing', 120, 920, 17000)
airBus = JenisPesawat('AirBus', 200, 650, 12000)

Penerbangan01 = Penerbangan('Yogyakarta', 'Boeing', 'Oslo',   date(2026, 5, 12), '18:30', 1_000_000)
Penerbangan02 = Penerbangan('Solo',        'Boeing', 'Florida', date(2027, 2, 1),  '08:30', 2_000_000)
```

### 2. Data Pemesan & Pemesanan

```python
pemesan1 = Pemesan('3306082108100005', 'Danu Rifai', 'rifaidanu12@gmail.com', '085693455370')

pemesanan = Pemesanan(
    boeing,                                   # armada pesawat
    Penerbangan02,                            # rute penerbangan
    pemesan1,                                 # data pemesan
    31,                                       # berat bagasi (kg)
    ['dewasa', 'dewasa', 'dewasa', 'dewasa', 'anak']  # daftar penumpang
)
```

### 3. Alur Kalkulasi Tarif

```
total_tarif()
    ├── jumlah_penumpang()
    │       └── len(self.penumpang)
    │
    ├── Tarif dasar = harga_penerbangan × jumlah_penumpang
    │
    ├── Sistem Diskon Grup:
    │       ├── > 3 penumpang, SEMUA dewasa → diskon 3%
    │       └── > 3 penumpang, ADA anak    → diskon 2%
    │
    └── biaya_bagasi()
            ├── ≤ 30 kg → gratis
            └── > 30 kg → (berat - 30) × Rp 50.000/kg
```

### 4. Output Program

```
===== SINGAPORE AIRLINES =====
nama pemesan        : Danu Rifai
no.ktp              : 3306082108100005
email               : rifaidanu12@gmail.com
no.hp               : 085693455370
jumlah penumpang    : 5
nama pesawat        : Boeing
asal                : Solo
tujuan              : Florida
waktu keberangkatan : 2027-02-01 18:30
biaya bagasi        : 50000
total harga         : Rp.9,850,000
```

> **Breakdown tagihan:**
> - Tarif dasar: Rp 2.000.000 × 5 penumpang = Rp 10.000.000
> - Diskon (ada anak, >3 penumpang): −2% = −Rp 200.000
> - Biaya bagasi: (31 − 30) kg × Rp 50.000 = Rp 50.000
> - **Total: Rp 9.850.000**

---

## 🧩 Detail Kelas

### `JenisPesawat`
| Atribut        | Tipe  | Keterangan                  |
|----------------|-------|-----------------------------|
| `name`         | str   | Nama maskapai/tipe pesawat  |
| `seatCapacity` | int   | Kapasitas kursi             |
| `maxSpeed`     | int   | Kecepatan maksimum (km/h)   |
| `planeRange`   | int   | Jangkauan terbang (km)      |

### `Penerbangan`
| Atribut       | Tipe     | Keterangan                      |
|---------------|----------|---------------------------------|
| `departure`   | str      | Kota asal                       |
| `pesawat`     | str      | Tipe pesawat                    |
| `destination` | str      | Kota tujuan                     |
| `date`        | date     | Tanggal keberangkatan           |
| `time`        | str      | Jam keberangkatan (HH:MM)       |
| `price`       | int      | Harga tiket per orang (Rp)      |

### `Pemesan`
| Atribut       | Tipe | Keterangan           |
|---------------|------|----------------------|
| `no_ktp`      | str  | Nomor KTP pemesan    |
| `name`        | str  | Nama lengkap         |
| `email`       | str  | Alamat email         |
| `phoneNumber` | str  | Nomor telepon        |

### `Pemesanan`
Kelas utama yang mengorkestrasikan sistem. Method yang tersedia:

| Method                | Keterangan                                          |
|-----------------------|-----------------------------------------------------|
| `jumlah_penumpang()`  | Mengembalikan jumlah penumpang dalam pemesanan      |
| `biaya_bagasi()`      | Menghitung biaya kelebihan bagasi (>30 kg)          |
| `total_tarif()`       | Total biaya = (harga × penumpang) − diskon + bagasi |

---

## 💡 Konsep OOP yang Diterapkan

| Konsep | Implementasi |
|--------|-------------|
| **Encapsulation** | Setiap kelas menyimpan dan mengelola datanya sendiri |
| **Composition** | `Pemesanan` menyusun `JenisPesawat`, `Penerbangan`, dan `Pemesan` |
| **Single Responsibility** | Satu kelas = satu tanggung jawab spesifik |

---

## 🚀 Menjalankan Program

```bash
cd singapore-airlines-system
python pemesanan.py
```

> **Catatan:** `pemesanan.py` sudah berisi data contoh dan akan langsung mencetak hasil pemesanan ke terminal saat dijalankan.

---

<div align="center">
  <sub>Dibuat dengan ✈️ untuk pembelajaran OOP Python</sub>
</div>
