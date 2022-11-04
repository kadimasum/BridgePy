from Animal import Animal

class Cow(Animal):

    def __init__(self, name: str, age: int, color: str, weight: float, breed:str):
        super().__init__(name, age, color, weight)
        assert len(breed) > 0, "Breed cannot be empty"
        self.breed = breed


    def talk():
        return "Mooowwwww"


cow_1 = Cow("Milky", 13, "Brown", 34.2, "Persian")
cow_1.save_animal()
print(cow_1.name)