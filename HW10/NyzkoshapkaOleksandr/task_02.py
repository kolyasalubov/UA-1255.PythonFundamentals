class Human():
    def __init__(self, human_name):
        self.human_name = human_name

    def  greeting(self):
        print(f"Welcome, {self.human_name} ")

    @classmethod
    def species(cls):
        return "It is a species of Homosapiens"
    
    @staticmethod
    def arbitary_message ():
        return "Hello, people"


human_1 = Human("Oleh")
human_1.greeting()
print(human_1.species())
print(human_1.arbitary_message())