# Реализовать классовую структуру вещей в комнате (на выбор): 
# холодильник, шкаф, тумбочка...Реализовать методы "положить" и "взять":

# ножницы
# книга
# карандаш
# яблоко

goods = {'food':['apple', 'banana'],
         'clothes':['shorts', 'shirt'],
         'item':['pencil', 'book', 'scissors']}

class Storage:
    def __init__(self):
        self.items = []

    def put(self, item):
        if item in goods[self.place]:
            self.items.append(item)
            print(f"{item} помещен в {self.__class__.__name__}.")
        else:
            print(f"{item} не может быть помещен в {self.__class__.__name__}.")

    def take(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} взят из {self.__class__.__name__}.")
        else:
            print(f"{item} не найден в {self.__class__.__name__}.")


class Refrigerator(Storage):
    def __iter__(self):
        return goods['food']

class Wardrobe(Storage):
    def __inin__(self):
        self.place = 'clothes'

    def __iter__(self):
        return goods['clothes']

class BedsideTable(Storage):
    def __iter__(self):
        return goods['item']
    
inner = Wardrobe()
inner.put('shorts')
inner.take('shirt')