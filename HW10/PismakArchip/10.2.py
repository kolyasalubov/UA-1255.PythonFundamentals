class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Ласкаво просимо, {self.name}!"

    @classmethod
    def species_info(cls):
        return f"Ми всі є видом {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Це довільне повідомлення."

person = Human("Іван")
print(person.welcome_message())
print(Human.species_info())
print(Human.arbitrary_message())
