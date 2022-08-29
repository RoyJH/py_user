from warnings import catch_warnings


print ("Hello, what is your name?")
user = input()
print ("Hello " + user +"!")
print ("It's a pleasure to know you.")
print ("How old are you?")
#print ("enter your age")

age = input("enter your age")
ageint = int(age)
if (ageint < 5):
    print (age + " years old huh?  Wow, you're still a baby!")

elif (ageint <= 17):
    print (age + " years old, you're just getting started!")

elif (ageint <35 ):
    print (age + " years old?  Well you've successfully made it to adulting!")

elif (ageint >= 55):
    print (age + " years old huh?  Got quite a bit of experience I bet!")
