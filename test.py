my_name = "Matej"
print(my_name)
print("My name is " + my_name)
print("My name is %s" % my_name)

name = raw_input("Please enter your name: ")
print("Howdy, %s" % name)


if name == "Mitja":
    print("Hello Mitja")
    kakosi = raw_input("Kako si?")
    print("Vidim da si %s" % kakosi)
else:
    print("Hello %s" % name)


num = 1
while num < 10:
    print(num)
    num += 1
