from temperature import Temperature


class Calorie:
    """Represent amount of calories calculated with
    BMR =  10*weight + 6.25*height -5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return result


if __name__ == "__main__":
    temperature = Temperature(country='India', city='Karimnagar').get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())
