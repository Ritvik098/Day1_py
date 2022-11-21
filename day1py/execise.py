# # Ex 1
sen = "Hello World\n"
print(sen*5)

#Ex 2
print ((99**3)*8)


# #Ex 4
computer_brand = "Mac"
print(f'I have a {computer_brand} computer')

# #Ex 5
name="Ritvik"
age="23"
shoe_size="43"
info=f'My name is {name} i am {age} and my shoe size is {shoe_size}....just in case you were wondering'

print(info)

#Ex 6
a = input("Enter number: ")
b = input("Enter another number: ")
if a>b:
    print ("Hello World")
else:
      (print("try again") )

#Ex 7
testnum = input("Enter a number to see if its odd or even: ")
if int(testnum)%2 == 0:
     print (f"The numer {testnum} is Even")
else:
     print(f"The numer {testnum} is odd")
     
#Ex 8
usrname = input("Whats your name?")
if usrname.lower() == "Ritvik":
     print("DONE!!")
else:
     print("Successfully")

# Ex 9

height = input("Enter height in Inches: ")
if (int(height)*2.54) > 145:
     print("You can ride")
else:
     (print("Come back when you've grown some more."))
     
     
#EX GOLD
# Ex 1
print("Hello World\n"*5+"I love python\n"*5)

# Ex 2
month=input("Enter a Month: ")
imonth=int(month)
if 3 <=imonth <=5:
    print("Spring")
elif 6 <=imonth <=8:
        print("Summer")
elif 9 <=imonth <=11:
    print("Autumn")
elif 12 ==imonth or 1<= imonth<=2:
    print("Winter")
elif imonth> 12:
    print("Error")


#EX NINJA
#ex4 --
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

#Ex 5

flag = True
word=input("Enter a word: ")
new_word=""
while flag is True:
    if len(new_word)>len(word):
        if "a" not in new_word:
           print("Congratulations")
           word = new_word
           break
    elif new_word == "q":
        flag = False    

    else: new_word = input("Enter another word: ")


#Daily Challenge
import random
sentance = input("Enter sentence with 10 characters long: ")
if len(sentance) == 10:
    for x in range(11):
        print(sentance[0:x])
        lsentance=list(sentance)
        random.shuffle(lsentance)
    print(("Randomised: ")+ "".join(lsentance))
elif len(sentance)>10:
    print ("String too long")
elif len(sentance)<10:
    print ("String too short")

print ("first characters: " + sentance[0])
print ("last characters: " + sentance[-1])