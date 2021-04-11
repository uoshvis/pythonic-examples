class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def say_hello(name):
        print "Hello, {}!".format(name)
       
user = Person("Big", "Ben")

print(user.first_name)

print(getattr(user, "firs_name")
      
print(getattr(user, "say_hello")
      
method = getattr(user, "say_hello")
method("Ten o'clock")
