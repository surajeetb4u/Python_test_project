#************************QUESTION-1************************
"""
data_list=[]
count=int(input("Enter number of elements:"))
for i in range(count):
          num=int(input())
          data_list.append(num)
total=0
for num in data_list:
        print(type(num),num)
        total+=num
print(f"Sum of numbers in {data_list} is {total}")

"""   
#************************QUESTION-2************************
"""
data_list=[]
count=int(input("Enter number of elements:"))
for i in range(count):
          num=int(input())
          data_list.append(num)
print(f"The largest number in {data_list} is {max(data_list)}")

"""
#************************QUESTION-3************************
"""
data_list=[]
count=int(input("Enter number of elements:"))
for i in range(count):
          num=int(input())
          data_list.append(num)
print(f"The smallest number in {data_list} is {min(data_list)}")

"""

#************************QUESTION-4************************
"""
color_list = ["Red","Green","White" ,"Black"]
print(f"First color:{color_list[0]}, Last color:{color_list[-1]}")

"""
#************************QUESTION-5************************
"""
input_str=input("Enter a string:")
length=len(input_str)
if length<3:
    print("Invalid string")
elif input_str[-3:]=='ing':
    input_str=input_str+'ly'
    print("Output:",input_str)
else:
    input_str=input_str+'ing'
    print("Output:",input_str)
"""
#************************QUESTION-6************************
"""
total_marks=0
for i in range(5):
    marks=int(input("Enter numbers obtained in subject"+str(i+1)+":"))
    total_marks+=marks
percentage=total_marks/500*100
if percentage>=60:
    print(f"Your aggregate is {total_marks}, secured {percentage}% and you have passed in 'First Division'.")
elif percentage>=50:
    print(f"Your aggregate is {total_marks},secured {percentage}% and you have passed in 'Second Division'.")
elif percentage>=40:
    print(f"Your aggregate is {total_marks},secured {percentage}% and you have passed in 'Third Division'.")
else:
    print(f"Your aggregate is {total_marks},secured {percentage}% and you are'Fail'.")
"""   
#************************QUESTION-7************************
"""
print("Enter three numbers:")
largest_num=0
for i in range(3):
    num=int(input())
    if num>largest_num:
        largest_num=num
print("The largest number is ",largest_num)
"""
#************************QUESTION-8************************
"""
input_year=int(input("Enter year to check:"))
if input_year%400==0:
    print(f"{input_year} is a Leap Year")
elif input_year%100==0:
    print(f"{input_year} is not a Leap Year")
elif input_year%4==0:
    print(f"{input_year} is a Leap Year")
else:
    print(f"{input_year} is not a Leap Year")
"""
#************************QUESTION-9************************
"""
input_str=(input("Enter a string to check:"))
reverse_str=input_str[::-1]
if input_str==reverse_str:
    print(f"{input_str} is a Palindrome")
else:
    print(f"{input_str} is not a Palindrome")
    
"""
#************************QUESTION-10************************
"""
input_str=(input("Enter a string:"))
output_str=input_str.split()
output_str.sort()
print(output_str)
"""
#************************QUESTION-11************************
"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
for i in sub_list:
    list1[2][1][2].append(i)        
print(list1)
"""
#************************QUESTION-12************************

list1 = [5, 10, 15, 20, 25, 50, 20]
c=list1.count(20)
if c>0:
    posn=list1.index(20)
    list1[posn]=200
    print("Udated list:",list1)
else:
    print("The number 20 is not in the list")
    
