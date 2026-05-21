from datetime import datetime

class Penerbangan:
    def __init__(self, departure, pesawat, destination, date, time, price:int):
        self.departure = departure
        self.pesawat = pesawat
        self.destination = destination
        self.date = date
        self.time = time
        self.price = price

Penerbangan01 = Penerbangan('Yogyakarta', 'Boeing', 'Oslo', datetime.strptime("12/05/2026", "%d/%m/%Y").date(), '18:30', 1000000)
Penerbangan02 = Penerbangan('Solo', 'Boeing', 'Florida', datetime.strptime("01/02/2027", "%d/%m/%Y").date(), '08:30', 2000000)