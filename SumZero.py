class Lsequence(object):
    """ This will give you the max list of items for which two items sum is zero \
        from the given list.
        Example : if list is having items [1, -2, 2, 3, -3, -2, 2, 3, -3, 3 , -3, 3, 4,-4, -4, 4]
                  then output will be [-2, 2, 3, -3, -2, 2, 3, -3, 3, -3, 4, -4, -4, 4]        
    """
    def __init__(self, data):
        self.data = data
        self.items = []
        self.nextitem = 0

    def getItems(self):
        for i, item in enumerate(self.data):
            self.nextitem = i + 1
            for j, item1 in enumerate(self.data[self.nextitem:]):
                if item1 + item == 0:
                    import pdb; pdb.set_trace()
                    self.data.pop(self.nextitem + j)
                    self.items.append(item)
                    self.items.append(item1)
                    break
        return self.items

if __name__ == "__main__":
    input_val = raw_input("Enter the list Items:")
    if type(eval(input_val)) == list:
        obj1 = Lsequence(eval(input_val))
        print obj1.getItems()
    else:
        raise Exception("You must provide list")


