# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables, just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help our user log in
    def login(self):
        self.logged = True
        print self.name + " is logged in"
        return self
# now create an instance of the class
new_user = User("Anna", "anna@anna.com")
print new_user.email

class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change: ", anna.name
bob = User()
print "bob's name: ", bob.name