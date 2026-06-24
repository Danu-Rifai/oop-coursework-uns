class Sales:
    def __init__(self, name, totalSales, targetSales):
        self.name = name
        self.totalSales = totalSales
        self.targetSales = targetSales
        self.komisiDasar = totalSales*0.05
        self.pajak = 0.05
        self.bonusPenjualan = 0

    def hitungBonusPenjualan(self):
        if self.totalSales >= self.targetSales:
            self.bonusPenjualan = 2000000
        
        return self.bonusPenjualan
    
class SalesJunior(Sales):
    def __init__(self, name, totalSales, targetSales):
        super().__init__(name, totalSales, targetSales)
        self.gajiPokok = 3000000

    def hitungGaji(self):
        total_gaji = (self.gajiPokok + self.komisiDasar + self.hitungBonusPenjualan())
        gaji_akhir = total_gaji - (total_gaji*self.pajak)
        return gaji_akhir
    
    def tampilkanGaji(self):
        print(f'''
nama                : {self.name}
total penjualan     : {self.totalSales}
target penjualan    : {self.targetSales}
gaji pokok          : {self.gajiPokok}
komisi dasar        : {self.komisiDasar}
bonus penjualan     : {self.hitungBonusPenjualan()}
pajak               : {self.pajak}
total gaji          : {self.hitungGaji()}
''')

class SalesSenior(Sales):
    def __init__(self, name, totalSales, targetSales):
        super().__init__(name, totalSales, targetSales)
        self.komisiPenjualan = totalSales*0.02
        self.gajiPokok = 5000000

    def hitungGaji(self):
        total_gaji = (self.gajiPokok + self.komisiDasar + self.komisiPenjualan + self.hitungBonusPenjualan())
        gaji_akhir = total_gaji - (total_gaji*self.pajak)
        return gaji_akhir
    
    def tampilkanGaji(self):
        print(f'''
nama                : {self.name}
total penjualan     : {self.totalSales}
target penjualan    : {self.targetSales}
gaji pokok          : {self.gajiPokok}
komisi dasar        : {self.komisiDasar}
komisi penjualan    : {self.komisiPenjualan}
bonus penjualan     : {self.hitungBonusPenjualan()}
pajak               : {self.pajak}
total gaji          : {self.hitungGaji()}
''')

class SalesManager(Sales):
    def __init__(self, name, totalSales, targetSales):
        super().__init__(name, totalSales, targetSales)
        self.komisiPenjualan = totalSales*0.03
        self.bonusTambahan = self.komisiPenjualan*0.01
        self.gajiPokok = 8000000 + self.komisiPenjualan + self.bonusTambahan

    def hitungGaji(self):
        total_gaji = (self.gajiPokok + self.komisiDasar + self.hitungBonusPenjualan())
        gaji_akhir = total_gaji - (total_gaji*self.pajak)
        return gaji_akhir
    
    def tampilkanGaji(self):
        print(f'''
nama                : {self.name}
total penjualan     : {self.totalSales}
target penjualan    : {self.targetSales}
gaji pokok          : {self.gajiPokok}
komisi dasar        : {self.komisiDasar}
komisi penjualan    : {self.komisiPenjualan}
bonus penjualan     : {self.hitungBonusPenjualan()}
bonus tambahan      : {self.bonusTambahan}
pajak               : {self.pajak}
total gaji          : {self.hitungGaji()}
''')

sales1 = SalesSenior('Danu', 2000000, 1500000)

sales1.tampilkanGaji()

