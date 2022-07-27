

# import re
    





# def decorator(func):

#     def inner(value_check):
#         while(True):
#             try:
#                 value_check = int(input("\nPlayer 1: Enter (1) to throw dice: "))
#                 if value_check!=1:
#                     raise Exception()
#                 else:
#                     break
#             except Exception:
#                 print("Please Enter (1) for player1")
#         return func
#     return inner

# @decorator
# def take_input():
#     return 
    
# obj = take_input(1)
class A:
    pass


obj = A()
f = open("game_data.txt", "a")
f.write("\nHello Worlssd\n")
x=1+2
f.write("\nBysse\n")
f.close()

#open and read the file after the appending:
f = open("game_data.txt", "r")
print(f.read())