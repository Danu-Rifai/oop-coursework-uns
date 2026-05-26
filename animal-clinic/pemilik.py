class Pemilik:
    def __init__(self, nama, telp, alamat):
        self.nama = nama
        self.telp = telp
        self.alamat = alamat
        self.peliharaan = []

    def tampilkan_info(self):
        print(f'''
nama        : {self.nama}
telp        : {self.telp}
alamat      : {self.alamat}
peliharaan  : {self.peliharaan}
''')