"""
Test file for testing a lot of fucntionalities of python

class animal():
    def __init__(self,name,species=""): #Constructor for the class
        self.name=name
        self.species=species
       
leopard=animal("Leopard")
print(leopard.species)
class mammalia(animal):
    def __init__(self, name):
        super().__init__(name,species="Mammal")
        
p=mammalia("LEOPARD")
print(p.species)

#Testing fucntional decorators in python

def announce(f):
    def wrapper():
        print("Started running the function")
        f()
        print("Done.")
    return wrapper

@announce
def hello():
    print("Hello world")
hello()
"""
#Using Lambda functions

list=[
    {"name":"harry","house":"Gry"},
     {"name":"Cho","house":"Ravenclaw"},
      {"name":"Draco","house":"Slytherin"}
    
]

list.sort(key= lambda list:list["name"])
print(list)
