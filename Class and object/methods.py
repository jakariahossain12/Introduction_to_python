class phone:
    price = 1999
    brand = "samsung"
    color = "black"

    def call(self):
        print("calling one person")

    def send_ms(self,phone , sms):
        text = f'sending  sms to : {phone} and message {sms}'
        return text



class calculator:

    def add(self,num,num2):
        return num+num2
    def de(self,num,num2):
        return num-num2
    def mul(self,num,num2):
        return num*num2

c = calculator()
print(c.mul(3,4))