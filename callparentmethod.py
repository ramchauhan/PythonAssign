#this program will show you how to call parent class method in python

class Room(object):
    
    def __init__(self, items):
        self.items = items
 
    def getItems(self):
        return self.items

class Item(Room):
    """ calling parent class method """
    def getItems(self):
        super(Item, self).getItems()
        print "calling parrent class method from child class"


obj1 = Room(10)
print obj1.getItems()


