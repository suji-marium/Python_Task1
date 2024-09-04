"""x=float(input("Enter the fahrenheit temperature: "))
y=((x-32)*5)/9

print("The temperature in celsius: ",y)

z=(y*(9/5))+32
print("The temperature in fahrenheit",z)"""

class Conversion:

    def __init__(self,temp):
        self.temp=temp

    def fah_to_cel_and_back(self):
        cel=((self.temp-32)*5)/9
        fah=(cel*(9/5))+32
        print("The temperature in celsius:",cel)
        print("The temperature in fahrenheit", fah)

con=Conversion(float(input('Enter the temperature: ')))
con.fah_to_cel_and_back()