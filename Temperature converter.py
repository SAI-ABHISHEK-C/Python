from itertools import count


class TemperatureConverter:
    def CelciusAndFahrenheit(self,count):
        self.count = count +1
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
        if t.lower() == "c":

            f = (float(n) * 9 / 5) + 32
            with open ("history.txt", "a") as file:
                file.write(f"{self.count}. Input : {n} , Unit : Celcius " + "\n" + f"\tOutput: {f} , Unit : Fahrenheit\n\n")
            return round(f,2), "Fahrenheit" , n, "Celcius" , self.count

        elif t.lower() == "f":
            c = (5/9) * (float(n) - 32)
            with open ("history.txt", "a") as file:
                file.write(f"{self.count}. Input : {n} , Unit : Fahrenheit " + "\n" + f"\t Output: {c} , Unit : Celcius \n\n")
            return round(c,2) ,"Celcius" , n , "Fahrenheit" ,self.count
count = 0
a , unit1, b, unit2 ,count  = TemperatureConverter().CelciusAndFahrenheit(count)
print(f"The temperature is", b, f"in °{unit2} is same as that of ", a, f"in °{unit1}")
ans = input("Do you want to continue ? (Y or N) :")
while ans.lower() == "y":
    a, unit1, b, unit2 , count = TemperatureConverter().CelciusAndFahrenheit(count)
    print(f"The temperature is", b, f"in °{unit2} is same as that of ", a, f"in °{unit1}")
    ans = input("Do you want to continue ? (Y or N) :")
    if ans.lower() != "y":
        break

