# data structure in list of python code 

numbers = list(range(10));
removed_numbers = numbers[::2];
print(numbers);
print(f"{numbers[::2]}");

# List unpaccking

num = [1,2,3];
x,y,z = num;
print(x,y,z);
# we can also write in manually
# x= num[0];
# y=num[1];
# z= num[2];

# if i do x,y = num; that will give error as list is not indexable
# so overcome that error  we use * operator
# x,*others = num;
# print(x,others); // 1 [2, 3]

# def multiply(*arg):
#     return      # it will convert all the ARGUMENTS into a tuple
  
# multiply(1,2,3,4,5);

#Add and Remnove elements from list

letters =["a","b","c"];
print(letters);
letters.append("d");
print(letters);
letters.remove("b");
print(letters);
letters.insert(1,"b");
print(letters);
letters.pop();
print(letters);