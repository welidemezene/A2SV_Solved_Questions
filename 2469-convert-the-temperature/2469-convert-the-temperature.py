class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        list1 = []
        kelvin = celsius + 273.15000
        fah = celsius * 1.80 + 32.00000
        list1.append(kelvin)
        list1.append(fah)
        return list1
        