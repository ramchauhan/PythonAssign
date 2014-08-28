""" How to make a dictionary form a list of elelment """
list_val = ["k1", "l1", "k2", "l2", "k3", "l3"]
final_dict = [{key:val} for key, val in zip(list_val[0:len(list_val):2], list_val[1:len(list_val):2])]
#Or
f_dict = dict(zip(list_val[0:len(list_val):2], list_val[1:len(list_val):2]))


""" how to find the list of values which is repeted in the given list """

list_values = [1,1,2,2,4,3,3,3]
f_list = [val for val in set(list_values) if list_values.count(val) > 1]


