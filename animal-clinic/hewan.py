class Hewan:
    def __init__(self, nama, usia, berat_badan, nama_pemilik):
        self.nama = nama
        self.usia = usia
        self.berat_badan = berat_badan
        self.nama_pemilik = nama_pemilik

class Kucing(Hewan):
    def __init__(self, nama, usia, berat_badan, nama_pemilik):
        super().__init__(nama, usia, berat_badan, nama_pemilik)

class Anjing(Hewan):
    def __init__(self, nama, usia, berat_badan, nama_pemilik):
        super().__init__(nama, usia, berat_badan, nama_pemilik)

class KucingPersia(Kucing):
    pass

class KucingKampung(Kucing):
    pass

class AnjingRumahan(Anjing):
    pass

class AnjingPenjaga(Anjing):
    pass