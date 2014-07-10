import sys

class QuickSort(object):

    def __init__(self, lis):
        self.start = 0
        self.end = len(lis) - 1
        self.info_list = lis

    def quick_sort(self):
        if start < end:
            pivot = partition(self.info_list, self.start, self.end)
            import pdb; pdb.set_trace()

    def partition(self, start, end):

if __name__ == "__main__":
    to_sort = raw_input("Please Enter List for Sorting:")
    if type(eval(to_sort)) == list:
        obj1 = QuickSort(eval(to_sort))
        import pdb; pdb.set_trace()
        obj1.quick_sort()
   
    else:
        raise Exception("You must provide list for sorting")

