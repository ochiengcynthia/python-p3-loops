#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print (i)
        i = i - 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = [x ** 2 for x in int_list]
    return squared_list
    pass

def fizzbuzz(num):
    #for num in range (1, 101):
     if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz" 
     elif num % 3 == 0:
        return "Fizz"
     elif num % 5 == 0:
        return "Buzz"
     else:
        print (num)
        pass
    
