class Shopping:
    cart = [] # class attribute  static attribute
    origin = 'china'

    def __init__(self,name, location):
        self.name = name
        self.location = location
    
    def purchase(self ,item,price,amount):
        remaining = amount - price
        print(f'fidjf skfjdf {remaining} skdfjosf   {item}' )

    @staticmethod
    def multi(a,b):
        return a*b
    
    @classmethod
    def hudai_dekhi(self,item):
        print("hudai dekhi kintu kimu na")


b = Shopping('ffff','dddddddd')

Shopping.hudai_dekhi('fid')

print(Shopping.multi(3,4))