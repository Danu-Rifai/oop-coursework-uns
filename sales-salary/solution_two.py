# parent class

class Sales:
    def __init__(self, nama: str, target_penjualan: int, total_penjualan: int):
        self.nama = nama
        self.target_penjualan = target_penjualan
        self.total_penjualan = total_penjualan
        self.besaran_komisi_dasar = 0.05
        self.bonus_pencapaian_target = 2000000

        self.PAJAK = 0.05

    def hitung_komisi_dasar(self):
        komisi_dasar = self.besaran_komisi_dasar * self.total_penjualan
        return komisi_dasar

    def hitung_bonus(self):
        if self.total_penjualan >= self.target_penjualan:
            return self.bonus_pencapaian_target
        else:
            return 0
        
    def hitung_pendapatan_kotor(self):
        gaji = getattr(self, 'gaji_pokok', 0)
        komisi_dasar = self.hitung_komisi_dasar()
        bonus = self.hitung_bonus()
        
        komisi_penjualan = self.hitung_komisi_penjualan() if hasattr(self, 'hitung_komisi_penjualan') else 0
        bonus_tambahan = self.hitung_bonus_tambahan() if hasattr(self, 'hitung_bonus_tambahan') else 0
        
        total_kotor = gaji + komisi_dasar + komisi_penjualan + bonus + bonus_tambahan
        return total_kotor
    
    def hitung_pajak(self):
        nominal_pajak = self.hitung_pendapatan_kotor()*self.PAJAK
        return nominal_pajak
    
    def hitung_pendapatan_bersih(self):
        return self.hitung_pendapatan_kotor() - self.hitung_pajak()

    def tampilkan_hasil(self):
        print(f"=========================================")
        print(f"Nama Sales        : {self.nama}")
        print(f"Total Penjualan   : Rp{self.total_penjualan:,}")
        print(f"Target            : Rp{self.target_penjualan:,}")
        print(f"-----------------------------------------")
        print(f"Gaji Pokok        : Rp{getattr(self, 'gaji_pokok', 0):,}")
        print(f"Komisi Dasar      : Rp{self.hitung_komisi_dasar():,}")
        if hasattr(self, 'hitung_komisi_penjualan'):
            print(f"Komisi penjualan  : Rp{self.hitung_komisi_penjualan():,}")
        print(f"Bonus Target      : Rp{self.hitung_bonus():,}")
        if hasattr(self, 'hitung_bonus_tambahan'):
            print(f"Bonus Tambahan    : Rp{self.hitung_bonus_tambahan():,}")
        print(f"-----------------------------------------")
        print(f"Pendapatan Kotor  : Rp{self.hitung_pendapatan_kotor():,}")
        print(f"Nominal Pajak     : Rp{self.hitung_pajak():,}")
        print(f"=========================================")
        print(f"TOTAL BERSIH      : Rp{self.hitung_pendapatan_bersih():,}")
        print(f"=========================================\n")
        
class JuniorSales(Sales):
    def __init__(self, nama, target_penjualan, total_penjualan):
        super().__init__(nama, target_penjualan, total_penjualan)
        self.gaji_pokok = 3000000

class SeniorSales(Sales):
    def __init__(self, nama, target_penjualan, total_penjualan):
        super().__init__(nama, target_penjualan, total_penjualan)
        self.gaji_pokok = 5000000
        self.besaran_komisi_penjualan = 0.02

    def hitung_komisi_penjualan(self):
        komisi_penjualan = self.besaran_komisi_penjualan * self.total_penjualan
        return komisi_penjualan
    
class ManagerSales(Sales):
    def __init__(self, nama, target_penjualan, total_penjualan):
        super().__init__(nama, target_penjualan, total_penjualan)
        self.gaji_pokok = 8000000
        self.besaran_komisi_penjualan = 0.03
        self.besaran_bonus_tambahan = 0.01

    def hitung_komisi_penjualan(self):
        komisi_penjualan = self.besaran_komisi_penjualan * self.total_penjualan
        return komisi_penjualan

    def hitung_bonus_tambahan(self):
        bonus_tambahan = self.besaran_bonus_tambahan * self.hitung_komisi_penjualan()
        return bonus_tambahan

sales1 = ManagerSales('Danu', 5000000, 6000000)
sales1.tampilkan_hasil()