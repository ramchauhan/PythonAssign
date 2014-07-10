import sys
class SumOfThreeFive(object):
    ''' This will calculate the sum of the numbers which is multiple of 3 and 5 '''

    def __init__(self, number):
        self.number = number

    def getsum(self):
        sum1 = 0
        return sum([sum1 + i for i in range(0, self.number) if i % 3 == 0 or i % 5 == 0])

if __name__ == "__main__":
  
    input_val = raw_input("Enter the Range:")
    if type(eval(input_val)) == int:
        obj1 = SumOfThreeFive(eval(input_val))
        print obj1.getsum()   
    else:
        raise Exception("You must provide list for sorting") 
