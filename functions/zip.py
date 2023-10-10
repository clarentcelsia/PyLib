# -*- coding: utf-8 -*-

# FUNCTION

def zip_():
    name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
    roll_no = [ 4, 1, 3, 2 ]
    
    # using zip() to map values
    mapped = zip(name, roll_no)
    
    print(set(mapped)) #{('Shambhavi', 3), ('Manjeet', 4), ('Nikhil', 1), ('Astha', 2)}
    
    for name, roll_no in list(zip(name, roll_no)):
        print(name, " ", roll_no)
        print()
