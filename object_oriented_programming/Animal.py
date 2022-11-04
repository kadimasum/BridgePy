from IAnimal import IAnimal

'''
Create class Animal that extends abstract class IAnimal
'''
class Animal(IAnimal):

    all_animals = {}
    index = 0

    def __init__(self, name:str, age:int, color:str, weight:float):
        # Validate name and color
        assert len(name) > 0, "Name cannot be empty"
        assert len(color) > 0, "Color cannot be empty"
        assert type(age) == int, "Age should be an integer"
        assert type(weight) == float, "Weight has to be a float"

        # Add double underscores before the variables to make them private
        self.__name = name
        self.__age = age
        self.__color = color
        self.__weight = weight

    
    # Add getter methods
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight


    # Add setter methods
    @name.setter
    def name(self,name):
        if type(name) == str:
            self.__name = name
        else:
            raise TypeError("Name must be a string.")

    @age.setter
    def age(self, age:int):
        if type(age) == int:
            self.__age = age
        else: raise TypeError("Age must be an integer")

    @color.setter 
    def color(self, color):
        if type(color)  == str:
            self.__color = color
        else:
            raise TypeError("Color must be a string")

    @weight.setter
    def weight(self, weight):
        if type(weight) == float:
            self.__weight = weight
        else: raise TypeError("Weight must be a floating point number")

    # Instance method 
    def save_animal(self):
        Animal.all_animals[Animal.index + 1] = self
        Animal.index += 1

    # Class method
    @classmethod
    def get_animal_by_id(cls,id):
        if id in cls.all_animals:
            return cls.all_animals[id]

    @classmethod
    def get_all_animals(cls):
        return cls.all_animals

    def delete_animal(id):
        del Animal.all_animals[id]

    def clear_all():
            Animal.all_animals = {}

    # Method is not related to the instance
    @staticmethod
    def size():
        return Animal.index

    # Return the string representation of the instance
    def __repr__(self) -> str:
        return f"<Animal name: {self.__name}, age: {self.__age}, color: {self.__color}, weight: {self.__weight}>"

dog = Animal('Dog', 13, "brown", 12.6)
cat = Animal('Cat', 5, "white", 1.5)

dog.save_animal()
cat.save_animal()
Animal.clear_all()
# print(Animal.size())