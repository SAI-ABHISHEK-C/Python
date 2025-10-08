class TemperatureConverter:
    def CelciusAndFahrenheit(self,unit,n):
        if unit.lower() == "c":
            f = (float(n) * 9 / 5) + 32
            return round(f,2), "Fahrenheit" , n, "Celcius"

        elif unit.lower() == "f":
            c = (5/9) * (float(n) - 32)
            return round(c,2) ,"Celcius" , n , "Fahrenheit"


t = input("Is the temperature in Celsius or in  Fahrenheit? (C or F) :")
while True:
    if t.lower() == "c" or t.lower() == "f":
        break
    else:
        t = input("Enter a valid Unit of temperature (C or F) :")

n = input("What is the temperature : ")
while True:
    try:
        n = float(n)
        break
    except ValueError:
        n = input("Please enter a number : ")


a , unit1, b, unit2  = TemperatureConverter().CelciusAndFahrenheit(t,n)
print(f"The temperature is", b, f"in °{unit2} is same as that of ", a, f"in °{unit1}")