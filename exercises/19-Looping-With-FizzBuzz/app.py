import random

# def fizz_buzz():
#     for i in range(1, 101):
#         if (i % 3 == 0):
#             print("Fizz")
#         elif (i % 5 ==0):
#             print("Buzz")
#         elif (i % 3 == 0) and (i % 5 == 0):
#             print("FizzBuzz")
#         print(i)
   
# fizz_buzz()

def fizz_buzz():
# your code here
    for i in range(1,101):
        if (i % 3 == 0):
            print ("Fizz")
            continue
        elif (i % 5==0):
            print("Buzz")
            continue
        elif (i % 3 == 0) and (i % 5==0):
            print("FizzBuzz")
        print(i)
    
fizz_buzz()