# WindchillCalculator.py
# Your job is to write a function in BMICalculator.py (call
# it **calculateWindchill()** that calculates the windchill # factor based on the New Wind Chill Index from 
# Calculator.net (http://www.calculator.net/wind-chill-calculator.html)

# Define Function below
# be sure to return an integer

import math
def calculateWindchill(V, T):
    Windchill = 35.74 + (0.6215*T) - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    Windchill = round(Windchill)
    return Windchill


if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
    answer = calculateWindchill(5, 40)
    print(answer)
