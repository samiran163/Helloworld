class Cars():
    def __init__(self,modelname,year,price):    #this is like creating a constructor
        self.modelname = modelname
        self.year = year
        self.price =price
    def price_in(self):                         #here we have defined a function
        self.price = int(self.price*1.15)

honda = Cars('city',2017,10000)
tata = Cars('bolt',2016,20000)

honda.cc = 1600   #creating an instance variable of an honda object

'''honda.modelname = 'city'
honda.year=2017
honda.price = 100000

tata.modelname = "bolt"
tata.year = 2017
tata.price = 200000'''

print(honda.__dict__)
print(honda.price)
honda.price_in()     #...................calling of price_in function
print(honda.price)