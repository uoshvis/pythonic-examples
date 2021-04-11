class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self, name):
        print("Hello, {}!".format(name))


user = Person("BigName", "BenLastName")

print(user.first_name)
# BigName

print(getattr(user, "first_name"))
# BigName

print(getattr(user, "say_hello"))
#<bound method Person.say_hello of <__main__.Person object at 0x7f39a6753c88>>

method = getattr(user, 'say_hello')
method('BigBen')
# Hello, BigBen!



## Pseudo

# if http_method == 'post':
#     requests.post(url, data=data)
# elif http_method == 'put':
#      requests.put(url, data=data)

## Pythonic pseudo

# method = getattr(requests, http_method)
# method(url, data=data)
