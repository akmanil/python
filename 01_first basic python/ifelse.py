cond = True;

if cond:
    print("Hello this is if statement");
else:
    print("End");

# for taking input from the user use input

input_value = input("enter the value :");
print ("entered value is :",input_value);

if int(input_value) > 9 :
    print("The value you entered is Double digit or more than that");

else :
    print("its single digit number");

# we also have elseif statematenbt\
a = input("Enter the number to check its range :");

if int(a)>= 10 and int(a) <=99 :
    print("The value is Double digit number")
elif int(a) <= 9:
    print("The vaalue u are entered this is single digit number");
else :
    print ("More than the double digit number");

# used nested if statement

age = int(input("enter ur age : "));
country = input("Enter ur contry : ");

if age >= 18 :
    if country == "india":
      print("you are vote in india");
    else:
        print("your are not belong to india so ur not vote");
else:
    print("your age not enough to vote");



   


