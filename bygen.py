import csv
import time
dict_item = {
    'id':[],
    'item': { 
         'items' : [],
         'price': []
         }
    }
def read_files(filenames):
    for name in filenames:
        try:
            openfile = open(name, 'rb')
        except IOError:
            print "File not found"
            exit()
        reader = csv.reader(openfile)
        for line in reader:
            yield line

def getitemsmatch(pattern, dict_item, start):
    max_list = []
    min_price = []
    for ind, item in enumerate(dict_item['id']):
        min_val = min(dict_item['item']['price'][ind])
        min_index = dict_item['item']['price'][ind].index(min_val)
        match = set(dict_item['item']['items'][ind][min_index]) & set(pattern)
        if match == set(pattern):
            if min_price:
                if min_price > min_val:
                    min_price[0] = min_val 
            else:
                max_list.append(item)
                min_price.append(min_val)

        else:
            dict_item['item']['price'][ind].remove(min_val)
            # will need to implement this here 

       
    end = time.time() 
    print dict_item, end-start
        
def printlines(pattern, lines, start):
    for line in lines:
        if len(line) >=1:
            if int(line[0]) in dict_item['id']:
                #import pdb; pdb.set_trace()
                st = []
                ind = dict_item['id'].index(int(line[0]))
                if set([i for i in pattern]) & set([l.strip() for l in line[2:]]):
                    indexval = 0
                    try:
                        #import pdb; pdb.set_trace()
                        length = len(dict_item['item']['price'][ind])
                        min_price = min(dict_item['item']['price'][ind])
                        if line[1].strip() < dict_item['item']['price'][ind][length - 1]: 
                            dict_item['item']['price'][ind].insert(length-1, line[1].strip())
                            indexval = length - 1
                        else:
                            dict_item['item']['price'][ind].insert(indexval, line[1].strip())
                    except IndexError:
                        dict_item['item']['price'].append([line[1].strip()])
                    for val in line[2:]:
                        #import pdb; pdb.set_trace()
                        if val.strip() in pattern:
                            st.append(val.strip())
                    try:
                        dict_item['item']['items'][ind].insert(indexval, st)
                    except IndexError:
                        dict_item['item']['items'].append([st])
                   
            else:
                #import pdb; pdb.set_trace()
                st = []
                dict_item['id'].append(int(line[0]))
                if set([i for i in pattern]) & set([l.strip() for l in line[2:]]):
                    dict_item['item']['price'].append([line[1].strip()])
                    for val in line[2:]:
                        #import pdb; pdb.set_trace()
                        if val.strip() in pattern:
                            st.append(val.strip())
                    dict_item['item']['items'].append([st])
   
    # function call
    getitemsmatch(pattern, dict_item, start)   

def main_function(pattern, filenames):
    start = time.time()
    lines = read_files(filenames)
    printlines(pattern, lines, start)


main_function(["tea", "toffee"], ['sample_data_4.csv'])
