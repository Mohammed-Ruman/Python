# 1) Write a python class to convert an integer into a roman numeral and viceversa

class Converter:
    def __init__(self):
        self.numeral_map = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

    def to_roman(self, num):
        result = ""
        for numeral, value in self.numeral_map:
            while num >= value:
                result += numeral
                num -= value
        return result

    def from_roman(self, roman):
        result = 0
        index = 0
        for numeral, value in self.numeral_map:
            while roman[index:index+len(numeral)] == numeral:
                result += value
                index += len(numeral)
        return result

# Example usage
converter = Converter()
print(converter.to_roman(354))  
print(converter.from_roman("CCCLIV"))  
