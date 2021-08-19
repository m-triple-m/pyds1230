class Computer:
    
    def __init__(self, ram, hdd):
        self.ram = ram
        self.hdd = hdd

    def getConfig(self):
        print('From Computer class')


class Laptop(Computer):

    def __init__(self, ram, hdd, wifi):
        super().__init__(ram, hdd)
        self.wifi = wifi

    
    def getConfig(self):
        print('From Laptop class')

class Tablet(Computer):

    def __init__(self, ram, hdd, bluetooth):
        super().__init__(ram, hdd)
        self.bluetooth = bluetooth



lappy = Laptop('4 gb', '1 tb', '802.11ac')

lappy.getConfig()


tab = Tablet('8 gb', '512 gb', '2.3')

tab.getConfig()