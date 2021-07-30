# Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections : Problem 1
"""
def con_temp():
    while True:
        try:
            temp_cel = float(input("Enter a temperature in Celsius: "))
            temp_fah = ((9 / 5) * (temp_cel)) + 32
            print(" %.2f  in Celsius: is %.2f Fahrenheit" % (temp_cel, temp_fah))
            return con_temp()
        except ValueError:
            print("Please enter a valid floating point for the temperature.")
        else:
            break
if __name__ == '__main__':
    con_temp()
    temp_cel = float(input("Enter a temperature in Celsius: "))
    print(" %.2f  in Celsius: is %.2f Fahrenheit" % (temp_cel, temp_fah))