"""
Author: Evan Mitchell
Date: September 2, 2021
Assignment: PA01_Repitition_Structutre 
Semester/Year: Fall 2021
Course Number and Title: IS310-01 Adcanced Computer Programming in Business 
About the Program: 
This program takes numbers 100 through 200 and shows the sum of all the numbers as well as both all even and odd numbers within this range.

Input: Takes numbers 100 through 200 and gives the summation. 
Output: The summation of all numbers 100 through 200 and odd and even as well.
"""
print(__doc__)
#This function adds all the numbers         
def add():
    i = 100
    sum1 = 0
    while i <= 200:
        sum1 += i
        i += 1
    return sum1 
#This fucntion adds all even numbers within range
def even():
    i = 100
    sum2 = 0
    while i <= 200:
        if i%2 == 0:
            sum2 = sum2 + i
        else: 
            sum2+=0
        i = i + 1
    return sum2  

#This function adds all odd numbers 

def odd():
    i = 100
    sum3 = 0
    while i <= 200:
        if i % 2 > 0:
            sum3 += i
        else:
            sum3 += 0
        i = i + 1
    return sum3 


def main():
#This calls all the functions and prints the outputs 
    print("Sum of 100 to 200 inclusive: " + str(add()))
    print("Sum of 100 to 200 odd numbers inclusive: " + str(odd()))
    print("Sum of 100 to 200 even numbers inclusive: " + str(even()))


if __name__ == '__main__':
    main()