import sys
import csv

year = []
month = []
share_price = []
final_dict = {'company': [], 'month': [], 'year': [], 'price' : []}

def read_data(inputstrings):
    filename = inputstrings[1] # getting the csv file name
    try:
        f = open(filename, 'rb') # opens the csv file
    except IOError:
        print "File not found"
        exit()

    data = [row for row in csv.reader(f)] # storing all csv data in the data
    f.close()
    all_company = [item for item in data[0][2:]] # storing all compnies

    # double list to store all share price according to the index of the country
    for i in range(len(all_company)):
        share_price.append([])

    # making data structure for the year, month and share_price 
    for item in data[1:]:
        i = 0
        year.append(item[0])
        month.append(item[1])
        for price in item[2:]:
            share_price[i].append(price)
            i = i + 1

    # finding the max share price according to the requirement and storing them in final dict and then returing it
    j = 0
    for item in share_price:
        if item:
            max_val = max(item)
            ind = item.index(max_val)
            final_dict['company'].append(all_company[j])
            final_dict['month'].append(month[ind])
            final_dict['year'].append(year[ind])
            final_dict['price'].append(max_val)
            j = j + 1

    return final_dict

if __name__ == "__main__":
    all_items = read_data(sys.argv)
    # printing output as company, month, year, max_share_price 
    for i in range(len(all_items['company'])):
        print ('%s, %s, %s, %s') %(all_items['company'][i], all_items['month'][i], all_items['year'][i], all_items['price'][i])

