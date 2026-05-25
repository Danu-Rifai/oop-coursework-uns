GRADE = {
    "A": 1.5,   
    "B": 1.0
}

class TenagaLayanan:
    def __init__(self, nama, nomor_pegawai):
        self.nama = nama
        self.nomor_pegawai = nomor_pegawai

class DokterHewan(TenagaLayanan):
    def __init__(self, nama, nomor_pegawai):
        super().__init__(nama, nomor_pegawai)

    def biaya_konsultasi(self):
        return 100_000

    def biaya_tindakan(self):
        return 150_000

class PerawatHewan(TenagaLayanan):
    def __init__(self, nama, nomor_pegawai):
        super().__init__(nama, nomor_pegawai)

    def biaya_konsultasi(self):
        return 50_000

    def biaya_tindakan(self):
        return 75_000

class DokterUmum(DokterHewan):
    def __init__(self, nama, nomor_pegawai, grade="B"):
        super().__init__(nama, nomor_pegawai)
        self.grade = grade

    def biaya_konsultasi(self):
        return int(75_000 * GRADE[self.grade])

    def biaya_tindakan(self):
        return int(100_000 * GRADE[self.grade])

class DokterSpesialis(DokterHewan):
    def __init__(self, nama, nomor_pegawai, GRADE="B"):
        super().__init__(nama, nomor_pegawai)
        self.grade = GRADE
        
    def biaya_konsultasi(self):
        return int(150_000 * GRADE[self.grade])

    def biaya_tindakan(self):
        return int(250_000 * GRADE[self.grade])

class PerawatInap(PerawatHewan):
    def __init__(self, nama, nomor_pegawai, grade="B"):
        super().__init__(nama, nomor_pegawai)
        self.grade = grade

    def biaya_konsultasi(self):
        return int(40_000 * GRADE[self.grade])

    def biaya_tindakan(self):
        return int(60_000 * GRADE[self.grade])

class PerawatGrooming(PerawatHewan):
    def __init__(self, nama, nomor_pegawai, grade="B"):
        super().__init__(nama, nomor_pegawai)
        self.grade = grade

    def biaya_konsultasi(self):
        return int(35_000 * GRADE[self.grade])

    def biaya_tindakan(self):
        return int(50_000 * GRADE[self.grade])