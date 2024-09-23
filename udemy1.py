class Product:
    def __init__ (self,Pname,Bname,Mname,Price):
        # Product name = Pname
        self.Pname = Pname
        # Brand name = Bname
        self.Bname = Bname
        # model name = Mname
        self.Mname = Mname
        # Price
        self.price = Price

iphone_X = Product('iPhone_X','Apple','Phone','¢2100')
print(iphone_X.Pname)
print(iphone_X.Bname)
print(iphone_X.Mname)
print(iphone_X.price)

print("////////////////////////////////////////////////////////////////")
mac = Product('Macbook','Apple','Laptop','¢10k')
print(mac.Pname)
print(mac.Bname)
print(mac.Mname)
print(mac.price)
        