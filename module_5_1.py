from module2_7  import  value


class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)
    def  __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название:{self.name},кол-во этажей:{self.number_of_floors}")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
    def __gt__(self, other):
        return self.__le__(other)
    def __ge__(self, other):
        return not self.__lt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print(h1==h2)
print(h1<h2)
print(h1<=h2)
print(h1>h2)
print(h1>=h2)
print(h1!=h2)
h1 = h1 + value
print(h1)
print(h1 == h2)
del h1
print(House.houses_history[0])
print(House.houses_history[-1])
del h2
print(House.houses_history)
