from hewan import Hewan, sheep

class Layanan:

    def grooming(self, hewan):
        biaya = hewan.biaya_grooming()
        print(f"Grooming {hewan.nama}, ({hewan.__class__.__name__}): Rp{biaya:,}")
        return biaya

    def inap(self, hewan, jumlah_malam=1):
        biaya = hewan.biaya_inap() * jumlah_malam
        print(f"Inap {hewan.nama} x {jumlah_malam} malam: Rp{biaya:,}")
        return biaya

    def perawatan_bulu(self, hewan):
        biaya = hewan.biaya_perawatan_bulu()
        print(f"Perawatan bulu {hewan.nama}: Rp{biaya:,}")
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
        print(f"total tagihan {hewan.nama}: Rp{total:,}")
        return total
    
