class Hewan:
    def __init__(self, nama, usia, berat_badan, nama_pemilik):
        self.nama = nama
        self.usia = usia
        self.berat_badan = berat_badan
        self.nama_pemilik = nama_pemilik

class Kucing(Hewan):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, warna_bulu, pola_bulu):
        super().__init__(nama, usia, berat_badan, nama_pemilik)
        self.warna_bulu = warna_bulu
        self.pola_bulu = pola_bulu

class Anjing(Hewan):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, ukuran_tubuh, sudah_rabies):
        super().__init__(nama, usia, berat_badan, nama_pemilik)
        self.ukuran_tubuh = ukuran_tubuh
        self.sudah_rabies = sudah_rabies

class KucingPersia(Kucing):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, warna_bulu, pola_bulu, warna_mata):
        super().__init__(nama, usia, berat_badan, nama_pemilik, warna_bulu, pola_bulu)
        self.warna_mata = warna_mata

    def biaya_grooming(self):
        return 75_000

    def biaya_inap(self):
        return 100_000

    def biaya_perawatan_bulu(self):
        return 60_000   

class KucingKampung(Kucing):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, warna_bulu, pola_bulu, sudah_steril):
        super().__init__(nama, usia, berat_badan, nama_pemilik, warna_bulu, pola_bulu)
        self.sudah_steril = sudah_steril

    def biaya_grooming(self):
        return 50_000

    def biaya_inap(self):
        return 75_000

    def biaya_perawatan_bulu(self):
        return 40_000

class AnjingRumahan(Anjing):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, ukuran_tubuh, sudah_rabies, jinak):
        super().__init__(nama, usia, berat_badan, nama_pemilik, ukuran_tubuh, sudah_rabies)
        self.jinak = jinak

    def biaya_grooming(self):
        return 100_000

    def biaya_inap(self):
        return 125_000

    def biaya_perawatan_bulu(self):
        return 80_000

class AnjingPenjaga(Anjing):
    def __init__(self, nama, usia, berat_badan, nama_pemilik, ukuran_tubuh, sudah_rabies, tingkat_agresivitas):
        super().__init__(nama, usia, berat_badan, nama_pemilik, ukuran_tubuh, sudah_rabies)
        self.tingkat_agresivitas = tingkat_agresivitas

    def biaya_grooming(self):
        return 150_000

    def biaya_inap(self):
        return 200_000

    def biaya_perawatan_bulu(self):
        return 120_000
    
sheep = KucingPersia("sheep", 3, 5, "Mariadi", "Blue", "Tabby", "Blue")