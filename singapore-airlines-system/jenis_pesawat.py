class JenisPesawat:
    def __init__(self, name, seatCapacity, maxSpeed, planeRange):
        self.name = name 
        self.seatCapacity = seatCapacity
        self.maxSpeed = maxSpeed
        self.planeRange = planeRange

boeing = JenisPesawat('Boeing', 120, 920, 17000)
airBus = JenisPesawat('AirBus', 200, 650, 12000 )