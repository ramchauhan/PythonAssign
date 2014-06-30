import sys
import csv

class MaxCast(object): 
    inputstrings = sys.argv
    final_dict = {'company': [], 'month': [], 'year': [], 'price' : []}
    def argsparse(self):
        if(len(sys.argv)) <= 1:
            raise Exception("Argument Error: Too few Arguments")
        else:
            self.filename = self.inputstrings[1]
            try:
                self.csvf = open(self.filename, 'rb') # opens the csv file
            except IOError:
                raise IOError("File not found, please check the filename")
            self.reader = csv.reader(self.csvf)

    def read_data(self):
        year = []
        month = []
        share_price = []
        for ind, item in enumerate(self.reader):
            i = 0
            if ind == 0:
                self.company_name = item[2:]
                for i in range(len(self.company_name)):
                    share_price.append([])
            else:
                year.append(item[0])
                month.append(item[1])
                for price in item[2:]:
                    share_price[i].append(price.strip())
                    i = i + 1

        j = 0
        for price in share_price:
            if price:
                max_val = max(price)
                ind = price.index(max_val)
                self.final_dict['company'].append(self.company_name[j])
                self.final_dict['month'].append(month[ind])
                self.final_dict['year'].append(year[ind])
                self.final_dict['price'].append(max_val)
                j = j + 1 
 
        return [(self.final_dict['company'][i], self.final_dict['month'][i], self.final_dict['year'][i], self.final_dict['price'][i]) for i in range(len(self.final_dict['company']))]       

if __name__ == "__main__":
    max_cast = MaxCast()
    max_cast.argsparse()
    max_cast.read_data()
    print [(max_cast.final_dict['company'][i], max_cast.final_dict['month'][i], max_cast.final_dict['year'][i], max_cast.final_dict['price'][i]) for i in range(len(max_cast.final_dict['company']))]
 

