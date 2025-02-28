#1
input_list=input("Input list:")
my_list=list(map(int, input_list.split()))
multiplay=1
for i in my_list:
    multiplay*=i
print(multiplay)


#2
def count_letters(letter):
    upper=0
    lower=0
    for i in letter:
        if i>="A" and i<="Z":
            upper+=1
        elif i>="a" and i<="z":
            lower+=1
    print("Number of upper case:", upper)
    print("Number of lower case:", lower)
            
sentence=str(input("Enter sentence:"))
count_letters(sentence)


#3
def polindrom(s):
    i=0
    j=len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
        
sentence=str(input("Enter sentence:"))
print(polindrom(sentence))


#4
import math
import time

num=int(input("Enter number:"))
miliseconds=int(input("Enter miliseconds:"))

print(f"Square root of {num} after {miliseconds} miliseconds is {math.sqrt(num)}")


#5
size_mylist=input("Enter  mylist:")
mylist=list(map(int, size_mylist.split()))
print("All True mylist:", all(mylist))