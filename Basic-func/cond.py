x = 1
y = 1

#and condition
if x == 1 and y==1:
    print("Yes")
else:
    print("No")

#or condition
if x == 1 or y==2:
    print("Yes")
else:
    print("No")

#conditional block
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

#check value
#message = "hello"
message = [1,2,3]

if isinstance(message,str):
    print ('This is string')
elif isinstance(message,list):
    print ('This is list')

if type(message) == str:
    print ('This is string')
elif type(message) == list:
    print ('This is list')
