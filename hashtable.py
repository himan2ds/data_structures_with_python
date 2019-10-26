#!/usr/bin/python3

"""
Implemetation of hash table in python using list and tuples.
The keys are accepted as integers and values the values can
be passed as any data type.
"""

length = 10

hash_table = [None]*10
print(hash_table)

data_to_be_inserted = { 
    2 : 'a', 
    3 : 'c', 
    13 : 'd', 
    10 : 'r', 
    12 : 'x', 
    7 : 'u', 
    18 : 'p', 
    0 : 'n' 
}

def hash_function(key):
    return key % 10 

def insert(key, value):
    pos = hash_function(key)
    if hash_table[pos]:
        hash_table[pos].append(( key, value ))
    else:
        hash_table[pos] = [( key, value )]

def create_table():
   cont = True 
   while cont:
       key = int(input("type key which is an integer "))
       value = input("type value ")
       insert(key, value)
       cont = bool(input("continue? type y/n ") == 'y')
       if not cont:
           break
           
create_table()

print(hash_table)
