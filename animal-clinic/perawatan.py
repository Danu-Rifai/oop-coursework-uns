from layanan import Layanan
from pemilik import Pemilik
from tenaga_layanan import DokterUmum, DokterSpesialis, PerawatGrooming, PerawatInap
from hewan import KucingPersia, KucingKampung, AnjingPenjaga, AnjingRumahan

class Perawatan:
    def __init__(self, hewan, pemilik, dokter, layanan_dokter, layanan_hewan):
        self.hewan = hewan
        self.pemilik = pemilik
        self.dokter = dokter
        self.layanan_dokter = layanan_dokter
        self.layanan_hewan = layanan_hewan
        self.service = Layanan()

    def total_biaya_dokter(self):
        tipe_layanan = {
            "konsultasi": self.dokter.biaya_konsultasi,
            "tindakan": self.dokter.biaya_tindakan
        }

        total = 0
        for i in self.layanan_dokter:
            if i in tipe_layanan:
                total += tipe_layanan[i]()
        return total

    def hitung_total(self):
        biaya_layanan =  self.service.total_tagihan(self.hewan, self.layanan_hewan)
        biaya_dokter = self.total_biaya_dokter()
        return biaya_layanan + biaya_dokter
    
    def status_perawatan(self):
        total = self.hitung_total()
        print(f'''
nama hewan      : {self.hewan.nama}
pemilik         : {self.pemilik.nama}
no.telp         : {self.pemilik.telp}
dokter          : {self.dokter.nama}
layana dokter   : {self.layanan_dokter}
nomor pegawai   : {self.dokter.nomor_pegawai}
layanan hewan   : {self.layanan_hewan}
total tagihan   : Rp.{total:,}'''
        )
    
