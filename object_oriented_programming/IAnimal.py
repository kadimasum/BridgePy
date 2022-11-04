'''
Import Abstract base class(ABC) from the abc module and absttract class method to allow the creation of abstract methods
'''

from abc import ABC, abstractclassmethod

'''
Inherit the abstract base class
'''
class IAnimal(ABC):

    '''
    Abstract classmethod decorator makes the method abstract
    '''
    @abstractclassmethod
    def save_animal(self):
        pass

    @abstractclassmethod
    def get_animal_by_id(id):
        pass

    @abstractclassmethod
    def get_all_animals():
        pass

    @abstractclassmethod
    def delete_animal(id):
        pass

    @abstractclassmethod
    def clear_all():
        pass
