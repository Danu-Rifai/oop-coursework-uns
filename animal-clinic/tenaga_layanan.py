class TenagaLayanan:
    def __init__(self, nama, nomor_pegawai):
        self.nama = nama
        self.nomor_pegawai = nomor_pegawai

class DokterHewan(TenagaLayanan):
    def __init__(self, nama, nomor_pegawai):
        super().__init__(nama, nomor_pegawai)

class PerawatHewan(TenagaLayanan):
    def __init__(self, nama, nomor_pegawai):
        super().__init__(nama, nomor_pegawai)

class DokterUmum(DokterHewan):
    pass

class DokterSpesialis(DokterHewan):
    pass

class PerawatInap(PerawatHewan):
    pass

class PerawatGrooming(PerawatHewan):
    pass