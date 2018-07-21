
class Temperature(object):
    # This class stores a temperature in Fahrenheit.  It can be set or retrieved using Kelvin, Celsius, Fahrenheit, or Rankine.

    def __new__(cls, temp, unit):  
        unit = unit.lower()
        
        if unit not in ['k', 'c', 'r', 'f', 'kelvin','celsius','rankine','fahrenheit']:
            raise ValueError('unsupported temperature unit')     

        if not cls.isFloat(temp):
            raise ValueError('temperature must be numeric')
            
        return super(Temperature, cls).__new__(cls)


    def __init__(self, temp, unit):
        unit = unit.lower()
        
        # convert input temperature to a float value
        temp = float(temp)
                
        if unit == 'kelvin' or unit == 'k':
            self.setFromKelvin(temp)
        elif unit == 'celsius' or unit == 'c':
            self.setFromCelsius(temp)
        elif unit == 'rankine' or unit == 'r':
            self.setFromRankine(temp)
        else:
            self.setFromFahrenheit(temp)


    # setters
    def setFromKelvin(self, temp):
        self.fTemp = temp * 9/5 - 459.67
    
    def setFromCelsius(self, temp):
        self.fTemp = temp * 9/5 + 32
        
    def setFromFahrenheit(self, temp):
        self.fTemp = temp
    
    def setFromRankine(self, temp):
        self.fTemp = temp - 459.67
        
    # getters
    def getAsKelvin(self):
        return round( (self.fTemp + 459.67) * 5/9 )
    
    def getAsCelsius(self):
        return round( (self.fTemp - 32) * 5/9 )
    
    def getAsFahrenheit(self):
        return round( self.fTemp )
    
    def getAsRankine(self):
        return round( self.fTemp + 459.67 )

    # utilities
    @staticmethod
    def isFloat(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    def compareTo(self, temp, unit):
        unit = unit.lower()
        
        try:
            valid = True

            if not Temperature.isFloat(temp): # in the test data, this results in "incorrect"
                valid = False
            elif unit == 'kelvin' or unit == 'k':
                correctTemp = self.getAsKelvin()
            elif unit == 'celsius' or unit == 'c':
                correctTemp = self.getAsCelsius()
            elif unit == 'rankine' or unit == 'r':
                correctTemp = self.getAsRankine()
            else:
                correctTemp = self.getAsFahrenheit()

            if ( valid and correctTemp == round( float(temp) ) ):
                return 'correct'
            else:
                return 'incorrect'
        except:
            return 'invalid'

