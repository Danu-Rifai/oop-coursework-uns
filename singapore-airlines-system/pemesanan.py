from jenis_pesawat import JenisPesawat, boeing
from penerbangan import Penerbangan, Penerbangan01, Penerbangan02
from pemesan import Pemesan, pemesan1

class Pemesanan:
    def __init__(self, JenisPesawat, Penerbangan, Pemesan, beratBagasi, penumpang):
        self.jenisPesawat = JenisPesawat
        self.Penerbangan = Penerbangan
        self.Pemesan = Pemesan
        self.beratBagasi = beratBagasi
        self.penumpang = penumpang

    def biaya_bagasi(self):
        biayaBagasi = 0

        if self.beratBagasi <= 30:
            biayaBagasi = 0
        elif self.beratBagasi > 30:
            biayaBagasi = (self.beratBagasi-30)*50000

        return biayaBagasi

    def jumlah_penumpang(self):
        jumlah_penumpang = len(self.penumpang)
        return jumlah_penumpang
    
    def total_tarif(self):
        tarif_maskapai = self.Penerbangan.price
        tarif = tarif_maskapai*self.jumlah_penumpang()
        
        if self.jumlah_penumpang() > 3 and all(item == 'dewasa' for item in self.penumpang):
            tarif -= tarif*(3/100)
        elif self.jumlah_penumpang() > 3 and 'anak' in self.penumpang:
            tarif -= tarif*(2/100)

        total_tarif = tarif+self.biaya_bagasi()
        return total_tarif

pemesanan1 = Pemesanan(boeing, Penerbangan01, pemesan1, 30, ['dewasa', 'dewasa', 'dewasa'])
pemesanan2 = Pemesanan(boeing, Penerbangan02, pemesan1, 31, ['dewasa', 'dewasa', 'dewasa', 'dewasa', 'anak'])

print(f'''
===== SINGAPORE AIRLINES =====
nama pemesan        : {pemesanan2.Pemesan.name}
no.ktp              : {pemesanan2.Pemesan.no_ktp}
email               : {pemesanan2.Pemesan.email}
no.hp               : {pemesanan2.Pemesan.phoneNumber}
jumlah penumpang    : {pemesanan2.jumlah_penumpang()}
nama pesawat        : {pemesanan2.jenisPesawat.name}
asal                : {pemesanan2.Penerbangan.departure}
tujuan              : {pemesanan2.Penerbangan.destination}
waktu keberangkatan : {pemesanan2.Penerbangan.date} {pemesanan1.Penerbangan.time}
biaya bagasi        : {pemesanan2.biaya_bagasi()}
total harga         : Rp.{int(pemesanan2.total_tarif()):,}
''')

pemesanan1.total_tarif()