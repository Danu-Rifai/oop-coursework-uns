# 🐾 Animal Clinic Management System

> Sistem manajemen klinik hewan berbasis Python dengan pendekatan **Object-Oriented Programming (OOP)** — mencakup pengelolaan data hewan, pemilik, tenaga layanan, hingga perhitungan tagihan secara otomatis.

---

## 📁 Struktur Proyek

```
animal-clinic/
├── hewan.py          # Definisi kelas hewan beserta seluruh subclass-nya
├── pemilik.py        # Kelas Pemilik (data kontak & daftar peliharaan)
├── tenaga_layanan.py # Hierarki kelas dokter dan perawat
├── layanan.py        # Kelas Layanan (kalkulasi biaya per jenis layanan)
├── perawatan.py      # Kelas Perawatan (orkestrasi seluruh komponen)
└── main.py           # Entry point program
```

---

## 🏗️ Arsitektur & Relasi Antar Kelas

Program ini dibangun dengan dua hierarki pewarisan utama yang saling terhubung melalui kelas `Perawatan`.

### 🐱🐶 Hierarki Hewan

```
Hewan
├── Kucing
│   ├── KucingPersia   → grooming: 75K | inap: 100K | perawatan bulu: 60K
│   └── KucingKampung  → grooming: 50K | inap: 75K  | perawatan bulu: 40K
└── Anjing
    ├── AnjingRumahan  → grooming: 100K | inap: 125K | perawatan bulu: 80K
    └── AnjingPenjaga  → grooming: 150K | inap: 200K | perawatan bulu: 120K
```

Setiap subclass hewan mendefinisikan tiga method biaya yang di-*override* sesuai jenis hewannya:
- `biaya_grooming()` — biaya layanan grooming
- `biaya_inap()` — biaya inap **per malam**
- `biaya_perawatan_bulu()` — biaya perawatan bulu khusus

### 👨‍⚕️ Hierarki Tenaga Layanan

```
TenagaLayanan
├── DokterHewan
│   ├── DokterUmum      → konsultasi: 75K×grade | tindakan: 100K×grade
│   └── DokterSpesialis → konsultasi: 150K×grade | tindakan: 250K×grade
└── PerawatHewan
    ├── PerawatInap     → konsultasi: 40K×grade  | tindakan: 60K×grade
    └── PerawatGrooming → konsultasi: 35K×grade  | tindakan: 50K×grade
```

**Sistem Grade Multiplier** (didefinisikan di `tenaga_layanan.py`):

| Grade | Multiplier |
|-------|-----------|
| `A`   | ×1.5      |
| `B`   | ×1.0      |

### 🔗 Relasi Antar Komponen

```
┌─────────────┐     dimiliki oleh     ┌──────────┐
│    Hewan    │ ──────────────────── │  Pemilik  │
└──────┬──────┘                       └──────────┘
       │ dilayani oleh                     │
       ▼                                   │
┌─────────────┐   menggunakan         ┌────┴─────────────┐
│   Layanan   │ ◄──────────────────  │    Perawatan      │
└─────────────┘                       │  (Orchestrator)   │
                                      └────┬─────────────┘
┌─────────────────┐  ditangani oleh        │
│  TenagaLayanan  │ ◄─────────────────────┘
└─────────────────┘
```

Kelas **`Perawatan`** adalah inti dari program — ia menjadi *orchestrator* yang menghubungkan semua komponen:
- Menerima objek `Hewan`, `Pemilik`, dan `TenagaLayanan`
- Mendelegasikan kalkulasi layanan hewan ke kelas `Layanan`
- Menghitung biaya dokter langsung dari objek tenaga layanan yang diberikan
- Menampilkan ringkasan tagihan lengkap via `status_perawatan()`

---

## ⚙️ Cara Kerja Program

### 1. Inisialisasi Objek

Di `main.py`, semua komponen dibuat secara independen terlebih dahulu:

```python
pemilik = Pemilik("Mariadi", "0812-3456-7890", "Bogor")
shaun   = KucingPersia("Shaun", 3, 5, "Mariadi", "Blue", "Tabby", "Blue")
Danu    = DokterSpesialis("dr. Danu", "D-001", "A")
```

### 2. Merakit Perawatan

Seluruh komponen dirangkai dalam satu objek `Perawatan`, beserta daftar layanan yang diinginkan:

```python
informasi = Perawatan(
    shaun,                      # objek hewan
    pemilik,                    # objek pemilik
    Danu,                       # objek dokter/perawat
    ["konsultasi", "tindakan"], # layanan yang ditangani dokter
    ["grooming"]                # layanan untuk hewan
)
```

### 3. Kalkulasi Tagihan

Saat `status_perawatan()` dipanggil, alur kalkulasinya sebagai berikut:

```
status_perawatan()
    └── hitung_total()
            ├── service.total_tagihan(hewan, layanan_hewan)
            │       └── Memanggil biaya_grooming() / biaya_inap() / biaya_perawatan_bulu()
            │           sesuai layanan yang dipilih
            │
            └── total_biaya_dokter()
                    └── Memanggil biaya_konsultasi() / biaya_tindakan()
                        dari objek dokter yang diberikan
```

### 4. Output Program

```
nama hewan      : Shaun
pemilik         : Mariadi
no.telp         : 0812-3456-7890
dokter          : dr. Danu
layana dokter   : ['konsultasi', 'tindakan']
nomor pegawai   : D-001
layanan hewan   : ['grooming']
total tagihan   : Rp.150,000
```

> **Breakdown tagihan contoh:**
> - Grooming KucingPersia: Rp 75.000
> - Konsultasi DokterSpesialis Grade A: Rp 150.000 × 1.5 = Rp 225.000
> - Tindakan DokterSpesialis Grade A: Rp 250.000 × 1.5 = Rp 375.000
> - **Total: Rp 675.000**

---

## 🧩 Detail Kelas

### `Hewan` — Base Class
| Atribut        | Tipe   | Keterangan                  |
|----------------|--------|-----------------------------|
| `nama`         | str    | Nama hewan                  |
| `usia`         | int    | Usia dalam tahun            |
| `berat_badan`  | float  | Berat badan dalam kg        |
| `nama_pemilik` | str    | Nama pemilik hewan          |

### `KucingPersia` — Subclass Kucing
Menambah atribut `warna_mata` di atas atribut `Kucing` (`warna_bulu`, `pola_bulu`).

### `KucingKampung` — Subclass Kucing
Menambah atribut `sudah_steril` (boolean) untuk status sterilisasi.

### `AnjingRumahan` — Subclass Anjing
Menambah atribut `jinak` (boolean) di atas atribut `Anjing` (`ukuran_tubuh`, `sudah_rabies`).

### `AnjingPenjaga` — Subclass Anjing
Menambah atribut `tingkat_agresivitas` sebagai indikator keamanan penanganan.

### `Layanan`
Kelas utility tanpa state yang menyediakan tiga method kalkulasi:
- `grooming(hewan)` — delegasi ke `hewan.biaya_grooming()`
- `inap(hewan, jumlah_malam=1)` — biaya inap dikalikan jumlah malam
- `perawatan_bulu(hewan)` — delegasi ke `hewan.biaya_perawatan_bulu()`
- `total_tagihan(hewan, layanan_dipilih)` — menjumlahkan semua layanan yang dipilih

### `Perawatan`
Kelas utama yang mengorkestrasikan seluruh sistem. Menerima semua komponen saat konstruksi dan menyediakan:
- `hitung_total()` — total biaya layanan hewan + biaya dokter
- `status_perawatan()` — cetak ringkasan perawatan ke terminal

---

## 🚀 Menjalankan Program

Pastikan semua file berada dalam satu direktori, lalu jalankan:

```bash
cd animal-clinic
python main.py
```

> **Catatan:** Program menggunakan relative import antar modul. Pastikan menjalankan dari direktori `animal-clinic/` agar semua import berjalan dengan benar.

---

## 💡 Konsep OOP yang Diterapkan

| Konsep | Implementasi |
|--------|-------------|
| **Inheritance** | `KucingPersia → Kucing → Hewan`, `DokterSpesialis → DokterHewan → TenagaLayanan` |
| **Method Overriding** | Setiap subclass hewan mendefinisikan ulang `biaya_grooming()`, `biaya_inap()`, `biaya_perawatan_bulu()` |
| **Polymorphism** | `Layanan` memanggil method biaya tanpa perlu tahu tipe spesifik hewan |
| **Encapsulation** | Setiap kelas mengelola atribut dan logika biayanya sendiri |
| **Composition** | `Perawatan` menyusun objek `Layanan`, `Hewan`, `Pemilik`, dan `TenagaLayanan` |

---

<div align="center">
  <sub>Dibuat dengan 🐾 untuk pembelajaran OOP Python</sub>
</div>
