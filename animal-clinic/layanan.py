from hewan import KucingPersia, KucingKampung, AnjingRumahan, AnjingPenjaga

class Layanan:
    def __init__(self, nama_layanan):
        self.nama_layanan = nama_layanan

    def grooming(self, hewan):
        harga_gromming = {
            KucingPersia: 1000,
            KucingKampung: 2000,
            AnjingRumahan: 3000,
            AnjingPenjaga: 5000
        }

    def inap(self, hewan):
        if isinstance(hewan, KucingPersia):
            pass
        elif isinstance(hewan, KucingKampung):
            pass
        elif isinstance(hewan, AnjingRumahan):
            pass
        elif isinstance(hewan, AnjingPenjaga):
            pass

    def perawatan_bulu(self, hewan):
        if isinstance(hewan, KucingPersia):
            pass
        elif isinstance(hewan, KucingKampung):
            pass
        elif isinstance(hewan, AnjingRumahan):
            pass
        elif isinstance(hewan, AnjingPenjaga):
            pass

print(type(KucingKampung))