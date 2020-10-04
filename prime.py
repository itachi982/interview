#!usr/bin/python3

num = int(input("Enter a number: "))
def prime(number):

    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                print("false")
                break
        else:
            print("true")
       
    else:
        print("false")

prime(num)
