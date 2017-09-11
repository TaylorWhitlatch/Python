# def say_hello_with_name(name):
#     print "Hello, %s" % name
#
# say_hello_with_name(Jim)
# say_hello_with_name(Ted)
#
# students = ['Jim','James','Jed']
# for i in range(0,len(students)):
#     say_hello_with_name(students[i])

def say_hello_with_safe(name, in_class="Yes"):
    print "%s, %s is in class" % (in_class, name)

say_hello_with_safe("Jim")
say_hello_with_safe("Dan", "No")

def return_user_name(name):
    normal_name = name.upper()
    return normal_name
