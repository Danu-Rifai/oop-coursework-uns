from hewan import Hewan

class Layanan:

    def grooming(self, hewan):
        biaya = hewan.biaya_grooming()
        return biaya

    def inap(self, hewan, jumlah_malam=1):
        biaya = hewan.biaya_inap() * jumlah_malam
        return biaya

    def perawatan_bulu(self, hewan):
        biaya = hewan.biaya_perawatan_bulu()
        return biaya
    
    def total_tagihan(self, hewan, layanan_dipilih):
        menu = {
            "grooming": self.grooming,
            "inap": self.inap,
            "perawatan_bulu": self.perawatan_bulu
        }
        total = 0
        for i in layanan_dipilih:
            if i in menu:
                total += menu[i](hewan)
        return total