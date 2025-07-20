def add(*args):
    #return sum(args)
    print(args[0]) # podemos acceder por posicion, porque es una tuple
    arg_sum = 0
    for arg in args:
        arg_sum += arg
    return arg_sum

print(add(1, 4, 7))

def calculate(n, **kwargs):
    # print(kwargs) es un diccionario
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)

    #print(kwargs["add"]) # permite ver todos los inputs y buscar los que quiero para hacer algo


    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("car")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan")
print(my_car.model)