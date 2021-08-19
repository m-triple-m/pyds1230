class Laptop:

    # ram = '8gb'
    # ssd = '512gb'
    # processor = 'intel i5'

    def __init__(self, ssd, processor, r = '4 gb',):
        self.ram = r
        self.storage = ssd
        self.processor = processor

    def playGame(self):
        print('laptop plays games')

    def playVideo(self):
        print('Laptop plays videos')

    def getConfiguration(self):
        print(f'RAM : {self.ram}, Processor : {self.processor}, Storage : {self.storage}')


lappy = Laptop('1tb', 'intel i3')

print(lappy.ram)

lappy.ram = '16 gb'
print(lappy.ram)

print(lappy.processor)
print(lappy.storage)

lappy.playGame()

lappy2 = Laptop('512', 'ryzen 5', '16 gb')

print(lappy2.processor, lappy2.ram, lappy2.storage)

lappy2.getConfiguration()
lappy.getConfiguration()