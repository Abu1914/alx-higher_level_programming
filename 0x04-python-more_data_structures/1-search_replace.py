#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [j if j != search else replace for j in my_list]
    return (new)
