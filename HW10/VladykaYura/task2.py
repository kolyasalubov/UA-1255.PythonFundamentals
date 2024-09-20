class Human():
    species = "Homosapiens"

    def __init__(self,name):
        self.name = name
    
    def welcome(self):
        return (f"Welcome {self.name}")
    
    @classmethod
    def class_metod(cls):
        return (cls.species)
    @staticmethod
    def arbitrary_message():
        return "Have a good day!" 
    
human1 = Human("Yura")
print(human1.welcome())
print(human1.class_metod())
print(human1.arbitrary_message())