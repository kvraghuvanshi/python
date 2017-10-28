import sys
import os
def main():
     print('\n')
     print("Hello world!!!")
     print("\n")
     print("I am Kirtivardhan Singh...")
     print ("This is my first program...")
     print('\n')
     print("There are three items in the list, that are:-")
     list = ['Linux','Windows','Mac ']
     print("The first item is" , list[0])
     print("The second item is" ,list[1])
     print("THe third item is" , list[2])
     l1=4000
     l2=4000
     l3=12000
     print("The cost of ", list[0], "=", l1)
     print("The cost of ", list[1], "=", l2)
     print("THe cost of ", list[2], "=", l3)
     print('\n')
     print("Total amount= ", l1+l2+l3 )
     print("Review all items", list[0:3])
     os.system("pause")

main()